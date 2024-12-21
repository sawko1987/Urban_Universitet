class Animal:
    alive = True
    fed = False
    name = None




class Plant:
   edible = False
   name = None



class Mammal(Animal):
    def eat(self,food):
        self.food = food
        if self.food != Plant.edible:
            print(f"{self.name} съел {food.name}")
            Animal.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            Animal.alive = False


class Predator(Animal):
    def __init__(self, eat):
        self.eat = eat


class Flower(Plant):
    def __init__(self, eat):
        self.eat = eat


class Fruit(Plant):
    edible = True



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

