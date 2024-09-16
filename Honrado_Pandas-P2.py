import pandas as pd

# use pd.read_csv("file") to load the CSV file into a DataFrame
cars = pd.read_csv("cars.csv")
cars

# Using .iloc - m row, n column indexes
cars.iloc[:5, 1::2]

# using loc - m row index, column name
cars.loc[cars['Model'] == 'Mazda RX4']

# loc - m row index, column name
cars.loc[cars['Model'] == 'Camaro Z28', ['Model','cyl']]

# using .isin function to select data based on the list 
selected_cars = cars[cars['Model'].isin(['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic'])]
selected_cars[['Model', 'cyl', 'gear']]