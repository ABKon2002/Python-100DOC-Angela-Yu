
import pandas as pd

data = pd.read_csv("D25 - CSV Data, Pandas Intro\\Data\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

print(data['Primary Fur Color'].value_counts().to_csv("D25 - CSV Data, Pandas Intro\\Data\\squirrel_count.csv"))
