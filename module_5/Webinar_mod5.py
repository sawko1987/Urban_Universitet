# class Person:
#     # Конструктор: задаёт начальные значения свойств
#     def __init__(self, name, age):
#         self.name = name  # Свойство "имя"
#         self.age = age    # Свойство "возраст"
#
#     # Метод: описывает поведение объекта
#     def greet(self):
#         print(f"Привет, меня зовут {self.name}, мне {self.age} лет.")
#
#     def set_age(self, new_age):
#         self.age = new_age  # Изменение возраста
#
# class Animal:
#     def __init__(self, name, species, sound):
#         self.name = name       # Имя
#         self.species = species # Вид
#         self.sound = sound     # Звук
#
#     def make_sound(self):
#         print(f"{self.name} издаёт звук: {self.sound}")
#
#
# cat = Animal("Барсик", "Кот", "Мяу")
# dog = Animal("Шарик", "Собака", "Гав")
#
# cat.make_sound()  # Барсик издаёт звук: Мяу
# dog.make_sound()  # Шарик издаёт звук: Гав





# Создаём объект класса Person
# person1 = Person("Иван", 25)
# person2 = Person("Мария", 30)
#
# # Вызываем метод объекта
# person1.greet()  # Привет, меня зовут Иван, мне 25 лет.
# person2.greet()  # Привет, меня зовут Мария, мне 30 лет.print(person1.name)  # Иван
#
# print(person1.name)  # Иван
# print(person2.age)   # 30
#
# # Создаём объект
# person = Person("Анна", 20)
#
# # Изменяем возраст
# person.set_age(21)
# print(person.age)  # 21
# person1.set_age(35)
# print(person1.age)


class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls)
        cls.houses_history.append(args[0])
        return obj

    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("Такого этажа не существует")

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __len__(self):
        return self.number_of_floors

    def __add__(self, other):
        if isinstance(other, House):
            self.number_of_floors += other.number_of_floors
        elif isinstance(other, int):
            self.number_of_floors += other
        return self


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)



# h1.go_to(5)
# h2.go_to(10)

# print(h1)
# print(h2)
# print(len(h1))
print(House.houses_history)