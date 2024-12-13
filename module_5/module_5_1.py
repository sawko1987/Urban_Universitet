

class House:
        def __init__(self, name, number_of_floors, new_floor):
            self.new_floor = None
            self.name = name
            self.number_of_floors = int(number_of_floors)
            self.new_floor = new_floor
        def go_to(self):

            if int(self.new_floor) < 0 or int(self.new_floor) > self.number_of_floors:
                print('"Такого этажа не существует"')
            else:
                print(f'Мы идем на {self.new_floor} этаж')
            for i in range (1, self.new_floor+1):
                print (f"Этаж №{i}")
                print(f'Мы пришли на {self.new_floor} этаж')



h1 = House('ЖК Горский', 18, 5)
h1.go_to()
# h2 = House('Домик в деревне', 2)
# h3 = House('ЖК Эльбрус', 30)
# h1.go_to(5)
# h2.go_to(10)
# h3.go_to(15)
# #

# class A:
#     name1 = "Alex"
#     def __init__(self, name):
#         self.name = name
#
# a1 = A("Matvey")
# a2 = A("Людмила")
# # print(a1.name)
# # print(a2.name)
# # print(a1.name1)
# # print(a2.name1)
# A.name1 = "Serg"
# print(a1.name1)
# print(a2.name1)