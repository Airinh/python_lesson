from sys import argv
_, hours, rate, premium = argv
try:
    hours = int(hours)
    rate = int(rate)
    premium = int(premium)
    print(f'заработная плата составит {hours * rate + premium}')
except ValueError:
    print('ошибка ввода')
