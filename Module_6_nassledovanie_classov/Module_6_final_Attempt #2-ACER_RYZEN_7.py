class Figure:
    sides_count = 0

    def __init__(self,color,*sides, filed:bool ):
        self.__color = color
        self.__sides = sides
        self.filled = filed


    def get_color(self):
        return self.__color

    def __is_valid_color(self,r,g,b):
        """
        принимает параметры r, g, b, который проверяет корректность переданных значений перед
        установкой нового цвета. Корректным цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255
        (включительно).
        """
        if isinstance(r,int) and isinstance(g,int) and isinstance(b,int):
            if r > 0 and r <= 255 and g > 0 and g <= 255 and b > 0 and b <= 255:
                return True
        else:
            return "цвет остается прежним"


    def set_color(self,r,g,b):
        """
        Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие
        значения, предварительно проверив их на корректность. Если введены некорректные данные,
         то цвет остаётся прежним.
        """
        if self.__is_valid_color:
            self.__color = (r,g,b)


    def __is_valid_sides(self,*sid_count):
        """
        Принимает неограниченное кол-во сторон, возвращает True если все стороны целые положительные числа и кол-во новых сторон совпадает с
        текущим, False - во всех остальных случаях.
        """
        if isinstance(sid_count,int):
            if len(sid_count) == self.sides_count:
                for side in sid_count:
                    if side > 0:
                        return True
        else:
            return False
    def get_sides(self):
        """
        Возвращает значение атрибуда __sides
        """
        return self.__sides

    def __len__(self):
        "Должен возвращать периметр фигуры (длина сторон)"
        return self.sides_count

    def set_sides(self, *new_sides):
        """
        Должен принимать новые стороны, если их количество не равно sides_count,
         то не изменять, в противном случае - менять.
        """
        if len(new_sides) != self.sides_count:
            self.sides_count = len(new_sides)
        return self.sides_count


class Circle(Figure):
    sides_count = 1

    def __init__(self, *__radius):
        """
        рассчитать исходя из длины окружности (одной единственной стороны).
        """
        self.__radius = self.sides_count *(2*3.14)


    def get_square(self):
        """
        возвращает площадь круга (можно рассчитать как через длину, так и через радиус).
        """
        return 3.14*(self.__radius**2)

class Triangle(Figure):
    sides_count = 3
    def __init__(self,__sides):
        self.__sides = __sides


    def get_square(self,a,b,c):
        """
        возвращает площадь треугольника
        """
        p = sum(self.__sides)/2
        s = (p*(p-a)*(p-b)*(p-c))**0.5
        return s


class Cube(Figure):
    sides_count = 12
    def __init__(self,color,*__sides):
        self.__sides = __sides
        self.color = color

    def get_volume(self):
        """
        Возвращает объем куба
        """
        return self.__sides**3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())


