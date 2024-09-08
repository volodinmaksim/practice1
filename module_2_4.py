import math
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for i in range(1, len(numbers)):
    is_prime = True

    for j in range (1, math.ceil(math.sqrt(numbers[i]))+1):
        if numbers[i] % numbers[j] == 0 and numbers[j]!= numbers[i]:
            is_prime = False

    if is_prime:
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])


print(primes)
print(not_primes)



