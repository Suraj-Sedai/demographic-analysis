import os
import pandas as pd
import numpy as np

class DataGenerator:
    def __init__(self, num_records=50, seed=42):
        np.random.seed(seed)
        self.num_records = num_records
        self.data_dir = os.path.join(os.path.dirname(__file__), '../data')
        os.makedirs(self.data_dir, exist_ok=True)  # Ensure the 'data' directory exists

    def generate_data(self):

        # Generate unique IDs from 1 to 50
        ids = np.arange(1, self.num_records + 1)

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

        age_groups = [self.classify_age_group(a) for a in age]

        # Create DataFrame
        data = pd.DataFrame({
            'Id': ids,
            'Gender': gender,
            'Age': age,
            'Age Group': age_groups,
            'Income': income,
            'Occupation': occupations,
            'Location': locations,
            'Education Level': education_levels
        })
        return data


    @staticmethod
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


    def save_data(self, df, filename='sample_data.csv'):
        csv_path = os.path.join(self.data_dir, filename)
        df.to_csv(csv_path, index=False)
        print(f"Data has been saved to '{csv_path}'.")
        print(df.head(30))  # Show first 5 rows

if __name__ == "__main__":
    generator = DataGenerator()
    data = generator.generate_data()
    generator.save_data(data)

