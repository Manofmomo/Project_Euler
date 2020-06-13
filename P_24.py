from math import factorial
list_num=[]
kewl = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
n=9
summu=0
copy=0
count=0
while n>-1:
    copy=summu
    summu += factorial(n)
    count+=1
    print(count)
    if summu >=1000000:
        summu=copy
        n=n-1
        count=count-1
        kewllu=kewl[count]
        list_num.append(str(kewllu))
        kewl.remove(kewllu)

        count=0
    if count >9:
        break
num=''.join(list_num)
print(num)

# 2783915460
