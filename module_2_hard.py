import random

from random import randrange
n = randrange(3,20,1)
spin = []
for i in (range(1,n-1)):
    for j in range(i+1,n):
        if n<=j:
            continue
        s = i+ j
        if n%s == 0:
            spin.append(str(i))
            spin.append(str(j))
        else:
            continue

result = "".join(spin)
print (f'{n}-{result}')



