import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Set seed for reproducibility
np.random.seed()

#generate unique Ids from 1 to 50
ids = np.arange(1,51)

#generate random gender values
gender = np.random.choice(['Male','Female'],50)

#generate realistic random age values
age = np.random.randint(18,65,50)

#generate dataframes
df = pd.DataFrame({'Id':ids,'Gender': gender, 'Age':age})


# Count occurrences of each gender
gender_counts = df['Gender'].value_counts()

# Create a pie chart
plt.figure(figsize=(6, 6))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140, colors=['lightblue', 'pink'])
plt.title('Gender Distribution')


# Show the pie chart
plt.show()
print(df.head())

