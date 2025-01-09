import math
class Figure:
    sides_count = 0

    def __init__(self,__color:list,*__sides:list, filled = True, ):   #__sides - список сторон  __color(список цветов)
        self.__sides = __sides
        self.__color = __color
        self.filled = filled

    def get_color(self):    # Метод get_color, возвращает список RGB цветов.
       return list(self.__color)

# Метод __is_valid_color - служебный, принимает параметры r, g, b, который проверяет корректность переданных значений перед установкой  нового цвета.
# Корректным цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
    def __is_valid_color(self,r, g, b):
        if type(r) in int and type(g) in int and type(b) in int:
            self.r = r
            self.g = g
            self.b = b
        return r,g,b
#  предварительно проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним.
    
    def set_color(self,r, g, b):
        if self.__is_valid_color:
            return f"Цвет изменится"
        else:
            return f"Цвет останется прежним"

# Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон, возвращает True если все стороны целые положительные числа
#  и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.
    def __is_valid_sides (self, *__sides):
        for i in self.__sides:
            if type(i) in int and type(i) in int:
                return True
            else:
                return False

    def get_sides(self): # Метод get_sides должен возвращать значение я атрибута __sides.
        return self.__sides


    def __len__(self):       # Метод __len__ должен возвращать периметр фигуры.
       return sum(self.get_sides())

# Метод set_sides(self, *new_sides) должен принимать новые стороны, если их количество не равно sides_count,
    # то не изменять, в противном случае - менять.
    def set_sides(self,*new_sides):
        if self.sides_count != new_sides:
            self.sides_count = new_sides
        return self.sides_count

# Атрибуты класса Circle: sides_count = 1
# Каждый объект класса Circle должен обладать следующими атрибутами и методами:
# Все атрибуты и методы класса Figure
# Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).

class Circle(Figure):
    sides_count =1
    

    def get_square(self,): # Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус).
        return math.pi * self.__radius**2





Circle((200, 200, 100), 10, 15, 6) #, т.к. сторона у круга всего 1, то его стороны будут - [1]
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)

#Проверка на изменение цветов:
# #
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
# #

# # #
# # Проверка на изменение сторон:


circle1.set_sides(15) # Изменится
print(circle1.get_sides())

print(len(circle1)) # Проверка периметра (круга), это и есть длина:

