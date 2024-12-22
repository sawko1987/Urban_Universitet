
# Создайте:2 класса родителя: Animal, Plant#
# Для класса Animal атрибуты alive = True(живой) и fed = False(накормленный), name - индивидуальное название каждого животного.

# У каждого из объектов класса Mammal и Predator должны быть атрибуты и методы:
    # eat(self, food) - метод, где food - это параметр, принимающий объекты классов растений.
#     # В данном случае можно использовать принцип наследования, чтобы не дублировать код.


class Animal:
    alive = True
    fed = False
    def __init__(self,name):
        self.name= name

# Метод eat должен работать следующим образом:
    # Если переданное растение (food) съедобное - выводит на экран "<self.name> съел <food.name>", меняется атрибут fed на True.
    #
    # Если переданное растение (food) не съедобное - выводит на экран "<self.name> не стал есть <food.name>", меняется атрибут alive на False.
    # Т.е если животному дать съедобное растение, то животное насытится, если не съедобное - погибнет.

    def eat(self,food):
        self.food = Plant.edible
        if not self.food == Plant.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


# Для класса Plant атрибут edible = False(съедобность), name - индивидуальное название каждого растения
class Plant:
   edible = True
   def __init__(self,name):
       self.name = name


# 4 класса наследника:
# Mammal,Predator для Animal.
# Flower, Fruit для Plant.

class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Flower(Plant):
    pass

class Fruit(Plant):
    pass


a1 = Predator('Волк с Уолл-Стрит')

a2 = Mammal('Хатико')

p1 = Flower('Цветик семицветик')

p2 = Fruit('Заводной апельсин')



print(a1.name)

print(p1.name)



print(a1.alive)

print(a2.fed)

a1.eat(p1)

a2.eat(p2)

print(a1.alive)

print(a2.fed)
