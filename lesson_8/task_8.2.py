class MyError(Exception):
    def __init__(self, text):
        self.txt = text

try:
    a = int(input('введите делимое: '))
    b = int(input('введите делитель: '))
    if b == 0:
        raise MyError('На 0 делить нельзя')
    else:
        print(f'частное равно {a / b:.2f}')
except MyError as err:
    print(err)
except ValueError:
    print('ошибка ввода')
