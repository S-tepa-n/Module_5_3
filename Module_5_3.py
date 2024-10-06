class House:
    def __init__(self, name, number):
        self.name = name
        self.number = int(number)

    def __len__(self):
        return self.number

    def __str__(self):
        return (f'Название:{self.name},кол-во этажей:{self.number}')

    def __eq__(self, other):
        return self.number == other.number

    def __lt__(self, other):
        return self.number < other.number

    def __gt__(self, other):
        return self.number > other.number

    def __le__(self, other):
        return self.number <= other.number

    def __ge__(self, other):
        return self.number >= other.number

    def __ne__(self, other):
        return self.number != other.number

    def __add__(self, value):
        if isinstance(value,int):
            self.number = self.number + value
        return self

    def __radd__(self, valse):
        if isinstance(valse, int):
            self.number = self.number + valse
        return self

    def __iadd__(self, valse):
        if isinstance(valse, int):
            self.number = self.number + valse
        return self

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
