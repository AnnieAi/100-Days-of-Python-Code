import pandas

data = pandas.read_csv("../weather_data.csv")

print(type(data))           # <class 'pandas.DataFrame'>
print(type(data["temp"]))   # <class 'pandas.Series'>

# The two primary data structures of pandas, Series (1-dimensional) and DataFrame (2-dimensional),
# handle the vast majority of typical use cases in finance, statistics, social science, and many areas of engineering.

data_dict = data.to_dict()              # dictionary对应DataFrame
print(data_dict)

temp_list = data["temp"].to_list()      # list对应Series
print(temp_list)
print(len(temp_list))