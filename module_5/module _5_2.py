class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = int(number_of_floors)
        self.new_floor = None

    def go_to(self, new_floor):
        self.new_floor = new_floor
        if int(self.new_floor) > self.number_of_floors or int(self.new_floor) < 0:
            print('Такого этажа не существует')
        else:
            print(f'Перемещаемся на этаж {self.new_floor}')

h1 = House(name="ЖК Горский", number_of_floors=18)
h1.go_to(5)