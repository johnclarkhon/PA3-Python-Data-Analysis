import pandas as pd

# use pd.read_csv("file") to load the CSV file into a DataFrame
cars = pd.read_csv("cars.csv")
cars

# use .head() to display the first five rows
cars.head()

# use .tail() to display the last five rows
cars.tail()