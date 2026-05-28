import pandas

data = pandas.read_csv("../weather_data.csv")

#%% Read A Row

print(data[data.day == "Monday"])
print("\n")

#%% Read the Row with max temp value

# Below two ways are all okay
print(data[data.temp == data["temp"].max()])
print(data[data.temp == data.temp.max()])
print("\n")

#%% DataFrame.某个heading 是 Series

monday = data[data.day == "Monday"]     # monday is a pandas.DataFrame Object
# print(type(monday))

print(monday.condition)                 # monday.condition is a Series Object
# print(type(monday.condition))


#%% Print Farenheit temperature

### My trying
tryy = monday.temp.to_list()
print(tryy[0]*1.8+32)

### Method 1  直接对 Series 做数学运算（推荐）
"""Pandas 最厉害的地方就在于，它可以直接把加减乘除应用到 Series 身上。"""
# 连 list 都不用转，直接拿 Series 去乘！
fahrenheit_series = monday.temp * 1.8 + 32
print(fahrenheit_series)

### Method 2  精准提取单个数值
"""如果你觉得上面那样打印出来还会带着行号（Index），你就是只想要那个干干净净的数字，
你可以用 Pandas 专门用来提取“唯一值”的 .item() 方法"""
# .item() 会剥开 Series 的外衣，直接把里面那个纯粹的数字（比如 12）递给你
pure_number = monday.temp.item()
print(pure_number * 1.8 + 32)

### Teacher's Method
monday_temp = monday.temp[0]
monday_temp_F = monday_temp * 1.8 + 32
print(monday_temp_F)