my_list = [8, 6, 3, 3, 1]
n = input('введите число: ')
while not n.isdigit():
    n = input('Пожалуйста, введите число правильно: ')
n = int(n)
range1 = 0
test = 0
for int in my_list:
    if n > int and test == 0:
        my_list.insert(range1, n)
        test = 1
    range1 += 1
print(my_list)
