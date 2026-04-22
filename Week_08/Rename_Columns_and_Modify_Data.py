import pandas as pd

def main():
    # Create a sample DataFrame
    data = {'col1': [1, 2, 3], 'col2': ['4', '5', '6']}
    df = pd.DataFrame(data)

    print("Original DataFrame:\n", df)
    print("\nOriginal Data Types:\n", df.dtypes)

    # Rename columns
    df = df.rename(columns={'col1': 'ID', 'col2': 'Score'})

    # Change data type of 'Score' from object (string) to int
    df['Score'] = df['Score'].astype(int)

    print("\nModified DataFrame:\n", df)
    print("\nModified Data Types:\n", df.dtypes)

if __name__ == "__main__":
    main()
