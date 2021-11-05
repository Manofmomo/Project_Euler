from math import sqrt
num=int(10000)
list_checked=[]

for nummu in range(3,num):
    n=nummu
    if nummu in list_checked:
        continue
    i=int(2)
    squareroot=sqrt(n)
    sum=int(1)

    while i < squareroot:
        if n%i == 0:
            sum += i + n/i
        i+=1

    if squareroot%1 ==0:
        sum += squareroot
    if n == sum:
        continue
    n=sum
    i=int(2)
    squareroot=sqrt(n)
    sum1=int(1)

    while i < squareroot:
        if n%i == 0:
            sum1 += i + n/i
        i+=1

    if squareroot%1 ==0:
        sum1 += squareroot
    if sum1==nummu:
        list_checked.append(int(sum1))
        list_checked.append(int(sum))
sum=int(0)
print(list_checked)
for i in list_checked:
    sum+=i
print(sum)
