numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for index, element in enumerate(numbers):
    if element < 2:
        continue
    is_prime = True
    for div in range(2,element):
        if element % div ==0:
            not_primes.append(element)
            is_prime = False
            break
    if is_prime:
        primes.append(element)
print(primes)
print(not_primes)
