# Question 4: Seaborn Relationships and Heatmaps

**Problem Statement:** 
Create scatter plots for feature relationships and generate a correlation heatmap.


```python
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
```

  **Output:**

```sh
--- Loading Dataset (Iris) ---

First 5 rows of Iris:
   sepal_length  sepal_width  petal_length  petal_width species
0           5.1          3.5           1.4          0.2  setosa
1           4.9          3.0           1.4          0.2  setosa
2           4.7          3.2           1.3          0.2  setosa
3           4.6          3.1           1.5          0.2  setosa
4           5.0          3.6           1.4          0.2  setosa

Correlation Matrix:
              sepal_length  sepal_width  petal_length  petal_width
sepal_length      1.000000    -0.117570      0.871754     0.817941
sepal_width      -0.117570     1.000000     -0.428440    -0.366126
petal_length      0.871754    -0.428440      1.000000     0.962865
petal_width       0.817941    -0.366126      0.962865     1.000000
\section{Problems based on HTML and JavaScript and CSS}

