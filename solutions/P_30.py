list_five=[]
for i in range(2,1000000):
    summu=0
    for digit in list(str(i)):
        summu+=int(digit)**5
    if summu == i:
        list_five.append(i)
print(sum(list_five))
