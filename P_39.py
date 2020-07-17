from math import sqrt
maxxu=[0,0] #max , p

for p in range (1a,1000):
    count=0
    for a in range(1,p//2):
        for b in range(a,p//2):
            if (p-a-b)==sqrt(a**2+b**2):
                count+=1
    if maxxu[0]<count:
        print("new max is", p)
        maxxu=[count,p]

print(maxxu[1])
