import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import matplotlib.pyplot as plt

def main():
    # Load dataset
    data = pd.read_csv("dataset.csv")

    # Check for required columns
    expected_columns = {'src_port', 'dst_port', 'packet_size', 'label'}
    if not expected_columns.issubset(data.columns):
        print("Error: Dataset must contain src_port, dst_port, packet_size, and label columns.")
        return

    # Features and label
    X = data[['src_port', 'dst_port', 'packet_size']]
    y = data['label']

    # Split into train and test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model accuracy: {accuracy:.2f}")

    # Save the model
    joblib.dump(model, "model.pkl")
    print("Model saved as model.pkl")

    # Plot feature importance
    importance = model.feature_importances_
    plt.bar(X.columns, importance)
    plt.title("Feature Importance")
    plt.ylabel("Importance Score")
    plt.savefig("feature_importance.png")
    print("Feature importance saved as feature_importance.png")

if __name__ == "__main__":
    main()

