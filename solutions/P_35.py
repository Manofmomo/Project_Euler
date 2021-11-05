from math import sqrt,ceil
check_till=1000000
primes=[2]
primes_mast_walle=[]
test=1
for num in range(3,check_till,2):
    Handle=True
    for i in range(2,ceil(sqrt(num))+1):
        if num%i==0:
            Handle=False
            break
    if Handle:
        print(num)
        primes.append(num)
print(primes[-1])
print("Lets check now")
for prime in primes:
    list_digits=[]
    for digit in str(prime):
        list_digits.append(digit)
    Handle=True
    for i in range(1,len(list_digits)):
        new_list=list_digits[i:len(list_digits)]+list_digits[0:i]
        if int(''.join(new_list)) not in primes:
            Handle=False
            break
    if Handle:
        print("mila reh",prime)
        primes_mast_walle.append(prime)

print("the number of such primes are",len(primes_mast_walle))
