class Clothes:
    # reserved_cloth = 0
    # cloth_require=0
    def __init__(self, size):
        self.size = size
        self.cloth_required = self.cloth_require()

    @property
    def add_to_reserve(self):
        self.reserved_cloth += self.cloth_required
        return self.reserved_cloth

    @property
    def cloth_require(self):
        return self.cloth_required


class Coat(Clothes):
    reserved_cloth = 0

    def cloth_require(self):
        self.cloth_required = self.size / 6.5 + 0.5
        return self.cloth_required


class Suit(Clothes):
    reserved_cloth = 0

    def cloth_require(self):
        self.cloth_required = self.size * 2 + 0.3
        return self.cloth_required


c1 = Coat(12)
c2 = Coat(20)
c3 = Coat(120)
c1.add_to_reserve
c2.add_to_reserve
c3.add_to_reserve
s1 = Suit(15)
s2 = Suit(50)
s3 = Suit(150)
s1.add_to_reserve
s2.add_to_reserve
s3.add_to_reserve
print(f'Coats : {c3.reserved_cloth}')
print(f'Suits : {s3.reserved_cloth}')
