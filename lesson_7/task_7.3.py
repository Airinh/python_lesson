class Cell:
    def __init__(self, cell_number: int):
        self.cell_number = cell_number

    def __add__(self, other):
        return Cell(self.cell_number + other.cell_number)

    def __sub__(self, other):
        if self.cell_number > other.cell_number:
            return Cell(self.cell_number + other.cell_number)
        else:
            print('вычитание невозможно')

    def __mul__(self, other):
        return Cell(self.cell_number * other.cell_number)

    def __truediv__(self, other):
        return Cell(self.cell_number // other.cell_number)

    def make_order(self, count: int):
        var = self.cell_number // count
        return '/n'.join(['*' for i in range(var)])


c1 = Cell(18)
print(c1.make_order(4))
c2 = Cell(19)
c3 = c1 + c2
print(c3.cell_number)
