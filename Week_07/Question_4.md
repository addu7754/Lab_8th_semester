# Question 4: DataFrame Operations

**Problem Statement:** 
Take a DataFrame and do the following:
    -  What is the average value of the second column?
    -  What is the average value of the first 5 rows of the third and fourth columns?
    -  Compute the row wise sum of all possible values in an array.
    -  Find the maximum of average value in each row.


```python
import pandas as pd
import numpy as np

# Create a sample DataFrame of 10 rows and 5 columns
np.random.seed(42)
df = pd.DataFrame(np.random.randint(1, 100, size=(10, 5)), columns=['A', 'B', 'C', 'D', 'E'])
print(f"Sample DataFrame:\n{df}\n")

# 1. Average value of the second column (Column 'B')
avg_second_col = df.iloc[:, 1].mean()
print(f"Average value of second column: {avg_second_col}")

# 2. Average value of the first 5 rows of the third and fourth columns (Cols 'C' and 'D')
avg_first_5_cols_3_4 = df.iloc[:5, 2:4].mean()
print(f"Average of first 5 rows of 3rd and 4th columns:\n{avg_first_5_cols_3_4}")

# 3. Compute row-wise sum
row_wise_sum = df.sum(axis=1)
print(f"\nRow-wise sum:\n{row_wise_sum}")

# 4. Find the maximum of average value in each row
max_avg_row = df.mean(axis=1).max()
print(f"\nMaximum average value in each row: {max_avg_row}")
```

**Output:**

```sh
Sample DataFrame:
    A   B   C   D   E
0  52  93  15  72  61
1  21  83  87  75  75
2  88  24   3  22  53
3   2  88  30  38   2
4  64  60  21  33  76
5  58  22  89  49  91
6  59  42  92  60  80
7  15  62  62  47  62
8  51  55  64   3  51
9   7  21  73  39  18

Average value of second column: 55.0
Average of first 5 rows of 3rd and 4th columns:
C    31.2
D    48.0
dtype: float64

Row-wise sum:
0    293
1    341
2    190
3    160
4    254
5    309
6    333
7    248
8    224
9    158
dtype: int64

Maximum average value in each row: 68.2
```



\section{Problems Based on HTML and JavaScript}

