import csv

### CHALLENGE 2: Get all the temperature info out and stack them as a list
temperatures = []
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)

    # 魔法就在这里：先把表头单独读取出来，指针就自动走到下一行了
    header = next(data)

    for row in data:
        temperatures.append(int(row[1]))
    print(temperatures)

# INFO: 如果第9行不做处理，那么"temp"就会被for循环读到，int()就会尝试把"temp"转成integer，然后就会报错：

# Traceback (most recent call last):
#   File "D:\1CodingSpace\Python\Python100\Day25_Working_with_CSV_Data_and_the_Pandas_Library\No190_Reading_CSV_Data_in_Python\190_Reading_CSV_Data_in_Python.py", line 32, in <module>
#     temperatures.append(int(row[1]))
#                         ^^^^^^^^^^^
# ValueError: invalid literal for int() with base 10: 'temp'