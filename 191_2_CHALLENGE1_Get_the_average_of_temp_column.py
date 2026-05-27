import pandas

data = pandas.read_csv("../weather_data.csv")
temp_list = data["temp"].to_list()
print(temp_list)

#%% -- Method 1: Pure Maths --

list_average1 = sum(temp_list)/len(temp_list)   # 传入list作为参数
print(list_average1)


#%% -- Method 2: Python pre-installed Library "statistics" --

import statistics
list_average2 = statistics.mean(temp_list)      # 用list调用函数
print(list_average2)


#%% -- Method 3: Pandas Library's Function --

# list_average3 = temp_list.mean()      # AttributeError: 'list' object has no attribute 'mean'
list_average3 = data["temp"].mean()     # 要用Series调用函数，不能用list调用
print(list_average3)