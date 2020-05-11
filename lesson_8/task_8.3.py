class MyError(Exception):
    def __init__(self, text):
        self.txt = text


list1 = []
while True:
    i = input('введите число (для остановки программы введите "стоп"): ')
    if i == 'стоп':
        break
    try:
        if i.isnumeric():
            list1.append(i)
        else:
            raise MyError('это не число')
    except MyError as er:
        print(er)
print('список чисел:', list1)
