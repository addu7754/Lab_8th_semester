import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def create_scatter_and_heatmap():
    # 1. Load built-in seaborn dataset 'iris'
    print("--- Loading Dataset (Iris) ---")
    df = sns.load_dataset('iris')
      print("\nFirst 5 rows of Iris:")
      print(df.head())

      # 2. Create a Scatter Plot for feature relationships
      plt.figure(figsize=(8, 6))
      sns.scatterplot(data=df, x='sepal_length', y='petal_length', hue='species', style='species', s=100)
      plt.title('Scatter Plot: Sepal Length vs Petal Length')
      plt.savefig('scatter_plot.png')
      plt.close()

      # 3. Generate a Correlation Heatmap
      # Extract only numeric columns for correlation computation
      numeric_df = df.select_dtypes(include=['float64', 'int64'])
      corr_matrix = numeric_df.corr()
      print("\nCorrelation Matrix:")
      print(corr_matrix)

      plt.figure(figsize=(8, 6))
      sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, linewidths=0.5)
      plt.title('Feature Correlation Heatmap')
      plt.tight_layout()
      plt.savefig('correlation_heatmap_w10.png')
      plt.close()

  if __name__ == "__main__":
      create_scatter_and_heatmap()
