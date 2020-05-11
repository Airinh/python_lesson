class MyError(Exception):
    def __init__(self, text):
        self.txt = text


class Store:
    dict_store = {'принтер': 0, 'сканер': 0, 'ксерокс': 0}

    def __str__(self):
        return self.dict_store

    @classmethod
    def instore(self, name, number):
        try:
             if name not in self.dict_store.keys():
                raise MyError('ошибка ввода')
             self.dict_store[name] += number
        except MyError as er:
            print(er)
        except TypeError:
            print('ошибка ввода')

    @classmethod
    def outstore(self, name, number, divis):
        try:
            if name not in self.dict_store.keys():
                raise MyError('ошибка ввода')
            else:
                self.dict_store[name] -= number
                print(f'{name} в количестве {number} штук отправлен в подразделение "{divis}".')
                return [name, number, divis]
        except MyError as er:
            print(er)
        except TypeError:
            print('ошибка ввода')


class Equipment:
    def __init__(self, name):
        self.name = name

    def __call__(self):
        return self.name


class Printer(Equipment):
    def __init__(self, name, type):
        super().__init__(name)
        self.type = type


class Scanner(Equipment):
    def __init__(self, name, view):
        super().__init__(name)
        self.view = view


class Copier(Equipment):
    def __init__(self, name, shape):
        super().__init__(name)
        self.shape = shape


cop1 = Copier('ксерокс', '0110')
Store.instore(cop1.name, 7)
print(Store.dict_store)
Store.outstore(cop1.name, 5, 'отдел кадров')
print(Store.dict_store)
