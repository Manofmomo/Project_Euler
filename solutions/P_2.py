a = 0
b = 1
sum = 0
while (b < 4000000):
    a = a + b
    b = a + b
    if a % 2 == 0:
        sum = sum + a
    if b % 2 == 0:
        sum = sum + b
print(sum)
