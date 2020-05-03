class Stationery:
    title = 'kp'
    def draw(self):
        print('Запуск отрисовки')


class Pen:
    title = 'ручка'
    def draw(self):
        print('прорисовка деталей')

class Pensil:
    title = 'карандаш'
    def draw(self):
        print('рисуем черновик')

class Handle:
    title = 'маркер'
    def draw(self):
        print('выделение')


step0 = Stationery()
step0.draw()
step1 = Pensil()
step1.draw()
step2 = Pen()
step2.draw()
step3 = Handle()
step3.draw()
print(step2.title)
