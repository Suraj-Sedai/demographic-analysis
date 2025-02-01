import os
import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Generate unique IDs from 1 to 50
ids = np.arange(1, 51)

# Generate random gender values
gender = np.random.choice(['Male', 'Female'], 50)

# Generate realistic random age values
age = np.random.randint(18, 65, 50)

# Generate random income between 20,000 and 120,000
income = np.random.randint(20000, 120001, 50)

# Random occupations
occupations = np.random.choice(['Engineer', 'Doctor', 'Teacher', 'Student', 'Manager', 'Freelancer'], 50)

# Random locations
locations = np.random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami'], 50)

# Random education levels
education_levels = np.random.choice(['High School', "Bachelor's", "Master's", 'PhD'], 50)

# Age group classification
def classify_age_group(age):
    if 18 <= age <= 25:
        return '18-25'
    elif 26 <= age <= 35:
        return '26-35'
    elif 36 <= age <= 45:
        return '36-45'
    elif 46 <= age <= 55:
        return '46-55'
    else:
        return '56+'

age_groups = [classify_age_group(a) for a in age]

# Create DataFrame
df = pd.DataFrame({
    'Id': ids,
    'Gender': gender,
    'Age': age,
    'Age Group': age_groups,
    'Income': income,
    'Occupation': occupations,
    'Location': locations,
    'Education Level': education_levels
})

# Ensure the 'data' directory exists
data_dir = os.path.join(os.path.dirname(__file__), '../data')
os.makedirs(data_dir, exist_ok=True)  # Create directory if it doesn't exist

# Save data to CSV
csv_path = os.path.join(data_dir, 'enhanced_sample_data.csv')
df.to_csv(csv_path, index=False)

print(f"Enhanced data has been generated and saved to '{csv_path}'.")
print(df.head(30))  # Show first 5 rows
