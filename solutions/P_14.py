li=[]
print("hello")
for i in range(2, 1000000):
    n=i
    count=0
    while n!=1:
        if n%2==0:
            n=n/2
        else:
            n=3*n+1
        count+=1
    li.append(count)

print(li.index(max(li))+1)
