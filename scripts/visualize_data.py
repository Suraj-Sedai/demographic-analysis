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
    
    def gender_chart(self):
        df = self.load_data()
        # Count occurrences of each gender
        gender_counts = df['Gender'].value_counts()

        # Create a pie chart
        plt.figure(figsize=(6, 6))
        plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140, colors=['lightblue', 'pink'])
        plt.title('Gender Distribution')

        # Show the pie chart
        plt.show()
    
    def age_chart(self):
        df = self.load_data()
        # Group by age group and count occurrences
        age_group_counts = df['Age Group'].value_counts().sort_index()

        # Create a bar chart
        plt.figure(figsize=(8, 6))
        plt.bar(age_group_counts.index, age_group_counts.values, color='skyblue')
        plt.xlabel('Age Group')
        plt.ylabel('Count')
        plt.title('Age Group Distribution')

        # Show the bar chart
        plt.show()

    def occupation_chart(self):
        df = self.load_data()
        # Count occurrences of each occupation
        occupation_counts = df['Occupation'].value_counts()

        # Create a horizontal bar chart
        plt.figure(figsize=(8, 6))
        plt.barh(occupation_counts.index, occupation_counts.values, color='lightcoral')
        plt.xlabel('Count')
        plt.ylabel('Occupation')
        plt.title('Occupation Distribution')

        # Show the horizontal bar chart
        plt.show()

    def location_chart(self):
        df = self.load_data()
        # Count occurrences of each location
        location_counts = df['Location'].value_counts()

        # Create a pie chart
        plt.figure(figsize=(6, 6))
        plt.pie(location_counts, labels=location_counts.index, autopct='%1.1f%%', startangle=140)
        plt.title('Location Distribution')

        # Show the pie chart
        plt.show()

if __name__ == '__main__':
    # Get the absolute path of the data folder
    script_dir = os.path.dirname(__file__)  # Get current script directory
    data_path = os.path.join(script_dir, '../data/sample_data.csv')  # Construct absolute path

    # Create an instance of DataVisualizer
    visualizer = DataVisualizer(data_path)

    # Load data
    data = visualizer.load_data()

    # Count occurrences
    visualizer.gender_chart()
    visualizer.age_chart()
    visualizer.occupation_chart()
    visualizer.location_chart()