list2 = input('Введите список значений через запятую: ')
list2 = list2.split(',')
for i in range(len(list2)-1):
    if i % 2 == 0:
        temp = list2[i]
        list2[i] = list2[i+1]
        list2[i+1] = temp
print('результат:', list2)

