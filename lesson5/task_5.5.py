import random
file1 = open("task_5.5.txt", 'w+')
n = 12
for i in range(0, n):
    file1.write(str(random.randint(1, n)) + ' ')
file1.seek(0)
str1 = file1.readline()
print(str1)
list1 = str1.split()
sum1 = 0
for i in list1:
    sum1 += int(i)
print('сумма равна ', sum1)
file1.close()
