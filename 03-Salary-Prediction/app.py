from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
model_path = 'Ml-Model/best_model.pkl'
with open(model_path, 'rb') as f:
    model = pickle.load(f)
    
if not hasattr(model, 'predict'):
    raise ValueError("Loaded object is not a model with a predict method")

@app.route('/')
def form():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    previous_ctc = float(request.form['previous_ctc'])
    previous_job_change = float(request.form['previous_job_change'])
    graduation_marks = float(request.form['graduation_marks'])
    exp_month = float(request.form['exp_month'])
    metro_city = int(request.form['metro_city'])
    role_manager = int(request.form['role_manager'])
    tier_2 = int(request.form['tier_2'])
    tier_3 = int(request.form['tier_3'])
    
    # Create feature array
    features = np.array([[previous_ctc, previous_job_change, graduation_marks, exp_month, metro_city, role_manager, tier_2, tier_3]])
    
    # Make prediction
    prediction = model.predict(features)[0]
    
    return render_template('result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
