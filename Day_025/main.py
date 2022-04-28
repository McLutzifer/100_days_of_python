import pandas as pd

squirrel_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
black_squirrels = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
red_squirrels = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])

headings = ["Fur Color", "Count"]

squirrel_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels, black_squirrels, red_squirrels]
}

squirrel_count = pd.DataFrame(squirrel_dict)
squirrel_count.to_csv("squirrel_count.csv")
