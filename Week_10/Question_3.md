# Question 3: Matplotlib Data Visualizations

**Problem Statement:** 
Read a dataset and create different line and bar plots using Matplotlib.


```python
import pandas as pd
import matplotlib.pyplot as plt

def create_plots():
    # 1. Create a sample dataset
    data = {
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        'Sales': [150, 200, 180, 220, 250, 230],
        'Expenses': [100, 120, 150, 170, 160, 190]
    }
    df = pd.DataFrame(data)
    print("Dataset loaded:\n", df)

    # 2. Create a Line Plot
    plt.figure(figsize=(10, 5))
    plt.plot(df['Month'], df['Sales'], marker='o', color='blue', label='Sales')
    plt.plot(df['Month'], df['Expenses'], marker='s', color='red', label='Expenses')
    plt.title('Monthly Sales vs Expenses (Line Plot)')
    plt.xlabel('Month')
    plt.ylabel('Amount ($)')
    plt.legend()
    plt.grid(True)
    plt.savefig('line_plot.png')
    plt.close()

    # 3. Create a Bar Plot
    plt.figure(figsize=(10, 5))
    x = range(len(df['Month']))
    width = 0.4

    plt.bar([i - width/2 for i in x], df['Sales'], width=width, color='skyblue', label='Sales')
    plt.bar([i + width/2 for i in x], df['Expenses'], width=width, color='salmon', label='Expenses')
    
    plt.xticks(x, df['Month'])
    plt.title('Monthly Sales vs Expenses (Bar Plot)')
    plt.xlabel('Month')
    plt.ylabel('Amount ($)')
    plt.legend()
    plt.savefig('bar_plot.png')
    plt.close()

if __name__ == "__main__":
    create_plots()
```

**Output:**

```sh
Dataset loaded:
   Month  Sales  Expenses
0   Jan    150       100
1   Feb    200       120
2   Mar    180       150
3   Apr    220       170
4   May    250       160
5   Jun    230       190
```



