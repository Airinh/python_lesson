subjs = {}
with open("task_5.6.txt", encoding='utf-8') as file1:
    for line in file1:
        hours = 0
        temp0 = 0
        for i in range(len(line.split(':')[0]) + 1, len(line)):
            temp = line[i]
            i1 = i + 1
            while True:
                if temp.isdigit():
                    temp0 = int(temp)
                    temp += line[i1]
                    i1 += 1
                else:
                    hours += temp0
                    break
        subjs[line.split(':')[0]] = hours
print(subjs)
