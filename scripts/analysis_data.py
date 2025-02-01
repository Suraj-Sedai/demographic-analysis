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
    

if __name__ == '__main__':
    # Get the absolute path of the data folder
    script_dir = os.path.dirname(__file__)  # Get current script directory
    data_path = os.path.join(script_dir, '../data/enhanced_sample_data.csv')  # Construct absolute path

    # Create an instance of DataAnalyzer
    analyzer = DataAnalyzer(data_path)
    
    # Load data
    data = analyzer.load_data()

    # Analyze income
    average_income, max_income, min_income = analyzer.analyze_income()
    print(f"Average Income: {average_income}")
    print(f"Maximum Income: {max_income}")
    print(f"Minimum Income: {min_income}")
