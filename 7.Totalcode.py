Import Libraries & Load Dataset

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv("data.csv")

print(df.head())
print(df.isnull().sum())


# Handle missing values
df = df.fillna(df.median(numeric_only=True))

# Drop unnecessary columns (if any)
# df = df.drop(['column_name'], axis=1)


# Example Feature Engineering
# Create new features if required

# df['NewFeature'] = df['Feature1'] * df['Feature2']



# Convert categorical data to numerical
df = pd.get_dummies(df, drop_first=True)


# Split data
X = df.drop('target', axis=1)
Y = df['target']

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

# Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Model
model = LogisticRegression(max_iter=2000)



# Cross Validation
cv_scores = cross_val_score(model, X, Y, cv=5)

print("Cross Validation Accuracy:", cv_scores.mean())

# Train model
model.fit(X_train, Y_train)

# Predictions
Y_pred = model.predict(X_test)

# Evaluation
print("Accuracy:", accuracy_score(Y_test, Y_pred))
print("Confusion Matrix:\n", confusion_matrix(Y_test, Y_pred))
print("Classification Report:\n", classification_report(Y_test, Y_pred))
