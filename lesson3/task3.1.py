def func_del(rez):
    arg_1 = input('введите первое число: ')
    arg_2 = input('введите второе число: ')
    try:
        arg_1 = int(arg_1)
        arg_2 = int(arg_2)
        return arg_1 / arg_2
    except ValueError:
        print('введите числа правильно')
    except ZeroDivisionError:
        print('на 0 делить нельзя')
test = 'да'
rez_1 = 0
while test == 'да':
    rez_1 = func_del(rez_1)
    if rez_1 != None:
        print(f'результат деления: {rez_1:.2f}')
    else: continue
    test = input('Хотите еще посчитать? (да/нет) ')
    test = test.lower()
