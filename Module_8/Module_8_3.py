
class Car:
    def __init__(self, model:str,__vin:int, __numbers:str):
        self.model = model
        self.__is_valid_vin(__vin)
        self.__is_valid_numbers(__numbers)



    def __is_valid_vin(self, vin_number):
        if not isinstance (vin_number, int):
            raise IncorrectVinNumber ('Некорректный тип vin номер')
        elif 1000000>vin_number<9999999:
            raise IncorrectVinNumber ('Неверная длина номера')
        else:
            return True


    def  __is_valid_numbers(self, numbers):
        if isinstance (numbers, str) and len(numbers) == 6:
            return True
        else:
            raise IncorrectCarNumbers ('Некорректно введен гос. номер автомобиля')

class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message



try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')

