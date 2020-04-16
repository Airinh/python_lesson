name = "N"
age = 0
print('Здравствуй,', name, ',тебе', age, '?')
name = input('Как тебя зовут? ')
print('Привет,', name, '!')
age = input('Сколько тебе лет? ')
while not age.isdigit():
    age = input('Введи правильно число лет: ')
age = int(age)
print('Здравствуй,', name, ',тебе уже', age, '!')
