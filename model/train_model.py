import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

import joblib


# Load dataset
data = pd.read_csv("dataset/symptoms.csv")


# Input features
X = data[
    [
        "fever",
        "cough",
        "headache",
        "fatigue"
    ]
]


# Target
y = data["disease"]


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create machine learning model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# Train model
model.fit(X_train, y_train)


# Test model
predictions = model.predict(X_test)


# Calculate accuracy
accuracy = accuracy_score(
    y_test,
    predictions
)


print("Model trained successfully!")
print("Accuracy:", accuracy)


# Save trained model
joblib.dump(
    model,
    "model/disease_model.pkl"
)


print("Model saved successfully!")
