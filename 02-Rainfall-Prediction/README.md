# Rainfall Prediction 

## Introduction

[DEMO](https://rainfall-prediction-6wjd.onrender.com/)

Rainfall prediction is a crucial area of research in meteorology and agriculture. Accurate rainfall predictions aid in better planning and decision-making for activities such as crop cultivation, disaster management, and water resource management. This project utilizes AI and Machine Learning (ML) techniques to develop a precise and reliable rainfall prediction model using historical weather data.


## Project Overview

This project explores the use of AI/ML techniques in rainfall prediction by analyzing historical weather data from Australia. The primary objective is to create a model that can predict whether it will rain the next day (RainTomorrow) based on various weather parameters.

## Features

- **Increased Accuracy**: AI/ML models extract complex patterns and trends not apparent with traditional methods, leading to more accurate predictions.
- **Timely Forecasting**: AI/ML models process large datasets quickly, enabling timely rainfall forecasts.
- **Scalability**: The models can handle large datasets, making them scalable for different regions and time periods.
- **Cost-Effective**: The models require minimal physical infrastructure and can be implemented using cloud-based services.
- ![Page_Home](https://github.com/Rutiktorambe/Rainfall-Prediction/assets/114429614/e6c71ca2-5ee9-497c-8586-e4ee4c36bc9c)


## Screenshots
### HomePage
![Page_Home](https://github.com/Rutiktorambe/Rainfall-Prediction/assets/114429614/e6c71ca2-5ee9-497c-8586-e4ee4c36bc9c)

### InputPage
![Page_2](https://github.com/Rutiktorambe/Rainfall-Prediction/assets/114429614/ace44663-1166-4c7b-9292-c6cc9ae8d424)

### ResultPage
- Rainly  
![Page_Rainly](https://github.com/Rutiktorambe/Rainfall-Prediction/assets/114429614/4ce8453a-1289-465d-98ec-42c758632059)
- Sunny
![Screenshot 2024-06-03 091915](https://github.com/Rutiktorambe/Rainfall-Prediction/assets/114429614/ced83a06-b965-4182-bd93-a857835091e5)


## Dataset

The dataset used is the "Weather in Australia" dataset from Kaggle, which includes historical weather data from 2007 to 2017. The dataset comprises 1,45,460 records with 24 features.
- Dataset: [Weather in Australia](https://www.kaggle.com/datasets/gauravduttakiit/weather-in-aus)
  
**Key Features:**

- Date
- Location
- MinTemp
- MaxTemp
- Rainfall
- Evaporation
- Sunshine
- WindGustDir
- WindGustSpeed
- WindDir9am
- WindDir3pm
- WindSpeed9am
- WindSpeed3pm
- Humidity9am
- Humidity3pm
- Pressure9am
- Pressure3pm
- Cloud9am
- Cloud3pm
- Temp9am
- Temp3pm
- RainToday
- RainTomorrow (target variable)
- Dataset (train/test indicator)

## Model Creation

1. **Data Cleaning and Preprocessing**:
   - Handle missing values using random sample imputation.
   - Visualize data for outliers and distributions.
   - Encode target labels and normalize data.
   - Plot correlation heatmap.
   - Remove outliers and analyze data for the best fit line.

2. **Data Splitting**:
   - Split data into training and testing sets using `sklearn`'s `train_test_split`.

3. **Model Training**:
   - Use SMOTE for balanced data.
   - Select CatBoost classifier for its high accuracy (85.63%).
   - Evaluate model using accuracy score, confusion matrix, classification report, and ROC AUC score.

4. **Model Saving and Deployment**:
   - Save the model using `joblib`.
   - Deploy the model using Flask on Render.

## Results

| Rank | Classifier                     | Accuracy | Precision | Recall | ROC AUC Score |
|------|--------------------------------|----------|-----------|--------|---------------|
| 1    | Cat-Boost Classifier           | 0.8563   | 0.7596    | 0.5252 | 0.7386        |
| 2    | Bagging Classifier             | 0.8540   | 0.7587    | 0.5111 | 0.7321        |
| 3    | Random Forest Classifier       | 0.8537   | 0.7704    | 0.4950 | 0.7262        |
| 4    | K-Neighbors Classifier         | 0.8399   | 0.7089    | 0.4850 | 0.7137        |
| 5    | Ada Boost Classifier           | 0.8381   | 0.7152    | 0.4614 | 0.7042        |
| 6    | Linear Discriminant Analysis   | 0.8366   | 0.6904    | 0.4916 | 0.7140        |
| 7    | Logistic Regression Classifier | 0.8344   | 0.7017    | 0.4542 | 0.6992        |
| 8    | Decision Tree Classifier       | 0.8263   | 0.7304    | 0.3568 | 0.6594        |



## CatBoost Classifier

CatBoost is a supervised ML method using decision trees for classification and regression, particularly effective with categorical data and gradient boosting. The process includes:

1. **Data Preprocessing**: Feature selection, data cleaning, and normalization.
2. **Initialization**: Starts with a single decision tree predicting the mean target value.
3. **Gradient Boosting**: Trains multiple decision trees sequentially, correcting previous errors.
4. **Tree Generation**: Selects best split points by minimizing the loss function.
5. **Shrinkage**: Reduces the weight of new trees to prevent overfitting.
6. **Prediction**: Uses the majority vote of decision trees for final prediction.

## Deployment

The model is deployed using Flask on Render.
- Demo: [Predict Weather](https://rainfall-prediction-6wjd.onrender.com/)
## Usage

To use this project:

1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/rainfall-prediction.git
   cd rainfall-prediction

2. **Install dependencies:**:
   ```sh
   pip install -r requirements.txt

3. **Run the Flask app**:
   ```sh
   python app.py

4. **Access the web app**:
   ```sh
   Open your web browser and go to http://localhost:5000

## Contributors
- Contributions are welcome! Please open an issue or submit a pull request for any changes.
