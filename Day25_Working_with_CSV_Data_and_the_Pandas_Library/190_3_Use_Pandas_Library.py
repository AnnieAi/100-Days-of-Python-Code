import pandas

data = pandas.read_csv("weather_data.csv")
print(data)

print("\n")
print(data["temp"])


# Provides another way to access the data.
# Fewer lines, better formatting.
