from math import sqrt,ceil
import time
def checkprime(num):
    Handle=True
    if num==1:
        return False
    for i in range(2,ceil(sqrt(num))+1):
        if num%i==0:
            Handle=False
            break

    return Handle

def leftprime(num):
    copystr=str(num)
    index=len(copystr)-1
    miniHandle=True
    while miniHandle and index>0:
        checkint=int(copystr[index:])
        if not checkprime(checkint):
            miniHandle=False
            break
        index+=-1

    return miniHandle


count=0
num=2
digit=1
primes=[2,3,5,7]
primes_add=[]
num_string=str(num)
list_final=set()
start=time.time()
final_primes=set()
while count<11 and digit <20:
    primes_add=[]
    print("digit:",digit)
    for prime in primes:
        for i in range(1,10):
            num=int(str(prime)+str(i))
            if checkprime(num):
                primes_add.append(num)
                if leftprime(num):
                    count+=1
                    print("found",count,"it is",num)
                    final_primes.add(num)

    digit+=1
    primes=primes_add

print(sum(final_primes))
