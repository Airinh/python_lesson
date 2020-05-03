class Car:
    def __init__(self,  color: str, name: str, speed: float, is_police: bool = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self):
        direction = input('куда поедем? (налево, направо, прямо): ')
        if direction in ('налево', 'направо', 'прямо'):
            print(f'машина поехала {direction}')
        else:
            print('машина не поняла')

    def show_speed(self):
        print('скорость', self.speed)

class TownCar(Car):
    version = 1
    def show_speed(self):
        if self.speed > 60:
            print(f'скорость {self.speed}, превышена!')
        else:
            print('скорость', self.speed)


class SportCar(Car):
    version = 2

class WorkCar(Car):
    version = 3
    def show_speed(self):
        if self.speed > 40:
            print(f'скорость {self.speed}, превышена!')
        else:
            print('скорость', self.speed)


class PoliceCar(Car):
    version = 4

car1 = WorkCar('желтый', 'солярис', 60, True)
car1.turn()
car1.show_speed()

