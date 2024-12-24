# Pandas Tutorial - Notes and Examples

# Import Pandas
import pandas as pd

# --- Pandas HOME ---
# Pandas is a powerful library used for data manipulation and analysis in Python.
# It provides data structures such as Series and DataFrame that allow for efficient handling of data.

# --- Pandas Intro ---
# Pandas is built on top of NumPy and is primarily used for working with structured data.
# The two main data structures in Pandas are:
# - Series (1-dimensional)
# - DataFrame (2-dimensional)

# --- Pandas Getting Started ---
# You can install Pandas using pip if it is not installed yet:
# pip install pandas

# --- Pandas Series ---
# A Pandas Series is a 1-dimensional labeled array capable of holding any data type.

# Example: Creating a Pandas Series
data = [1, 2, 3, 4, 5]
series = pd.Series(data)
print("Series:\n", series)

# Example: Creating a Series with custom index
index = ['a', 'b', 'c', 'd', 'e']
series_with_index = pd.Series(data, index=index)
print("Series with custom index:\n", series_with_index)

# --- Pandas DataFrames ---
# A DataFrame is a 2-dimensional labeled data structure, similar to a table or spreadsheet.

# Example: Creating a Pandas DataFrame from a dictionary
data_dict = {'Name': ['Alice', 'Bob', 'Charlie'],
             'Age': [25, 30, 35],
             'City': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data_dict)
print("DataFrame:\n", df)

# --- Pandas Read CSV ---
# You can read data from CSV files using pd.read_csv().

# Example: Reading a CSV file
df_csv = pd.read_csv('data.csv')  # Replace 'data.csv' with the actual file path
print("Data from CSV:\n", df_csv)

# --- Pandas Read JSON ---
# You can read data from JSON files using pd.read_json().

# Example: Reading a JSON file
df_json = pd.read_json('data.json')  # Replace 'data.json' with the actual file path
print("Data from JSON:\n", df_json)

# --- Pandas Analyzing Data ---
# Pandas provides several functions to analyze data, such as basic statistics and summary information.

# Example: Getting summary statistics
print("Summary Statistics:\n", df.describe())  # Summary stats like count, mean, std, etc.

# Example: Checking data types
print("Data Types:\n", df.dtypes)

# Example: Checking for missing values
print("Missing Values:\n", df.isnull().sum())

# --- Cleaning Data ---
# Cleaning data is an essential step in any data analysis workflow.
# It involves handling missing values, correcting data formats, and removing unwanted data.

# --- Cleaning Empty Cells ---
# You can handle empty (NaN) cells using methods like dropna() and fillna().

# Example: Dropping rows with any NaN values
df_cleaned = df.dropna()  # Removes rows with any missing values
print("Data without missing values:\n", df_cleaned)

# Example: Filling NaN values with a specific value
df_filled = df.fillna(0)  # Replace NaN with 0
print("Data with NaN replaced by 0:\n", df_filled)

# --- Cleaning Wrong Format ---
# Sometimes data is in the wrong format (e.g., dates in string format). Pandas provides functions to handle this.

# Example: Converting a column to a datetime format
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')  # Convert 'Date' column to datetime
print("Data with Date in correct format:\n", df)

# --- Cleaning Wrong Data ---
# You can clean data by replacing incorrect values or filtering out unwanted rows.

# Example: Replacing incorrect values in a column
df['Age'] = df['Age'].replace(0, 30)  # Replace all 0 values in 'Age' with 30
print("Data after replacing wrong values:\n", df)

# --- Removing Duplicates ---
# You can remove duplicate rows using the drop_duplicates() function.

# Example: Dropping duplicate rows
df_no_duplicates = df.drop_duplicates()  # Removes duplicate rows
print("Data without duplicates:\n", df_no_duplicates)

# --- Correlations ---
# Pandas makes it easy to compute the correlation between numerical columns in a DataFrame.

# Example: Calculating correlations between columns
correlations = df.corr()  # Compute pairwise correlations between numeric columns
print("Correlations:\n", correlations)

# --- Pandas Correlations ---
# The corr() method calculates the Pearson correlation coefficient between columns. It returns values between -1 and 1, where:
# - 1 indicates a perfect positive correlation
# - -1 indicates a perfect negative correlation
# - 0 indicates no correlation.

# Example: Viewing correlations in a dataset
df_numeric = df[['Age', 'Salary']]  # Assuming these columns are numerical
correlation_matrix = df_numeric.corr()  # Calculate correlation
print("Correlation Matrix:\n", correlation_matrix)
