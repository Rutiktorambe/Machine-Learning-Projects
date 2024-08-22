from flask import Flask, render_template, request
import joblib

app = Flask(__name__, template_folder='template')

# Load the trained model
model = joblib.load('RF_regression.pkl')

def AQI_Range(x):
    if x <= 50:
        return "Good"
    elif 50 < x <= 100:
        return "Moderate"
    elif 100 < x <= 200:
        return "Poor"
    elif 200 < x <= 300:
        return "Unhealthy"
    elif 300 < x <= 400:
        return "Very Unhealthy"
    elif x > 400:
        return "Hazardous"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        so2 = float(request.form['so2'])
        no2 = float(request.form['no2'])
        rspm = float(request.form['rspm'])
        spm = float(request.form['spm'])

        predicted_aqi = model.predict([[so2, no2, rspm, spm]])
        aqi_range = AQI_Range(predicted_aqi[0])

        return render_template('result.html', predicted_aqi=predicted_aqi[0], aqi_range=aqi_range)

if __name__ == '__main__':
    app.run(debug=True)
