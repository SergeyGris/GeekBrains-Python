class Road:
    def __init__(self, length, width, depth, mass=25):
        self._length = length
        self._width = width
        self._mass = mass
        self._depth = depth

    def mass(self):
        mass = self._mass * self._width * self._length * self._depth / 1000
        rez = f'{self._width} м*{self._length} м*{self._mass} кг*{self._depth} см = {int(mass)} т'
        print(rez)


road_1 = Road(5000, 20, 5, 25)
road_2 = Road(2000, 20, 5)
road_1.mass()
road_2.mass()
