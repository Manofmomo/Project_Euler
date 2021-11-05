
res=["1","2","1","1"]
index=10**12
for _ in range(index-4):
    n=''.join(res) # 111211
    res = []
    temp = n #111211
    count = 0
    for i in range(len(temp)-1): #4
        if temp[i] == temp[i+1]:
            count += 1
        else:
            res.append(str(count+1))
            res.append(str(temp[i]))
            if i == len(temp)-2:
                res.append(str(1))
                res.append(str(temp[i+1]))
            count = 0
    if count != 0:
        res.append(str(count+1))
        res.append(str(temp[len(temp)-1]))
final=''.join(res)
print(final)
a=final.count('1')%(2**30)
c=final.count('3')%(2**30)
b=final.count('2')%(2**30)
print(a,b,c,sep=",")
