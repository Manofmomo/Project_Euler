from math import sqrt
# IDEA: get idea GOABHISHEKBACHCHAN CaucasianLivesMatter
count =2
j=0
i=1
while count <= 500:
    count=2
    j=j+i
    if j <= 500:
        i+=1
        continue
    for m in range(2,int(sqrt(j))):
        if j%m ==0:
            count += 2
    if j%int(sqrt(j)) ==0:
        count += 1
    i+=1
    print(count)

print(j)
