import math
def is_prime(func):
    """Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом и
    "Составное" в противном случае."""
    def wrapper(*args,**kwargs):
        result_sum = func(*args,**kwargs)
        if result_sum < 2:
            return result_sum
        for sum in range(2, math.isqrt(result_sum) + 1):
            if result_sum % sum == 0:
                return "Число является составным"
        return result_sum

    return wrapper


@is_prime
def sum_three(*args):
    """Функция, которая складывает 3 числа """
    return sum(args)



result = sum_three(2,3,6)
print(result)
