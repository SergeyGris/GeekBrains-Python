class Cell:
    def __init__(self, cell_number=1):
        self.cell_number = int(cell_number)

    def __add__(self, other):
        rez = self.cell_number + other.cell_number
        return rez

    def __str__(self):
        cells = '*' * self.cell_number
        rez = f'{cells}\n'
        return rez

    def __sub__(self, other):
        if self.cell_number > other.cell_number:
            rez = self.cell_number - other.cell_number
            return rez
        else:
            raise ValueError

    def __mul__(self, other):
        rez = self.cell_number * other.cell_number
        return rez

    def __floordiv__(self, other):
        rez = self.cell_number // other.cell_number
        return rez

    def make_order(self, cells_in_row):
        rows = self.cell_number // cells_in_row
        cells_left = self.cell_number % cells_in_row
        cells_in_row_str = rows * (cells_in_row * '*' + '\n')
        cells_left_str = cells_left * '*'
        return f'{cells_in_row_str}{cells_left_str}'


c1 = Cell(10)
c2 = Cell(5)
c3 = Cell(20)
c4 = Cell(11)
c5 = Cell(3)
c6 = Cell(6)

print("c1+c2=", c1 + c2)
try:
    print("c3-c2=", c3 - c2)
    print("c4-c3=", c4 - c3)
except ValueError:
    print('Операция не может быть выполнена')
print("c5*c6=", c5 * c6)
print("c3//c1=", c3 // c1)
print("c3.make_order(5)=", c3.make_order(5))
print("c1.make_order(7)=", c1.make_order(7))
