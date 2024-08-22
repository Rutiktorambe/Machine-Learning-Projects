from flask import Flask, request, jsonify, render_template
import pickle
import json
import numpy as np

# Load the model
with open('server/model/final_model.pickle', 'rb') as f:
    model = pickle.load(f)

# Load column names
with open('server/model/columns.json', 'r') as f:
    columns = json.load(f)
data_columns = columns['data_columns']

# Extract location list from data_columns
locations = [col for col in data_columns if col not in ['total_sqft', 'bath', 'bhk']]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', locations=locations)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        
        # Extract data
        location = data.get('location')
        sqft = data.get('sqft')
        bath = data.get('bath')
        bhk = data.get('bhk')

        # Validate input
        if not all([location, sqft, bath, bhk]):
            return jsonify({'error': 'Missing data in request'}), 400
        
        # Check location
        loc_index = np.where(np.array(data_columns) == location.lower())[0]
        if len(loc_index) == 0:
            return jsonify({'error': f"Location '{location}' not found in the columns"}), 400
        
        loc_index = loc_index[0]

        # Create input vector
        x = np.zeros(len(data_columns))
        x[data_columns.index('total_sqft')] = float(sqft)
        x[data_columns.index('bath')] = float(bath)
        x[data_columns.index('bhk')] = float(bhk)
        x[loc_index] = 1

        # Predict
        prediction = model.predict([x])[0]

        # Round the prediction to 2 decimal places and format with "Lakhs"
        rounded_prediction = round(prediction, 2)
        formatted_prediction = f"{rounded_prediction} Lakhs"

        return jsonify({'price': formatted_prediction})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False)  # Change to True for debugging or False for production
