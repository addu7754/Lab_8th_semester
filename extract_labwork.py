import re
import os
import argparse

def sanitize_filename(name):
    name = re.sub(r'[^\w\s.-]', '', name)
    name = name.strip().replace(' ', '_')
    if not name:
        return 'code_snippet'
    return name

def process_weeks(start_week, end_week):
    with open('lab_file.tex', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    current_week = 0
    current_question = 0
    question_title = ""
    question_content = []
    
    in_listing = False
    current_code = []
    current_lang = None
    current_caption = None

    week_re = re.compile(r'\\fancyhead\[R\]\{Week (\d+)\}')
    subsec_re = re.compile(r'\\subsection\*?\{(.*?)\}')
    listing_start_re = re.compile(r'\\begin\{lstlisting\}')
    listing_end_re = re.compile(r'\\end\{lstlisting\}')

    def save_question():
        if current_week == 0 or current_question == 0 or not question_content:
            return
        if not (start_week <= current_week <= end_week):
            return
            
        dir_name = f"Week_{current_week:02d}"
        os.makedirs(dir_name, exist_ok=True)
        
        md_filename = os.path.join(dir_name, f"Question_{current_question}.md")
        with open(md_filename, 'w', encoding='utf-8') as f_md:
            f_md.write(f"# Question {current_question}: {question_title}\n\n")
            f_md.writelines(question_content)

    for line in lines:
        week_match = week_re.search(line)
        if week_match:
            save_question()
            current_week = int(week_match.group(1))
            current_question = 0
            question_content = []
            continue

        subsec_match = subsec_re.search(line)
        if subsec_match:
            save_question()
            current_question += 1
            question_title = subsec_match.group(1)
            question_content = []
            continue

        if current_question > 0:
            if listing_start_re.search(line):
                in_listing = True
                lang_match = re.search(r'language=([A-Za-z]+)', line)
                caption_match = re.search(r'caption=\{(.*?)\}', line)
                
                current_lang = lang_match.group(1) if lang_match else 'txt'
                current_caption = caption_match.group(1) if caption_match else ''
                current_code = []
                
                md_lang = current_lang.lower()
                if md_lang == 'bash': md_lang = 'sh'
                question_content.append(f"\n```{md_lang}\n")
                continue

            if listing_end_re.search(line) and in_listing:
                in_listing = False
                question_content.append("```\n\n")
                
                if start_week <= current_week <= end_week:
                    dir_name = f"Week_{current_week:02d}"
                    os.makedirs(dir_name, exist_ok=True)
                    
                    file_ext = {'Python': 'py', 'HTML': 'html', 'XML': 'xml', 'bash': 'txt', 'CSS': 'css', 'JavaScript': 'js'}.get(current_lang, 'txt')
                    
                    fname_match = re.search(r'([a-zA-Z0-9_-]+\.[a-zA-Z0-9]+)', current_caption)
                    if current_lang.lower() == 'bash':
                        current_filename = f"Q{current_question}_output.txt"
                    elif fname_match:
                        current_filename = fname_match.group(1)
                    else:
                        clean_cap = sanitize_filename(current_caption)
                        if not clean_cap:
                            clean_cap = f"Q{current_question}_code"
                        clean_cap = clean_cap[:30]
                        if clean_cap.endswith('_'): clean_cap = clean_cap[:-1]
                        current_filename = f"{clean_cap}.{file_ext}"
                        
                    base, ext = os.path.splitext(current_filename)
                    final_filename = current_filename
                    counter = 1
                    while os.path.exists(os.path.join(dir_name, final_filename)):
                        final_filename = f"{base}_{counter}{ext}"
                        counter += 1
                        
                    with open(os.path.join(dir_name, final_filename), 'w', encoding='utf-8') as out_f:
                        out_f.writelines(current_code)
                continue

            if in_listing:
                current_code.append(line)
                question_content.append(line)
            else:
                clean_line = line
                clean_line = re.sub(r'\\textbf\{(.*?)\}', r'**\1**', clean_line)
                clean_line = re.sub(r'\\textit\{(.*?)\}', r'*\1*', clean_line)
                clean_line = clean_line.replace('\\begin{itemize}', '')
                clean_line = clean_line.replace('\\end{itemize}', '')
                clean_line = clean_line.replace('\\begin{enumerate}', '')
                clean_line = clean_line.replace('\\end{enumerate}', '')
                clean_line = clean_line.replace('\\begin{description}', '')
                clean_line = clean_line.replace('\\end{description}', '')
                clean_line = re.sub(r'\\item\[(.*?)\]', r'- **\1** ', clean_line)
                clean_line = re.sub(r'\\item', r'- ', clean_line)
                clean_line = re.sub(r'\\\\', '', clean_line)
                clean_line = re.sub(r'\\newpage', '', clean_line)
                clean_line = re.sub(r'\\vspace\{.*?\}', '', clean_line)
                # Ignore pure latex commands that span lines or are too noisy, but keep simple text
                if '\\subsubsection' in clean_line:
                    clean_line = clean_line.replace('\\subsubsection*{', '### ').replace('\\subsubsection{', '### ').replace('}', '')
                if '\\paragraph' in clean_line:
                    clean_line = clean_line.replace('\\paragraph{', '#### ').replace('}', '')
                
                # strip out comments
                if clean_line.strip().startswith('%'):
                    continue

                if clean_line.strip() or line.strip() == '':
                    question_content.append(clean_line)

    save_question()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--start', type=int, required=True)
    parser.add_argument('--end', type=int, required=True)
    args = parser.parse_args()
    process_weeks(args.start, args.end)
    print(f"Extracted weeks {args.start} to {args.end} successfully.")
