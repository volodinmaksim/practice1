import math

def divider(n):
    array = []
    for i in range(3, n+1):   
        if n % i == 0:
            array.append(i)
    return array

def summ(arr):
    array = []
    for member in arr:
        for i in range(1, member//2 + 1):
            for j in range(member, member//2 , -1):
                if i + j == member:
                    array.append(str(i)+str(j))
    return array

for i in range(3,20+1):
    print(f'{i}:{summ(divider(i))}')
