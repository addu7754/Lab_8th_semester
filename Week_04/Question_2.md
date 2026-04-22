# Question 2: Complex Table Merging (Rowspan \& Colspan)


**Problem Statement:** 
Write HTML code to generate the following output layout:

\begin{center}
\renewcommand{\arraystretch}{1.5} % Increases row height slightly for better look
\begin{tabular}{|c|c|c|c|}
\hline
1 & 2 & 3 & 4  \hline
5 & \multicolumn{2}{c|}{\multirow{2}{*}{**Image**}} & 6  \cline{1-1} \cline{4-4} 
7 & \multicolumn{2}{c|}{} & 8  \hline
9 & 10 & 11 & 12  \hline
\end{tabular}
\end{center}

**Source Code Solution:**


```html
<!DOCTYPE html>
<html>
<head>
    <title>Complex Table Layout</title>
    <style>
        table {
            border-collapse: collapse;
            width: 50%;
            text-align: center;
        }
        td {
            border: 1px solid black;
            padding: 15px;
            font-size: 18px;
        }
        img {
            display: block;
            margin: auto;
            max-width: 100px; /* Adjust image size */
        }
    </style>
</head>
<body>

    <table>
        <tr>
            <td>1</td>
            <td>2</td>
            <td>3</td>
            <td>4</td>
        </tr>
        <tr>
            <td>5</td>
            <td colspan="2" rowspan="2">
                <img src="my-image.jpg" alt="Center Image">
            </td>
            <td>6</td>
        </tr>
        <tr>
            <td>7</td>
            <td>8</td>
        </tr>
        <tr>
            <td>9</td>
            <td>10</td>
            <td>11</td>
            <td>12</td>
        </tr>
    </table>

</body>
</html>
```

