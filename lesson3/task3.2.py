def person(name, surname, date, town, email, telephone):
    print(name, surname, date, town, email, telephone)
test = 'да'
diction = {'имя', 'фамилия', 'год рождения', 'город проживания', 'e-mail', 'телефон'}
diction_pers = {'имя': '1', 'фамилия': '2', 'год рождения': '3', 'город проживания': '4', 'e-mail': '5', 'телефон': '6'}
while test == 'да':
    for i in diction:
        print(i, ': ')
        diction_pers[i] = input()
    person(name=diction_pers['имя'], surname=diction_pers['фамилия'], date=diction_pers['год рождения'], town=diction_pers['город проживания'], email=diction_pers['e-mail'], telephone=diction_pers['телефон'])
    test = input('хотите продолжить ввод? (да/нет)')
    test = test.lower()
