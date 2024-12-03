from fake_math import divide as fm
from true_math import divide as tm
import Hello as hl
from paket import add, subtract
from paket.paket_2.file_1 import area as circle_area
from paket.paket_2.file_2 import area as rectangle_area
import tutur_name

print(tutur_name.greet())


print (circle_area(5))
print(rectangle_area(5, 6))


print(add(10,5))
print(subtract(10,5))
print(hl.greet("Alex"))
print(hl.PI)

result1 = fm(69, 3)
result2 = fm(3, 0)
result3 = tm(49, 7)
result4 = tm(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)