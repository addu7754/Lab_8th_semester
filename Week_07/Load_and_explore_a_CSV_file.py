import pandas as pd

# Assuming 'data.csv' is present in the directory
df = pd.read_csv('data.csv')

print("--- First 5 rows (head) ---")
print(df.head())

print("\n--- Last 5 rows (tail) ---")
print(df.tail())

print("\n--- Dataset Info ---")
df.info()
