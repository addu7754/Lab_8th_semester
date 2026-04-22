import pandas as pd
import numpy as np

def main():
    # Create a sample DataFrame with missing values and various numbers
    data = {
        'A': [85, 45, np.nan, 90, 60],
        'B': [75, 55, 60, 95, 20],
        'C': [70, 85, 40, np.nan, 99]
    }
    df = pd.DataFrame(data)

    print("Original DataFrame:\n", df)

    # 1. Remove rows with any missing values
    df_no_missing = df.dropna()
    print("\nDataFrame after removing missing values:\n", df_no_missing)

    # 2. Filter rows where value in column 'A' is greater than or equal to 50
    df_filtered = df_no_missing[df_no_missing['A'] >= 50]
    print("\nDataFrame applying condition (A >= 50):\n", df_filtered)

if __name__ == "__main__":
    main()
