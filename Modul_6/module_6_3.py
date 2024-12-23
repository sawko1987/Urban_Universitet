
import random

class Animal:
    live= True
    sound =None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed,_cords = [0,0,0]) :
        self._cords = _cords
        self.speed = int(speed)

    def move(self, dx, dy, dz):
        self._cords[0] = int(dx)*self.speed
        self._cords[1] = int(dy)*self.speed
        if dz<=0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[2] = int(dz)*self.speed

    def get_coards(self):
        print (f" X:{self._cords[0]},Y: {self._cords[1]}, Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER <5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        print (str(self.sound))

class Bird(Animal):
    beak = True
    def lay_eggs(self):
        print(f"Here are(is) {random.randint(1,4)} eggs for you")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3.

    def dive_in(self, dz):
        dz =  abs(dz)* self.speed/2
        self._cords[2] = dz

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(Bird,PoisonousAnimal, AquaticAnimal ):
    sound = "Click-click-click"
    def __init__(self,speed):
        super().__init__(speed)

db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_coards()
db.dive_in(6)
db.get_coards()
db.lay_eggs()