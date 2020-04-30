while True:
    str1 = input('введите строку: ')
    f_obj = open("new_file.txt", 'a')
    f_obj.write(str1 + '\n')
    f_obj.close()
    if not str1:
        break
with open("new_file.txt") as f_obj:
    print(f_obj.read())
