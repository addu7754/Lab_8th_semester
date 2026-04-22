# Question 3: Splitting Datasets for Training and Testing

**Problem Statement:** 
Read a dataset and split a dataset into training and testing sets.


```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_diabetes

def main():
    print("--- Loading Dataset ---")
    data = load_diabetes(as_frame=True)
    df = data.frame
    
    print(f"Original dataset shape: {df.shape}")
    
    # Define features (X) and target (y)
    X = df.drop(columns=['target'])
    y = df['target']
    
    # Split the dataset into training (80%) and testing (20%) sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("\n--- Data Splitting Results ---")
    print(f"Training features (X_train) shape: {X_train.shape}")
    print(f"Testing features (X_test) shape: {X_test.shape}")
    print(f"Training target (y_train) shape: {y_train.shape}")
    print(f"Testing target (y_test) shape: {y_test.shape}")

if __name__ == "__main__":
    main()
```

**Output:**

```sh
--- Loading Dataset ---
Original dataset shape: (442, 11)

--- Data Splitting Results ---
Training features (X_train) shape: (353, 10)
Testing features (X_test) shape: (89, 10)
Training target (y_train) shape: (353,)
Testing target (y_test) shape: (89,)
```


