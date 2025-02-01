import joblib
import pandas as pd

# Load the trained model
model = joblib.load('heart_disease_model.pkl')

# Correct column names for new data (ensure it matches training data)
new_data = pd.DataFrame([[60, 0, 2, 120]], columns=['age', 'sex ', 'chest pain type', 'max heart rate'])

# Make prediction
prediction = model.predict(new_data)

# Display result
print(f"Predicted heart disease: {'Yes' if prediction[0] == 1 else 'No'}")
