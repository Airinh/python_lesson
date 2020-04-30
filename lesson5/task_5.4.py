with open("task_5.4.txt", encoding='utf-8') as my_f1:
    text1 = my_f1.read()
    text1.replace('One', 'Один')
    text1.replace('Two', 'Два')
    text1.replace('Three', 'Три')
    text1.replace('Four', 'Четыре')
my_f2 = open("task_5.4_new.txt", 'w', encoding='utf-8')
my_f2.write(text1)
my_f2.close()
