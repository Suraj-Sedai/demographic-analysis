import os
import pandas as pd
import matplotlib.pyplot as plt

# Get the absolute path of the data folder
script_dir = os.path.dirname(__file__)  # Get current script directory
data_path = os.path.join(script_dir, '../data/sample_data.csv')  # Construct absolute path

# Check if the CSV file exists
if not os.path.exists(data_path):
    raise FileNotFoundError(f"Error: The file '{data_path}' does not exist. Please run generate_data.py first.")

# Load dataset
df = pd.read_csv(data_path)

# Count occurrences of each gender
gender_counts = df['Gender'].value_counts()

# Create a pie chart
plt.figure(figsize=(6, 6))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140, colors=['lightblue', 'pink'])
plt.title('Gender Distribution')

# Show the pie chart
plt.show()
