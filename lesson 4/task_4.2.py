my_list = [10, 11, 8, 9, 23, 25, 26]
new_list = [my_list[i] for i in range(1,len(my_list)) if my_list[i] > my_list[i-1]]
print(new_list)
