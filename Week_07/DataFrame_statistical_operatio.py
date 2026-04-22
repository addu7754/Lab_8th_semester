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
