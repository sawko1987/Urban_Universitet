class House:
    def __init__(self, name, number_of_floors):
        self.new_floor = None
        self.name = name
        self.number_of_floors = int(number_of_floors)

    def go_to(self, new_floor):
        self.new_floor = new_floor
        if int(self.new_floor) < 0 or int(self.new_floor) > self.number_of_floors:
            print('"Такого этажа не существует"')
        else:
            print(f'Мы на {self.new_floor} этаже')
        for i in range(1, self.new_floor + 1):
            print(f"Этаж №{i}")
            print(f'Мы идём на {self.new_floor} этаж')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name} Этажей:{self.number_of_floors}"
    def __eq__(self, other):
        if isinstance(self.number_of_floors, int):
            return self.number_of_floors == other.number_of_floors
    def __lt__(self, other):
        if isinstance(self.number_of_floors, int):
            return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        if isinstance(self.number_of_floors, int):
            return self.number_of_floors <= other.number_of_floors
    def __gt__(self, other):
        if isinstance(self.number_of_floors, int):
            return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        if isinstance(self.number_of_floors, int):
            return self.number_of_floors >= other.number_of_floors
    def __ne__(self, other):
        if isinstance(self.number_of_floors, int):
             return self.number_of_floors != other.number_of_floors
    def __add__(self, other):
        if isinstance(other, House):
            self.number_of_floors = self.number_of_floors + other.number_of_floors
            return self
        elif isinstance(other, int):
            self.number_of_floors = self.number_of_floors + other
            return self
        else:
            print(f"""Полученное значение {other} не является целым числом или объектом House. 
          Увеличить количество этажей не представляется возможным""")
            return self
    def __radd__(self, other):
        if isinstance(other, House):
            self.number_of_floors = self.number_of_floors + other.number_of_floors
            return self
        elif isinstance(other, int):
            self.number_of_floors = self.number_of_floors + other
            return self
        else:
            print(f"""Полученное значение {other} не является целым числом или объектом House. 
          Увеличить количество этажей не представляется возможным""")
            return self

    def __iadd__(self, other):
        if isinstance(other, House):
            self.number_of_floors = self.number_of_floors + other.number_of_floors
            return self
        elif isinstance(other, int):
            self.number_of_floors = self.number_of_floors + other
            return self
        else:
            print(f"""Полученное значение {other} не является целым числом или объектом House. 
          Увеличить количество этажей не представляется возможным""")
            return self




h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House('ЖК Эльбрус', 30)
print(len(h1))
h1.go_to(5)
print (str(h1))
print(h1)
print(h2)
print(h1 == h2) # __eq__
h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)
h1 += 10 # __iadd__
print(h1)
h2 = 10 + h2 # __radd__
print(h2)
print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h2 < h3)
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
print(len(h2))
h2.go_to(10)
print (str(h2))
print(len(h3))
h3.go_to(15)
print (str(h3))




