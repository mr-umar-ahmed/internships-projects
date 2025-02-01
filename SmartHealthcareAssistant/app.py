from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Collect input data from the form
    age = request.form.get('age')
    sex = request.form.get('sex')
    chest_pain = request.form.get('chest_pain')
    resting_bp = request.form.get('resting_bp')
    max_heart_rate = request.form.get('max_heart_rate')

    # For demonstration, mock a prediction result
    prediction = "High Risk of Disease" if int(age) > 50 else "Low Risk of Disease"

    return f"""
    <h1>Prediction Result</h1>
    <p>Based on the inputs:</p>
    <ul>
        <li>Age: {age}</li>
        <li>Sex: {sex}</li>
        <li>Chest Pain Type: {chest_pain}</li>
        <li>Resting Blood Pressure: {resting_bp}</li>
        <li>Max Heart Rate: {max_heart_rate}</li>
    </ul>
    <h2>Prediction: {prediction}</h2>
    <a href="/">Back to Form</a>
    """

if __name__ == '__main__':
    app.run(debug=True)
