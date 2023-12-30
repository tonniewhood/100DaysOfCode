# Anthony Wood
# 100 Days of Coding
# Day 25

import pandas

squirrels = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

num_gray = len(squirrels[squirrels["Primary Fur Color"] == "Gray"]["Primary Fur Color"])
num_cinnamon = len(squirrels[squirrels["Primary Fur Color"] == "Cinnamon"])
num_black = len(squirrels[squirrels["Primary Fur Color"] == "Black"])

colors_dict = {
    "Color": ["Gray", "Cinnamon", "Black"],
    "Count": [num_gray, num_cinnamon, num_black]
}

colors_data_frame = pandas.DataFrame(data=colors_dict)
colors_data_frame.to_csv("colors.csv")
