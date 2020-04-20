def my_func(x, y):
    return x ** y
def my_func1(x, y):
    c = 1
    for i in range(abs(y)):
        c = c / x
    return c
test = 'да'
while test == 'да':
    try:
        n1 = float(input('введите действительное положительное число х: '))
        n2 = int(input('введите целое отрицательное число у: '))
    except ValueError:
        print('пожалуйста, введите число правильно')
        continue
    if n1 < 0 or n2 >= 0:
        print('пожалуйста, введите числа правильно')
        continue
    print('x в степени y по первому варианту: ', my_func(n1, n2))
    print('x в степени y по второму варианту:', my_func1(n1, n2))
    test = input('хотите продожить? (да/нет) ')
    test = test.lower()
