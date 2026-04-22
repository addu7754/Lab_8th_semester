# Question 3: Loading and Exploring CSV Datasets

**Problem Statement:** 
Load a CSV file and display the first five rows and display head, tail, and info of a dataset.


```python
import pandas as pd

# Assuming 'data.csv' is present in the directory
df = pd.read_csv('data.csv')

print("--- First 5 rows (head) ---")
print(df.head())

print("\n--- Last 5 rows (tail) ---")
print(df.tail())

print("\n--- Dataset Info ---")
df.info()
```


