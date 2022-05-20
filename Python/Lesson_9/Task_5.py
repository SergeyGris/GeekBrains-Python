class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'У вас в руках {self.title}')


class Pen(Stationary):
    def draw(self):
        print(f'У вас в руках {self.title}')


class Pencil(Stationary):
    def draw(self):
        print(f'У вас в руках {self.title}')


class Handle(Stationary):
    def draw(self):
        print(f'У вас в руках {self.title}')

nothing=Stationary('ничего нет')
pen=Pen('ручка')
pencil=Pencil('карандаш')
handle=Handle('маркер')

nothing.draw()
pen.draw()
pencil.draw()
handle.draw()