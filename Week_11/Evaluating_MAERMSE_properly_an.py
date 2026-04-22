import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.datasets import load_diabetes

def main():
    print("--- Loading and Splitting Dataset ---")
    data = load_diabetes(as_frame=True)
    df = data.frame
    
    X = df.drop(columns=['target'])
    y = df['target']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 1. Initialize and train the Linear Regression model
    print("\n--- Training Model ---")
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # 2. Predict on test set
    y_pred = model.predict(X_test)
    
    # 3. Evaluate Performance (MAE and RMSE)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    
    print("\n--- Regression Performance Metrics ---")
    print(f"Mean Absolute Error (MAE): {mae:.2f}")
    print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
    
    # 4. Visualize Actual vs Predicted
    plt.figure(figsize=(8, 6))
    plt.scatter(y_test, y_pred, color='blue', alpha=0.6, label='Predictions')
    
    # Perfect prediction line (y=x)
    max_val = max(np.max(y_test), np.max(y_pred))
    min_val = min(np.min(y_test), np.min(y_pred))
    plt.plot([min_val, max_val], [min_val, max_val], color='red', linestyle='--', lw=2, label='Perfect Fit')
    
    plt.title('Actual vs Predicted Values (Linear Regression)')
    plt.xlabel('Actual Target Values')
    plt.ylabel('Predicted Target Values')
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.7)
    
    plt.savefig('actual_vs_predicted.png', dpi=300)
    plt.close()
    
    print("\nPlot saved successfully as 'actual_vs_predicted.png'.")

if __name__ == "__main__":
    main()
