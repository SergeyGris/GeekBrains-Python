class Car:
    def __init__(self, color, name, speed=0, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed=30):
        self.speed = speed
        print(f'Машина поехала со скоростью {self.speed} км/ч')

    def stop(self):
        self.speed = 0
        print(f'Машина остановилась. Текущая скорость равна {self.speed} км/ч')

    def turn(self, direction='направо'):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        if self.speed >= 60:
            print(f'Превышение скорости! Ваша скорость {self.speed} км/ч')
        else:
            super().show_speed()


class SportCar(Car): pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed >= 40:
            print(f'Превышение скорости! Ваша скорость {self.speed} км/ч')
        else:
            super().show_speed()


class PoliceCar(Car):
    def __init__(self, color, name, speed=0):
        # self.is_police = is_police
        super().__init__(color, name, speed, is_police=True)


# не понимаю, почему у car_4 все равно атрибут is_police меняется на False.
# Подскажите, как его надо было правильно изменить?


car_1 = TownCar('red', 'Mazda')
car_2 = WorkCar('blue', 'Ford')
car_3 = SportCar('yellow', 'Ferrari')
car_4 = PoliceCar('white', 'Chevrolet')
