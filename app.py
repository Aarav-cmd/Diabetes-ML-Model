from flask import Flask, request, url_for, redirect, render_template
from joblib import load
import numpy as np

app = Flask(__name__)

# Load the model and scaler
model = load("FinalDiabetes_model.pkl")
scaler = load("finalscaler.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract features from form
        feature_names = ['pregnancies', 'glucose', 'bloodpressure', 'skinthickness', 'insulin', 'bmi', 'dpf', 'age']
        features = [request.form[name] for name in feature_names]
        features = np.array(features, dtype=float).reshape(1, -1)
        
        # Scale features
        scaled_features = scaler.transform(features)
        
        #This line will convert the dpf value from the form into a floating point number, preserving any decimals the user has entered.
        features = [float(request.form[name]) for name in feature_names]
        
        # Make prediction
        prediction = model.predict_proba(scaled_features)[0][1]
        
        # Format the prediction to two decimal places
        output = '{:.2f}'.format(prediction)
        
        # Determine the message based on the prediction
        if prediction > 0.5:
            message = f'Your chance of having diabetes is high: {output}'
        else:
            message = f'You are safe. Probability of having diabetes is: {output}'
    except KeyError as e:
        message = f"Error: Missing input for '{e.args[0]}'. Please fill out all the fields."

    return render_template('result.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)

