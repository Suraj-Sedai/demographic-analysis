import os
import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed()

# Generate unique IDs from 1 to 50
ids = np.arange(1, 51)

# Generate random gender values
gender = np.random.choice(['Male', 'Female'], 50)

# Generate realistic random age values
age = np.random.randint(18, 65, 50)

# Create DataFrame
df = pd.DataFrame({'Id': ids, 'Gender': gender, 'Age': age})

# Ensure the 'data' directory exists
data_dir = os.path.join(os.path.dirname(__file__), '../data')
os.makedirs(data_dir, exist_ok=True)  # Create directory if it doesn't exist

# Save data to CSV
csv_path = os.path.join(data_dir, 'sample_data.csv')
df.to_csv(csv_path, index=False)

print(f"Data has been generated and saved to '{csv_path}'.")
print(df.head())  # Show first 5 rows
