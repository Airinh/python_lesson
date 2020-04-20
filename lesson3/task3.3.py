def my_func(x, y, z):
    a = y
    if x < y:
        a = x
    if a > z:
        a = z
    return (x + y + z) - a
test = 'да'
while test == 'да':
    try:
        n1 = int(input('введите первое число: '))
        n2 = int(input('введите второе число: '))
        n3 = int(input('введите третье число: '))
    except ValueError:
        print('пожалуйста, введите числа правильно')
        continue
    print('сумма двух наибольших чисел равна', my_func(n1, n2, n3))
    test = input('хотите продожить? (да/нет) ')
    test = test.lower()
