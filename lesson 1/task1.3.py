n = input('Введите число: ')
while not n.isdigit():
    n = input('Пожалуйста, введите число правильно: ')
n = str(n)
nn = n * 2
nnn = n * 3
print(f'итог = {int(n) + int(nn) + int(nnn)}')
