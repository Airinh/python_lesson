income = input('Введите выручку фирмы за период: ')
while not income.isdigit():
    income = input('Пожалуйста, введите число правильно: ')
expense = input('Введите расходы фирмы за период: ')
while not expense.isdigit():
    expense = input('Пожалуйста, введите число правильно: ')
income = int(income)
expense = int(expense)
profit = income - expense
print('Ваша прибыль составит', profit)
if profit > 0:
    rent = round(profit / income * 100, 1)
    print("Рентабельность выручки - ", rent, "%")
number = input('Введите число сотрудников фирмы: ')
while not number.isdigit():
    number = input('Пожалуйста, введите число правильно: ')
number = int(number)
print(f'Прибыль на одного сотрудника = {round(profit / number, 2)}')
