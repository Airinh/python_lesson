import os
import json
pathfile = os.path.join(os.path.dirname(__file__), 'task_5.7.txt')
profit_o = {}
profit_f = {}
profit = 0
number = 0
with open(pathfile, 'r', encoding='utf-8') as file7:
    while True:
        list1 = file7.readline().split()
        if list1:
            count = float(list1[2]) - float(list1[3])
            profit_f[list1[0]] = count
            if count >= 0:
                profit += count
                number += 1
        else:
            break
profit = profit / number
profit_o["average_profit"] = profit
list2 = [profit_f, profit_o]
print(list2)
with open("task_5.7.json", "a") as file8:
    json.dump(list2, file8)
