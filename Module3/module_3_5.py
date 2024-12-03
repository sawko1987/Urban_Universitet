# def get_multiplied_digits(number):
#     str_number = str(number)
#     first = int(list(str_number)[0])
#
#     if len(str_number)<=1:
#         return first
#     else:
#         return first * get_multiplied_digits(int(str_number[1:]))
#
#
#
#
#
# result = get_multiplied_digits(40203)
#
# # print(result)
#
# Добрый день!
#
# В коде ошибка.
#
# Она возникает при наличии цифры 0 в числе.
#
# При умножении на 0 результат всего произведения становится 0. Чтобы исправить это, нужно игнорировать цифру 0.
#
# Вот исправленный код:

def get_multiplied_digits(number):

    str_number = str(number)

    first = int(str_number[0])

    if len(str_number) > 1:

    if first != 0:

        return first * get_multiplied_digits(int(str_number[1:]))

    else:

        return get_multiplied_digits(int(str_number[1:]))

    else:

        return first if first != 0 else 1



result = get_multiplied_digits(40203)

print(result) # 24

result2 = get_multiplied_digits(402030)

print(result2) # 24

