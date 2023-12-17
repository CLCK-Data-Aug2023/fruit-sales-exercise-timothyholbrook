import pandas as pd

# Create a list
data = [
    {'Apples': 35, 'Bananas': 21},
    {'Apples': 41, 'Bananas': 34}
]

# Create a pandas dataframe
df = pd.DataFrame(data, index=['2017 Sales', '2018 Sales'])

# Write to CSV file named fruit.csv
df.to_csv('fruit.csv')

# Display
print(df)
