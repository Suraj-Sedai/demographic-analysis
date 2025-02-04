from rest_framework.response import Response
from rest_framework.decorators import api_view
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
import base64

DATA_PATH = os.path.join(os.path.dirname(__file__), '../../data/sample_data.csv')

# Data Generator
@api_view(['GET'])
def generate_data(request):
    np.random.seed(42)
    ids = np.arange(1, 51)
    gender = np.random.choice(['Male', 'Female'], 50)
    age = np.random.randint(18, 65, 50)
    income = np.random.randint(20000, 120001, 50)
    occupations = np.random.choice(['Engineer', 'Doctor', 'Teacher', 'Student', 'Manager', 'Freelancer'], 50)
    locations = np.random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami'], 50)
    education_levels = np.random.choice(['High School', "Bachelor's", "Master's", 'PhD'], 50)

    data = pd.DataFrame({
        'Id': ids,
        'Gender': gender,
        'Age': age,
        'Income': income,
        'Occupation': occupations,
        'Location': locations,
        'Education Level': education_levels
    })

    data.to_csv(DATA_PATH, index=False)
    return Response({"message": "Data generated successfully!"})

# Data Analyzer
@api_view(['GET'])
def analyze_data(request):
    if not os.path.exists(DATA_PATH):
        return Response({"error": "Data file not found. Please generate data first."})

    df = pd.read_csv(DATA_PATH)
    analysis = {
        "average_income": df['Income'].mean(),
        "max_income": df['Income'].max(),
        "min_income": df['Income'].min(),
        "occupation_counts": df['Occupation'].value_counts().to_dict(),
        "location_counts": df['Location'].value_counts().to_dict(),
        "education_counts": df['Education Level'].value_counts().to_dict(),
        "gender_counts": df['Gender'].value_counts().to_dict()
    }
    return Response(analysis)

# Data Visualization
@api_view(['GET'])
def visualize_data(request):
    if not os.path.exists(DATA_PATH):
        return Response({"error": "Data file not found. Please generate data first."})

    df = pd.read_csv(DATA_PATH)
    gender_counts = df['Gender'].value_counts()

    plt.figure(figsize=(6, 6))
    plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%')
    plt.title('Gender Distribution')

    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    image_base64 = base64.b64encode(image_png).decode('utf-8')

    return Response({"image": image_base64})
