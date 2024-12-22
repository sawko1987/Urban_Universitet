# Вам __color=Noneоздать 2 класса: Vehicle и Sedan
# где Vehicle - это любой транспорт
#Каждый объект Vehicle должен содержать следующие атрибуты объекта:
#Атрибут owner(str) - владелец транспорта. (владелец может меняться)
#Атрибут __model(str) - модель (марка) транспорта. (мы не можем менять название модели)
#Атрибут __engine_power(int) - мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)
#Атрибут __color(str) - название цвета. (мы не можем менять цвет автомобиля своими руками)
#Атрибут класса __COLOR_VARIANTS, в который записан список допустимых цветов для окрашивания. (Цвета написать свои)

class Vehicle:
    __COLOR_VARIANTS = ["green", "blue", "red", "black"]
    def __init__ (self, owner, __model,__color,__engine_power,) :
        self.owner = str(owner)
        self.__model = str(__model)
        self.__engine_power = int(__engine_power)
        self.__color = str(__color)
        
# Метод get_model - возвращает строку: "Модель: <название модели транспорта>
    def get_model(self):
        return f"Модель: {self.__model}"

# Метод get_horsepower - возвращает строку: "Мощность двигателя: <мощность>"
    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

# Метод get_color - возвращает строку: "Цвет: <цвет транспорта>"
    def get_color(self):
        return f" Текущий цвет: {self.__color}"

#Метод print_info - распечатывает результаты методов (в том же порядке): get_model, get_horsepower, get_color;
                    # а так же владельца в конце в формате "Владелец: <имя>"
    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

#Метод set_color - принимает аргумент new_color(str), меняет цвет __color на new_color, если он есть в списке __COLOR_VARIANTS, в противном случае выводит на экран надпись: "Нельзя сменить цвет на <новый цвет>".
#Взаимосвязь методов и скрытых атрибутов:
    def set_color(self, new_color = str(None)):
        for color in self.__COLOR_VARIANTS:
            if new_color.lower() in color.lower():
                self.__color = color
                print(f"Цвет автомобиля изменился на {new_color} ")
            else:
                print(f"Нельзя сменить цвет {self.__color} на {new_color}")


#Sedan(седан) - наследник класса Vehicle.
#Класс Sedan наследуется от класса Vehicle, а так же содержит следующие атрибуты:
#Атрибут __PASSENGERS_LIMIT = 5(в седан может поместиться только 5 пассажиров)

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства

vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)

vehicle1.set_color('Pink')

vehicle1.set_color('BLACK')

vehicle1.owner = 'Vasyok'

# Проверяем что поменялось

vehicle1.print_info()

