# Salary Prediction of Newly Hired Employees

## Introduction

[DEMO](https://salary-prediction-6dgr.onrender.com/)

This repository contains a machine learning model for predicting salary/CTC (Cost to Company) of newly hired employees based on various features. The dataset includes information about previous job roles, previous CTC, graduation marks, and more. The project includes data preprocessing, exploratory data analysis, and training of multiple machine learning models to identify the best performing model.

##  Problem Statement:
Create a machine learning model which will help the company in determining the salary of newly hired employees using the given data.


## Project Overview

This project explores the use of AI/ML techniques in salary/CTC (Cost to Company) of newly hired employees prediction by analyzing historical employees data from TechWorks Consulting . The primary objective is to create a model that can predict salary/CTC (Cost to Company) of newly hired employees.How much will salary pays to newly hired employees based on various employees data parameters.

## Features

- **Increased Accuracy**: AI/ML models extract complex patterns and trends not apparent with traditional methods, leading to more accurate predictions.
- **Timely Predicting**: AI/ML models process large datasets quickly, enabling timely Salary Prediction for the newly hired employees.
- **Scalability**: The models can handle large datasets, making them scalable for different regions and time periods.
- **Cost-Effective**: The models require minimal physical infrastructure and can be implemented using cloud-based services.



## Dataset
You are given employee data (here)as well as various other features that can be responsible for determining the employee's salary, such as the college an employee attends or the city from which the employee is coming, what the employee's previous CTC was, how much experience that employee has, and his academic record.
- The data contains 8 columns:
 - College name: Colleges belong to three groups Tier1,Tier2 and Tier3 where tier1 college has the highest weightage.
 - City:It has 2 types of cities: metro and non metro cities convert this categorical data into numerical data such that 0 goes for non metro and 1 for metro cities.
 - Role: Manager and Executive
 - Other columns Like: Previous CTC,Previous Job Change,Graduation marks, Experience in Months and CTC.
  
**Key Features:**

- College	City
- Role
- Previous CTC
- Previous job change	
- Graduation Marks	
- EXP (Month)	
- CTC(target variable)
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
   - Select Random Forest Regresssor for its high R-Squared Value (0.6594).
   - Evaluate model using R-Squared Error,Mean Squared Error.

4. **Model Saving and Deployment**:
   - Save the model using `pickel`.
   - Deploy the model using Flask on Render.

## Results

| Model                        | R-Squared Error | Mean Squared Error  |
|------------------------------|-----------------|---------------------|
| Random Forest Regression     | 0.6594          | 50,540,240.22       |
| XGBoost Regressor            | 0.6263          | 55,454,902.69       |
| Gradient Boosting Regression | 0.6193          | 56,493,762.01       |
| Decision Tree Regression     | 0.5928          | 60,424,631.03       |
| AdaBoost Regressor           | 0.5988          | 59,528,805.33       |
| Linear Regression            | 0.5367          | 68,751,323.93       |
| Ridge Regression             | 0.5366          | 68,768,563.69       |
| Lasso Regression             | 0.5367          | 68,750,405.10       |



## Deployment

The model is deployed using Flask on Render.
- Demo: [Predict Salary](https://salary-prediction-6dgr.onrender.com/)
## Usage

To use this project:

1. **Clone the repository**:
   ```sh
   git clone https://github.com/rutiktorambe/salary-prediction.git
   cd salary-prediction

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
- Rutik Jayram Torambe
- Contributions are welcome! Please open an issue or submit a pull request for any changes.


## Screenshots

### Index Page
![Screenshot 2024-06-03 090914](https://github.com/Rutiktorambe/Salary-Prediction/assets/114429614/cffccf15-45e7-49d2-bd96-db9f8fb98136)

### Result Page
![Screenshot 2024-06-03 101051](https://github.com/Rutiktorambe/Salary-Prediction/assets/114429614/829b8225-af20-4497-aad5-b733036d47c2)



