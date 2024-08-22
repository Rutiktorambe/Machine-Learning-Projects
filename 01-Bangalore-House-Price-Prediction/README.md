# Bengaluru House Price Prediction

## Introduction

This project focuses on predicting house prices in Bengaluru using machine learning techniques. By analyzing various features such as area type, location, and total square footage, the model aims to provide accurate price predictions. The project uses several regression algorithms to evaluate and compare their performance.

## Dataset

The dataset used for this project includes the following features:

- **area_type**: Type of the area (e.g., Super Built-up Area, Built-up Area, etc.)
- **availability**: Availability status of the property (e.g., Ready To Move, Under Construction)
- **location**: Geographical location of the property
- **size**: Size of the property (e.g., 2 BHK, 3 BHK)
- **society**: Name of the society or community
- **total_sqft**: Total area of the property in square feet
- **bath**: Number of bathrooms
- **balcony**: Number of balconies
- **price**: Price of the property (target variable)

## Models and Evaluation

The following table summarizes the performance of each model:

| Model                     | R-squared Score | Mean Squared Error |
|---------------------------|-----------------|---------------------|
| XGBoost Regressor         | 0.8811          | 688.81              |
| Lasso Regression          | (value not provided) | (value not provided) |
| Linear Regression        | 0.8658          | 777.45              |
| Decision Tree Regression  | 0.7054          | 1706.62             |
| Random Forest Regression  | 0.8427          | 911.10              |
| Gradient Boosting Regression | 0.8869       | 655.41              |

## Model Implementation

1. **Data Preprocessing**:
   - Handle missing values.
   - Encode categorical variables.
   - Normalize or standardize numerical features if required.

2. **Model Training**:
   - Train models using the dataset.
   - Evaluate performance using R-squared Score and Mean Squared Error.

3. **Model Evaluation**:
   - Compare models based on their R-squared Scores and Mean Squared Errors to select the best performing model.

4. **Deployment**:
   - Deploy the model using a suitable framework (e.g., Flask, Django) for predictions in a real-time environment.

## Usage

To use this project:

1. **Clone the repository**:
   ```sh
   git clone https://github.com/Rutiktorambe/Bangalore-House-Price-Prediction.git
   cd Bangalore-House-Price-Prediction
   ```

2. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```

3. **Run the script for training and evaluation**:
   ```sh
   python app.py
   ```
   
## Contributors
Contributions are welcome! Please open an issue or submit a pull request for any changes or improvements.
