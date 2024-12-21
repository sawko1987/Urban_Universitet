

class Car:
    motor = 1
    def __init__(self, brand):
        self.brand = brand

    def __str__(self):
        return f'{self.brand} {self.motor}'


car1 = Car('BMW')
car2 = Car('Mazda')
print (car1)
print (car2)
Car.motor = 2
print (car1)
print (car2)