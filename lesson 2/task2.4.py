list3 = input('Введите список значений через пробел: ')
list3 = list3.split(' ')
temp = 1
for int in list3:
    print('{} {:<10}'. format (temp, int))
    temp += 1
