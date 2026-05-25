with open("weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)
    # ['day,temp,condition\n', 'Monday,12,Sunny\n', 'Tuesday,14,Rain\n', 'Wednesday,15,Rain\n', 'Thursday,14,Cloudy\n', 'Friday,21,Sunny\n', 'Saturday,22,Sunny\n', 'Sunday,24,Sunny']

    # painful to read
    # a list; all elements are string;
    # inside the string there are content, comma, and \n, mingled together