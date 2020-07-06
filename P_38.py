maxxu=0
for num in range(100,10000):
    Handle=True
    miniHandle=True
    i=2
    productt=str(num)
    while miniHandle:
        productt+=str(num*i)
        if len(productt)>=9:
            miniHandle=False
            break
        i+=1

    digitset=set()
    if len(productt)==9 and Handle:
        for digit in productt:
            digit=int(digit)
            if digit==0:
                Handle=False
                break
            digitset.add(digit)

    if len(digitset)==9:
        if int(productt)>maxxu:
            maxxu=int(productt)
print("max is",maxxu)
