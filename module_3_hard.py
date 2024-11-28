data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])]

def calculate_structure_sum(*args: object) -> object:
    summa = 0
    for elements in args :
        if isinstance(elements,str):
            summa += len(elements)
        if isinstance(elements,int):
            summa += elements
        if isinstance(elements,(list, tuple, set)):
            for i in elements :
                summa += calculate_structure_sum (i)
        if isinstance(elements, dict):
            for key,value in elements.items():
                summa += calculate_structure_sum(key)
                summa += calculate_structure_sum(value)


    return summa

result = calculate_structure_sum(data_structure)
print(result)