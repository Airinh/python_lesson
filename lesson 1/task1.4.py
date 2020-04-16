nat = input ('введите целое положительное число: ')
while not nat.isdigit():
    nat = input('Пожалуйста, введите число правильно: ')
natwork = int(nat)
while natwork < 0:
    nat = input('Пожалуйста, введите число правильно: ')
while not nat.isdigit():
    nat = input('Пожалуйста, введите число правильно: ')
natwork = int(nat)
nat1 = natwork % 10
nat2 = 0
while natwork > 0:
    nat2 = (natwork // 10) % 10
    if nat1 < nat2:
        nat1 = nat2
    natwork = int((natwork - nat2) / 10)
print('наибольшая цифра в числе', nat, '-', nat1)
