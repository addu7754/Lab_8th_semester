import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_wine

def main():
    print("--- Loading Wine Dataset for Model Comparison ---")
    data = load_wine()
    X = pd.DataFrame(data.data, columns=data.feature_names)
    y = data.target

    # Splitting data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Initialize a dictionary holding different classification models
    models = {
        "Logistic Regression": LogisticRegression(max_iter=10000),
        "Decision Tree": DecisionTreeClassifier(random_state=42),
        "Random Forest": RandomForestClassifier(random_state=42),
        "Support Vector Machine": SVC()
    }

    print("\n--- Model Comparison on Test Set ---")
    # Iterate through models to train and evaluate
    for name, model in models.items():
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        acc = accuracy_score(y_test, predictions)
        print(f"{name.ljust(25)} : Accuracy = {acc:.4f}")

if __name__ == "__main__":
    main()
