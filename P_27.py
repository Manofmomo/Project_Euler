from math import sqrt,ceil
num=1000*1000
primes=[]
for i in range(2,num):
    flag =0
    for j in range(2,ceil(sqrt(i))):
        if i%j ==0:
            flag=1
            break
    if flag==0:
        primes.append(i)
maxlist=[0,0,0]


print(len(primes))
n=39
list_suspects=[]

for b in primes[0:180]:
    for prime in primes:
        a=(prime-b-n*n)/n
        if a<-1000:
            continue

        if a%1==0:
            list_suspects.append([a,b])
        if a>1000:
            break

if [1,41] in list_suspects:
    print("list seems good")
else:
    exit()
Handle=False

n=1
while not Handle:
    print("n is:",n," and range is",len(list_suspects))
    for a,b in list_suspects:
        if  (n*n + a*n + b) not in primes:
            list_suspects.remove([a,b])

    if len(list_suspects)==1:
        Handle=True
        break

    n+=1
print(list_suspects)
print(list_suspects[0][0]*list_suspects[0][1])
