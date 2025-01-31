import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

#generate unique Ids from 1 to 50
ids = np.arange(1,51)

#generate random gender values
gender = np.random.choice(['Male','Female'],50)

#generate realistic random age values
age = np.random.randint(18,65,50)

#generate dataframes
df = pd.DataFrame({'Id':ids,'Gender': gender, 'Age':age})

print(df.head())