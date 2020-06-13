from math import sqrt
list_adbundant=[]
num=int(0)
for num in range(3,28123):
    i=int(2)
    sum=int(1)
    squareroot=sqrt(num)
    while i<squareroot:
        if num%i==0:
            sum+= i + num/i
        i+=1
        if squareroot%1==0:
            sum+=squareroot

    if sum>num:
        list_adbundant.append(num)
list_sum=[]
for i in range(1,28123):
    print(i)
    flag =0
    for check in list_adbundant:
        if check>i:
            break
        if (i - check) in list_adbundant:
            flag=1
            break
    if flag == 0:
        list_sum.append(i)
print(sum(list_sum))
