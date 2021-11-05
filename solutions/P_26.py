recurring = []
num2=10
num = 0
max=0
for num in range(1,1000):
    handle= False
    count=0
    num2=10
    recurring=[]
    while not handle:
        num2=num2%num
        count+=1
        if num2 in recurring:
            handle=True
            break
        recurring.append(num2)
        num2*=10
    if max < (count-recurring.index(num2)):
        max=num

print(max)
