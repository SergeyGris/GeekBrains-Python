class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        wage, bonus = income
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    # def __init__(self,name, surname, position, income):
    #     super().__init__(name, surname, position, income)
    def get_full_name(self):
        name = self.name
        surname = self.surname
        full_name = (f'{name} {surname}')
        print(full_name)

    def get_total_income(self):
        wage = self._income['wage']
        bonus = self._income['bonus']
        total_income = wage + bonus
        print(total_income)



pos_1 = Position('Alex', 'Manin', 'manager', (20000, 5000))
pos_1.get_full_name()
pos_1.get_total_income()

pos_2 = Position('Sergey', 'Grishin', 'seller', (10000, 2000))
pos_2.get_full_name()
pos_2.get_total_income()