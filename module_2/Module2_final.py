import random

ran_number = random.randrange(3,20,1)
print(ran_number)
spisok = []
for index, number in enumerate (range(1,20)):
    if ((index+1) + number) == ran_number and (ran_number % ((index+1)+ number)) :       
        spisok.append(index+1)
        spisok.append(number)
        continue
    if number > ran_number :
            break
    else:continue

print(spisok)






