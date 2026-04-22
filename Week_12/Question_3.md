# Question 3: Classification Performance and Confusion Matrix

**Problem Statement:** 
Generate and interpret a confusion matrix. Calculate accuracy, precision, recall, and F1-score and visualize classification results.


```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from sklearn.datasets import load_wine

def main():
    print("--- Loading Wine Dataset ---")
    data = load_wine()
    X = pd.DataFrame(data.data, columns=data.feature_names)
    y = data.target

    # Split dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    print("--- Training Logistic Regression Model ---")
    model = LogisticRegression(max_iter=10000)
    model.fit(X_train, y_train)

    # Predict on test set
    y_pred = model.predict(X_test)

    print("\n--- Classification Performance Metrics ---")
    print(f"Accuracy : {accuracy_score(y_test, y_pred):.4f}")
    print(f"Precision: {precision_score(y_test, y_pred, average='weighted'):.4f}")
    print(f"Recall   : {recall_score(y_test, y_pred, average='weighted'):.4f}")
    print(f"F1-Score : {f1_score(y_test, y_pred, average='weighted'):.4f}")

    print("\n--- Confusion Matrix ---")
    cm = confusion_matrix(y_test, y_pred)
    print(cm)
    
    print("\n--- Classification Report ---")
    print(classification_report(y_test, y_pred, target_names=data.target_names))

    # Visualize the confusion matrix
    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=data.target_names, yticklabels=data.target_names)
    plt.title('Confusion Matrix - Wine Dataset')
    plt.xlabel('Predicted Class')
    plt.ylabel('Actual Class')
    plt.tight_layout()
    plt.savefig('confusion_matrix_w12.png', dpi=300)
    plt.close()
    
    print("\nVisualization saved successfully as 'confusion_matrix_w12.png'.")

if __name__ == "__main__":
    main()
```

**Output:**

```sh
--- Loading Wine Dataset ---
--- Training Logistic Regression Model ---

--- Classification Performance Metrics ---
Accuracy : 1.0000
Precision: 1.0000
Recall   : 1.0000
F1-Score : 1.0000

--- Confusion Matrix ---
[[19  0  0]
 [ 0 21  0]
 [ 0  0 14]]

--- Classification Report ---
              precision    recall  f1-score   support

     class_0       1.00      1.00      1.00        19
     class_1       1.00      1.00      1.00        21
     class_2       1.00      1.00      1.00        14

    accuracy                           1.00        54
   macro avg       1.00      1.00      1.00        54
weighted avg       1.00      1.00      1.00        54

Visualization saved successfully as 'confusion_matrix_w12.png'.
```


