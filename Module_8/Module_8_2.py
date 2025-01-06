def personal_sum(numbers):
    result =  0
    incorrect_data = 0
    sum_elem = 0
    for number in numbers:
        sum_elem+=1
        try:
            result += number
        except TypeError as exc:
            print(f'Некорректный тип данных для подсчета суммы - {number}')
            incorrect_data +=1
    return (result,incorrect_data)

def calculate_average(numbers):
    try:
        total = personal_sum(numbers)
        sr_arifmetiv = total[0] / len(numbers)
        return sr_arifmetiv
    except ZeroDivisionError as exc2:
        return 0
    except TypeError as exc3:
        print(f'В numbers записан некорректный тип данных')
        return None



print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать


