
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle
import numpy as np

# Load the dataset
heart_disease = pd.read_csv('datasets/processed_heart_disease.csv')

# Clean the column names to remove any leading/trailing spaces
heart_disease.columns = heart_disease.columns.str.strip()

# Print columns to confirm
print("Dataset Columns:", heart_disease.columns)

# Handle missing values by filling with the median or remove rows
heart_disease = heart_disease.fillna(heart_disease.median())  # Fill missing values with median

# Check for infinite or extreme values
heart_disease.replace([np.inf, -np.inf], np.nan, inplace=True)  # Replace infinity with NaN
heart_disease = heart_disease.fillna(heart_disease.median())  # Fill NaN again

# Select relevant features and target
# Make sure you are using the same features as in the training phase
X = heart_disease[['age', 'sex', 'chest pain type', 'max heart rate']]  # Modify as needed
y = heart_disease['heart disease']  # Make sure this column exists in the dataset

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train a Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Predict and calculate accuracy
y_pred = model.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
print(f'Model Accuracy: {accuracy * 100:.2f}%')

# Save the model and scaler for later use
pickle.dump(model, open('heart_disease_model.pkl', 'wb'))
pickle.dump(scaler, open('scaler.pkl', 'wb'))
