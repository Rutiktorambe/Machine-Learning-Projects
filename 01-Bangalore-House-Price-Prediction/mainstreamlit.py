import streamlit as st
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

# Streamlit app
st.title('House Price Prediction')

# Create input fields for user data
location = st.selectbox('Select Location', locations)
sqft = st.number_input('Total Square Feet', min_value=0.0, step=0.1)
bath = st.number_input('Number of Bathrooms', min_value=0, step=1)
bhk = st.number_input('Number of BHK', min_value=0, step=1)

# Predict button
if st.button('Predict'):
    try:
        # Check location
        loc_index = np.where(np.array(data_columns) == location.lower())[0]
        if len(loc_index) == 0:
            st.error(f"Location '{location}' not found in the columns")
        else:
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

            st.success(f'Predicted Price: {formatted_prediction}')
    except Exception as e:
        st.error(f'An error occurred: {str(e)}')
