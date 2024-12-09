# def example_function():
#     local_var = "I am local"
#     print(local_var)
#
# example_function()
# # print(local_var)  # Ошибка! Переменная вне области видимости
#
# global_var = "I am global"
#
# def example_function():
#     print(global_var)  # Доступ к глобальной переменной
#
# example_function()
#
# count = 0
#
# def increment():
#     global count  # Указываем, что изменяем глобальную переменную
#     count += 1
#
# increment()
# increment()
# increment()
# print(count)  # Вывод: 1
#
# def outer_function():
#     enclosing_var = "I am enclosing"
#
#     def inner_function():
#         print(enclosing_var)  # Доступ к переменной внешней функции
#
#     inner_function()
#
# outer_function()
#
# print(len([1, 2, 3]))

x = "global"

def example_function():
    x = "local"  # Локальная переменная, не влияет на глобальную
    print(x)

example_function()  # Вывод: local
print(x)  # Вывод: global

x = 10

def check_namespaces():
    y = 20
    print("Локальные переменные:", locals())  # {'y': 20}
    print("Глобальные переменные:", globals())  # {'x': 10, ...}

check_namespaces()