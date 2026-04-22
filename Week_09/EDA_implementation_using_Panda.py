import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def perform_eda():
    # Load built-in seaborn dataset 'titanic'
    print("--- Loading Dataset (Titanic) ---")
    df = sns.load_dataset('titanic')

    print("\n--- 1. Summary Statistics ---")
    print(df.describe())

    print("\n--- 2. Dataset Info ---")
    print(df.info())

    print("\n--- 3. Missing Values Check ---")
    print(df.isnull().sum())

    print("\n--- 4. Correlation Matrix ---")
    # Select only numeric columns for correlation matrix
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    corr_matrix = numeric_df.corr()
    print(corr_matrix)

    # Plot heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Heatmap')
    plt.tight_layout()
    plt.savefig('correlation_heatmap.png')

if __name__ == "__main__":
    perform_eda()
