my_f = open("task_5.2.txt", "r")
n = 0
for line in my_f:
    n += 1
    str1 = line
    print(f'количество слов в {n} строке = {len(str1.split())}')
my_f.close()
print('количество строк в файле - ', n)
