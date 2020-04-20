def func(int):
    global sum1
    global test
    if test == 1:
        try:
            sum1 = sum1 + float(int)
            return sum1
        except ValueError:
            print('процесс завершен')
            test = 0
test = 1
sum1 = 0
print('введите числа через пробел: ')
while test == 1:
    list1 = input().split(' ')
    for i in list1:
        func(i)
    print('сумма равна ', sum1)


