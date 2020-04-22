my_list = [10, 11, 10, 8, 9, 8, 23, 25, 26, 9]
new_list = [el for el in my_list if my_list.count(el) == 1]
print(new_list)
