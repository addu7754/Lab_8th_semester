# Question 3: Renaming Columns and Changing Data Types

**Problem Statement:** 
Rename columns of the datasets and change their data types.


```python
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
```

**Output:**

```sh
Original DataFrame:
    col1 col2
0     1    4
1     2    5
2     3    6

Original Data Types:
 col1     int64
col2    object
dtype: object

Modified DataFrame:
    ID  Score
0   1      4
1   2      5
2   3      6

Modified Data Types:
 ID       int64
Score    int64
dtype: object
```



