from sortfunc import *

data1 = list(map(int, input("ВВедите число через пробел").split()))
data2 = list(map(int, input("ВВедите число через пробел").split()))
data3 = list(map(int, input("ВВедите число через пробел").split()))

buble_sort (data1)
selection_sort (data2)

print("Пузырьковая сортировка", data1)
print("Сортирвока выбором" , data2)