numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 307]
primes = []
not_primes = []

for i in range(len(numbers)):
    count_del = 0

    for j in range (1, numbers[i]+1):
        if numbers[i] % j == 0 :
            count_del += 1
        if count_del > 2:
            break

    if count_del <= 2:
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])

print(primes)
print(not_primes)



