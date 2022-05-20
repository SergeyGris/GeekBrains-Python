class Complex():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Complex(x,y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Complex(x,y)

    def __mul__(self, other):
        x = self.x * other.x - self.y * other.y
        y = self.x * other.y + self.y * other.x
        return Complex(x,y)

    def __str__(self):
        i="+"
        if self.y<0:
            i=''
        return f'{self.x}{i}{self.y}i'


n1 = Complex(1, 2)
n2 = Complex(3, 4)
n3 = n1 + n2
n4 = n1 - n2
n5 = n1 * n2
print('Число 1: ',n1)
print('Число 2: ',n2)
print('Операции с комплексными числами:')
print(f'Сложение: {n3} = {n1} + {n2}')
print(f'Вычитание: {n4} = {n1} - {n2}')
print(f'Умножение: {n5} = {n1} * {n2}')
