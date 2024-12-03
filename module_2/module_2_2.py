# На вход программе подаются 3 целых числа и записываются в переменные first, second и third соответственно.
first = input("Введите первое число")
second = input("Введите второе число")
third = input("Введите третье число")

# Ваша задача написать условную конструкцию (из if, elif, else), которая выводит кол-во одинаковых чисел среди 3-х введённых.

if first == second and first == third:
        print (3)
elif first== second:
        print (2)
elif second == third:
        print(2)
elif first == third:
        print (2)
else:
        print (0)









