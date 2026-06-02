my_tuple = (1,3,8)

print(my_tuple[0]) # 1
print(my_tuple[1]) # 3
print(my_tuple[2]) # 8

# my_tuple[2] = 12  # TypeError: 'tuple' object does not support item assignment

my_list = list(my_tuple)
my_list[2] = 2
print(my_list)
