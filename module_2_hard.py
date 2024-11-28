import random

from random import randrange
ran_number = randrange(3,20,1)
spin = []
for number1 in (range(1,20)):
    for number2 in range(2,20):
        sum = (number1 + number2 )
        sum2 = (str(number2) + (str(number1 )))
        if sum2 in spin:
             continue
        if number1 == number2:
            continue
        if ran_number % sum==0:
            spin.append(str(number1) + str(number2))
        if sum >= ran_number:
            break
result = "".join(spin)
print (f'{ran_number}-{result}')


