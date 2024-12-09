class House:
    def __init__(self, name, number_of_floors):
        self.new_floor = None
        self.name = name
        self.number_of_floors = int(number_of_floors)

    def go_to(self,new_floor):
        self.new_floor = new_floor
        if int(self.new_floor) < 0 or int(self.new_floor) > self.number_of_floors:
            print('"Такого этажа не существует"')
        else:
           print(f'Проийдете на {self.new_floor} этаж')




h1 = House('ЖК Горский', 18)
h1.go_to(5)
h2 = House('Домик в деревне', 2)
h3 = House('ЖК Эльбрус', 30)
h1.go_to(5)
h2.go_to(10)
h3.go_to(15)

