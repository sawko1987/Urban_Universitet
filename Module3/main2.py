data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])]


summa = [0]
while len (data_structure) > 0:
    if isinstance (data_structure[0], list):
        summa.append(sum(data_structure.pop(0)))
    else:
        if isinstance(data_structure[0], dict):
            summa.append(len(list(data_structure[0])))
            summa.append(sum(list(data_structure[0].values())))
            data_structure.pop(0)
        else:
            if isinstance(data_structure[0], tuple):
                summa.append()












print(summa)