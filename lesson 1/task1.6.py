a = input('Введите начальный результат, км: ')
while not a.isdigit():
    a = input('Пожалуйста, введите число правильно: ')
a = int(a)
b = input('Введите конечный результат, км: ')
while True:
    if not b.isdigit():
        b = input('Пожалуйста, введите число правильно: ')
        continue
    else:
        b = int(b)
    if b < a:
        b = input('Конечный результат должен быть больше начального, пожалуйста, введите число правильно: ')
        continue
    break
number = 1
while a < b:
    print("{}-й день: {:.2f}". format(number, a))
    a = a * 1.1
    number = number + 1
print("{}-й день: {:.2f}". format(number, a))
print()
print(f'Ответ: на {number}-й день спортсмен достиг результата - не менее {b} км')