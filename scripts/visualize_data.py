import os
import pandas as pd
import matplotlib.pyplot as plt

class DataVisualizer:
    def __init__(self, data_path):
        self.data_path = data_path

    def load_data(self):
        if not os.path.exists(self.data_path):
            raise FileNotFoundError(f"Error: The file '{self.data_path}' does not exist. Please run generate_data.py first.")
        return pd.read_csv(self.data_path)
    
    def pie_chart(self):
        df = self.load_data()
        # Count occurrences of each gender
        gender_counts = df['Gender'].value_counts()

        # Create a pie chart
        plt.figure(figsize=(6, 6))
        plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140, colors=['lightblue', 'pink'])
        plt.title('Gender Distribution')

        # Show the pie chart
        plt.show()

if __name__ == '__main__':
    # Get the absolute path of the data folder
    script_dir = os.path.dirname(__file__)  # Get current script directory
    data_path = os.path.join(script_dir, '../data/enhanced_sample_data.csv')  # Construct absolute path

    # Create an instance of DataVisualizer
    visualizer = DataVisualizer(data_path)

    # Load data
    data = visualizer.load_data()

    # Count occurrences
    visualizer.pie_chart()