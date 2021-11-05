from math import sqrt
max = 0

count = 0
j=1
while count != 10002:
    is_prime = True
    for m in range(2, j):
        if j % m == 0:
            is_prime = False
            break
    if is_prime:
        count += 1
    j=j+1
print(j-1)
