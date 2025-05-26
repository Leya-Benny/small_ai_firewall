import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import matplotlib.pyplot as plt

def main():
    # Load the dataset
    try:
        data = pd.read_csv("dataset.csv")
    except FileNotFoundError:
        print("Error: dataset.csv not found.")
        return

    # Check if required columns exist
    required_columns = {"src_port", "dst_port", "packet_size", "label"}
    if not required_columns.issubset(data.columns):
        print("Error: Dataset must include columns: src_port, dst_port, packet_size, label")
        return

    # Separate features and labels
    X = data[["src_port", "dst_port", "packet_size"]]
    y = data["label"]

    # Split into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train Random Forest classifier
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model accuracy: {accuracy:.2f}")

    # Save the trained model
    joblib.dump(model, "model.pkl")
    print("Trained model saved as model.pkl")

    # Plot and save feature importance graph
    feature_importance = model.feature_importances_
    plt.bar(X.columns, feature_importance)
    plt.title("Feature Importance")
    plt.xlabel("Feature")
    plt.ylabel("Importance")
    plt.tight_layout()
    plt.savefig("feature_importance.png")
    print("Feature importance chart saved as feature_importance.png")

if __name__ == "__main__":
    main()



