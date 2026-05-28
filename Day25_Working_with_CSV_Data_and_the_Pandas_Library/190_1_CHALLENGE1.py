import csv

### CHALLENGE 1: Use csv library to read csv file

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    print(data)     # <_csv.reader object at 0x0000028B67586B00>        a csv object was created
    for row in data:
        print(row)
    # ['day', 'temp', 'condition']
    # ['Monday', '12', 'Sunny']
    # ['Tuesday', '14', 'Rain']
    # ['Wednesday', '15', 'Rain']
    # ['Thursday', '14', 'Cloudy']
    # ['Friday', '21', 'Sunny']
    # ['Saturday', '22', 'Sunny']
    # ['Sunday', '24', 'Sunny']

    # easier to read;
    # 之前的列表中的每个元素都被视作一个单独的列表;
    # 每个列表内部被comma分隔的content都被拆出来变成了列表里的一个个元素
