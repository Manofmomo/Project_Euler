from math import sqrt
res = 0
j=2
for j in range(2000000):
    is_prime = True
    for m in range(2, int(sqrt(j))+1):
        if j % m == 0:
            is_prime = False
            break
    if is_prime:
        res += j
    print(res)
