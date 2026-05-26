import csv

### CHALLENGE 2: Get all the temperature info out and stack them as a list
temperatures = []
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)

    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)
