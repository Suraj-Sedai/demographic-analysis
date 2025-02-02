import os
import pandas as pd
import numpy as np

class DataAnalyzer:
    def __init__(self, data_path):
        self.data_path = data_path

    def load_data(self):
        if not os.path.exists(self.data_path):
            raise FileNotFoundError(f"Error: The file '{self.data_path}' does not exist. Please run generate_data.py first.")
        return pd.read_csv(self.data_path)

    def analyze_income(self):
        df = self.load_data()
        average_income = df['Income'].mean()
        max_income = df['Income'].max()
        min_income = df['Income'].min()
        return average_income, max_income, min_income
    
    def analyze_occupation(self):
        df = self.load_data()
        occupation_counts = df['Occupation'].value_counts()
        return occupation_counts
    
    def analyze_location(self):
        df = self.load_data()
        location_counts = df['Location'].value_counts()
        return location_counts
    
    def analyze_education_level(self):
        df = self.load_data()
        education_level_counts = df['Education Level'].value_counts()
        return education_level_counts
    
    def analyze_age_group(self):
        df = self.load_data()
        age_group_counts = df['Age Group'].value_counts().sort_index()
        return age_group_counts
    

if __name__ == '__main__':
    # Get the absolute path of the data folder
    script_dir = os.path.dirname(__file__)  # Get current script directory
    data_path = os.path.join(script_dir, '../data/sample_data.csv')  # Construct absolute path

    # Create an instance of DataAnalyzer
    analyzer = DataAnalyzer(data_path)
    
    # Load data
    data = analyzer.load_data()

    # Analyze income
    average_income, max_income, min_income = analyzer.analyze_income()
    print(f"Average Income: {average_income}")
    print(f"Maximum Income: {max_income}")
    print(f"Minimum Income: {min_income}")
    print(f"\nOccupation Counts:\n{analyzer.analyze_occupation()}")
    print(f"\nLocation Counts:\n{analyzer.analyze_location()}")
    print(f"\nEducation Level Counts:\n{analyzer.analyze_education_level()}")
    print(f"\nAge Group Counts:\n{analyzer.analyze_age_group()}")
