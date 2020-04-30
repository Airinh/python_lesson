my_f2 = open("new.txt", "r", encoding='utf-8')
n = 0
income = float(0)
print('Доход менее 20 тыс. получают: ')
while True:
    n += 1
    str1 = my_f2.readline()
    if not str1:
        break
    else:
        list1 = str1.split()
    if float(list1[1]) < 20:
        print(list1[0])
    income += float(list1[1])
my_f2.close()
print(f'Средний доход - {(income / n):.2f}')
