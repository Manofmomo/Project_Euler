from math import sqrt
max = 0
big_num=600851475143
i = big_num
primes = []

j= 2
while i != 1 and j < big_num:
    is_prime = True
    for m in range(2, int(sqrt(j))):
        if j % m == 0:
            is_prime = False
            break
    if is_prime:
        while i % j ==0:
            i =i/j
            primes.append(j)
    j=j+1
print(primes[-1])
