import os
import pandas as pd
import numpy as np

# Get the absolute path of the data folder
script_dir = os.path.dirname(__file__)  # Get current script directory
data_path = os.path.join(script_dir, '../data/enhanced_sample_data.csv')  # Construct absolute path

# Check if the CSV file exists
if not os.path.exists(data_path):
    raise FileNotFoundError(f"Error: The file '{data_path}' does not exist. Please run generate_data.py first.")

# Read the CSV file into a DataFrame
df = pd.read_csv(data_path)

average_income = df['Income'].mean()
print(f'Average Income: ${average_income:.2f}')

#calculate max income
max_income = df['Income'].max()
print(f'Max Income: ${max_income}')

#calculate min income
min_income = df['Income'].min()
print(f'Min Income: ${min_income}')
