from abc import ABC, abstractmethod


class Wear(ABC):

    @property
    @abstractmethod
    def calc(self):
        pass


class Suit(Wear):
    def __init__(self, name, height):
        self.height = height
        self.name = name

    @property
    def calc(self):
        return round(2 * self.height + 0.3, 2)


class Coat(Wear):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    @property
    def calc(self):
        return round(self.size / 6.5 + 0.5, 2)


suit1 = Suit('костюм серый', 1.2)
coat1 = Coat('пальто красное', 48)
print(suit1.calc)
print(coat1.calc)
