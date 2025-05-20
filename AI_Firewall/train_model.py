import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
data = pd.read_csv("dataset.csv")

# Features and label
X = data[['src_port', 'dst_port', 'packet_size']]
y = data['label']

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save the model
joblib.dump(model, "model.pkl")

print("Model trained and saved as model.pkl")
