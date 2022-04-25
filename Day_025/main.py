import pandas as pd

print("test")

data = pd.read_csv("weather_data.csv")

print(data["temp"])