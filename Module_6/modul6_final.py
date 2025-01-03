import math
class Figure:
    def __init__(self,__color,*__sides:tuple, filled = True,sides_count = 0 ):   #__sides - список сторон  __color(список цветов)
        self.__sides = __sides
        self.__color = __color
        self.filled = filled
        self.sides_count = sides_count

    def get_color(self):    # Метод get_color, возвращает список RGB цветов.
        return list(self.__color)

# Метод __is_valid_color - служебный, принимает параметры r, g, b, который проверяет корректность переданных значений перед установкой  нового цвета.
# Корректным цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
    def __is_valid_color(self,r, g, b):
        if type(r) in int and type(g) in int and type(b) in int:
            self.r = r
            self.g = g
            self.b = b
        return (r,g,b)
#  предварительно проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним.
    
    def set_color(self,r, g, b):
        pass
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
        perimeter = 0
        perimeter += self.__sides
        return perimeter

# Метод set_sides(self, *new_sides) должен принимать новые стороны, если их количество не равно sides_count, то не изменять, в противном случае - менять.
    def set_sides(self,__sides):
        if self.len(self.__sides) != len(__sides):
            __sides = self.__sides
        return self.__sides

# Атрибуты класса Circle: sides_count = 1
# Каждый объект класса Circle должен обладать следующими атрибутами и методами:
# Все атрибуты и методы класса Figure
# Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).

class Circle(Figure):
    sides_count =1
    __radius = None

    def get_square(self): # Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус).
        return math.pi * self.__radius**2

# Атрибуты класса Triangle: sides_count = 3
# Каждый объект класса Triangle должен обладать следующими атрибутами и методами:
# Все атрибуты и методы класса Figure
class Triangle(Figure):
    sides_count = 3

# Метод get_square возвращает площадь треугольника. (можно рассчитать по формуле Герона)
    def get_square(self):
        pass

# Атрибуты класса Cube: sides_count = 12
# Каждый объект класса Cube должен обладать следующими атрибутами и методами:
# Все атрибуты и методы класса Figure.
# Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
class Cube(Figure):

    def __init__(self, __color, *__sides, filled=True, sides_count=12):  # __sides - список сторон  __color(список цветов)
        self.__sides = __sides
        self.__color = __color
        self.filled = filled
        self.sides_count = sides_count

    def get_color(self):  # Метод get_color, возвращает список RGB цветов.
        return list(self.__color)

        # Метод __is_valid_color - служебный, принимает параметры r, g, b, который проверяет корректность переданных значений перед установкой  нового цвета.
        # Корректным цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).

    def __is_valid_color(self, r, g, b):
        if type(r) in int and type(g) in int and type(b) in int:
            self.r = r
            self.g = g
            self.b = b
        return (r)

        #  предварительно проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним.

    def set_color(self, r, g, b):
        pass

        # Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон, возвращает True если все стороны целые положительные числа
        #  и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.

    def __is_valid_sides(self, *__sides):
        pass

        # Метод get_sides должен возвращать значение я атрибута __sides.

    def get_sides(self):
        return self.__sides

    def __len__(self):  # Метод __len__ должен возвращать периметр фигуры.
        perimeter = 0
        perimeter += self.__sides
        return perimeter

        # Метод set_sides(self, *new_sides) должен принимать новые стороны, если их количество не равно sides_count, то не изменять, в противном случае - менять.

    def set_sides(self, *__sides):
        def set_sides(self, __sides):
            if self.len(self.__sides) != len(__sides):
                __sides = self.__sides
            return self.__sides


# Метод get_volume, возвращает объём куба.
    def get_volume(self):
        v=0
        v = self.sides_count **3
        return v


Circle((200, 200, 100), 10, 15, 6) #, т.к. сторона у круга всего 1, то его стороны будут - [1]
#
Triangle((200, 200, 100), 10, 6)  #т.к. сторон у треугольника 3, то его стороны будут - [1, 1, 1]
Cube((200, 200, 100), 9)   #  , т.к. сторон(рёбер) у куба - 12, то его стороны будут - [9, 9, 9, ....., 9] (12)
#
Cube((200, 200, 100), 9, 12) #, т.к. сторон(рёбер) у куба - 12, то его стороны будут - [1, 1, 1, ....., 1]
# Код для проверки:
#
circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
#
cube1 = Cube((222, 35, 130), 6)
##
#Проверка на изменение цветов:
# #
# # circle1.set_color(55, 66, 77) # Изменится
# #
# # print(circle1.get_color())
# #
# # cube1.set_color(300, 70, 15) # Не изменится
# #
# # print(cube1.get_color())
# # #
# # Проверка на изменение сторон:
# #
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
# #
print(cube1.get_sides())
# #
# # circle1.set_sides(15) # Изменится
# #
# # print(circle1.get_sides())

print(len(circle1)) # Проверка периметра (круга), это и есть длина:
print(cube1.get_volume()) # Проверка объёма (куба):

