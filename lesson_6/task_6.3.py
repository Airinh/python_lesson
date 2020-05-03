class Worker:
    def __init__(self, position, name, surname, salary, bonus):
        self.position1 = position
        self.name = name
        self.surname = surname
        self._income = {"salary": salary, "bonus": bonus}


class Position(Worker):

    def __init__(self, position, name, surname, salary, bonus):
        super().__init__(position, name, surname, salary, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return sum(self._income.values())


work1 = Position('кассир', 'Андрей', 'Иванов', 30000, 10000)
print(f'{work1.get_full_name()} получил доход {work1.get_total_income()}')
