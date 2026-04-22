import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def handle_outliers():
    print("--- 1. Generating Data ---")
    np.random.seed(10)
    data = np.random.normal(50, 10, 200).tolist()
    data.extend([150, 160, -20, -30]) # Inject outliers intentionally
    df = pd.DataFrame({'Value': data})

    # Plot original boxplot
    plt.figure(figsize=(8, 4))
    sns.boxplot(x=df['Value'])
    plt.title('Boxplot Before Removing Outliers')
    plt.savefig('boxplot_before.png')

    print("\n--- 2. Identifying Outliers (IQR Method) ---")
    Q1 = df['Value'].quantile(0.25)
    Q3 = df['Value'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = df[(df['Value'] < lower_bound) | (df['Value'] > upper_bound)]
    print(f"Number of outliers detected: {len(outliers)}")
    print(outliers)

    print("\n--- 3. Removing Outliers ---")
    df_clean = df[(df['Value'] >= lower_bound) & (df['Value'] <= upper_bound)]
    print(f"Cleaned dataset shape: {df_clean.shape}")

    # Plot cleaned boxplot
    plt.figure(figsize=(8, 4))
    sns.boxplot(x=df_clean['Value'])
    plt.title('Boxplot After Removing Outliers')
    plt.savefig('boxplot_after.png')

if __name__ == "__main__":
    handle_outliers()
