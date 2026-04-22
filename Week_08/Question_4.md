# Question 4: Filtering Data Based on Conditions

**Problem Statement:** 
Filter rows and columns based on specific conditions (such as remove rows with missing values, if value is less than 50 etc.).


```python
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
```

**Output:**

```sh
Original DataFrame:
       A   B     C
0  85.0  75  70.0
1  45.0  55  85.0
2   NaN  60  40.0
3  90.0  95   NaN
4  60.0  20  99.0

DataFrame after removing missing values:
       A   B     C
0  85.0  75  70.0
1  45.0  55  85.0
4  60.0  20  99.0

DataFrame applying condition (A >= 50):
       A   B     C
0  85.0  75  70.0
4  60.0  20  99.0
```



\section{Problems based on HTML and JavaScript}

