from prettytable import PrettyTable    # from prettytable PACKAGE get PrettyTable CLASS

table = PrettyTable()
# print(table)    # This line of code prints the backbone of a Pretty table, it is difficult to decipher it though

table.add_column("Pokemon Name",["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type",["Electric", "Water", "Fire"])
print(table)
table.align = "l"   # Set it to left aligned

print(table)