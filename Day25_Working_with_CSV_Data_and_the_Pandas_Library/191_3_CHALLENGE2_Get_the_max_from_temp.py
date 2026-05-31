import pandas

data = pandas.read_csv("../weather_data.csv")

temp_max = data["temp"].max()
print(temp_max)


print(data["condition"])    # 这样写更符合字典的对应，字典的直觉
print(data.condition)       # 之所以可以这么写，是因为pandas偷偷把heading转化成了这个data的attribute
