from math import sqrt, ceil
list_adbundant = []
num = int(0)
for num in range(3,28123):
    i = int(2)
    addition = int(1)
    squareroot = sqrt(num)
    while i < ceil(squareroot):
        if num % i == 0:
            addition += i + (num / i)
        i+=1
    if squareroot % 1 == 0:
        addition += squareroot

    if addition > num:
        list_adbundant.append(num)

list_sum = []
for i in range(1,28124):
    flag = 0
    for check in list_adbundant:
        if check > i:
            break
        if (i - check) in list_adbundant:
            flag = 1
            break
    if flag == 0:
        list_sum.append(int(i))
print(sum(list_sum))
4179871
