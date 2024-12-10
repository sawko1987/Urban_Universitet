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





h1 = House('ЖК Горский', 18)
print(len(h1))
h1.go_to(5)
print (str(h1))

h2 = House('Домик в деревне', 2)
print(len(h2))
h2.go_to(10)
print (str(h2))

h3 = House('ЖК Эльбрус', 30)
print(len(h3))
h3.go_to(15)
print (str(h3))




