n = input('Введите число от 1 до 12: ')
while True:
    if n.isdigit():
        n = int(n)
        if n > 12 or n < 0:
            n = input('Пожалуйста, введите число правильно: ')
            continue
        else:
            break
    else:
        continue
time = {'зима': [1, 2, 12], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}
for int in time:
    if n in time.get(int):
        print('это', int)
