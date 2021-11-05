from math import log,floor
def numtobinary(num):
    check=2**floor(log(num,2))
    binary=""
    copy=num
    while check>=1:
        if num>=check:
            binary+="1"
            num=num-check
        else:
            binary+="0"
        check=check/2
    if binary==binary[::-1]:
        return True
    else:
        return False
final_set=set()
for i in range(1,1000001):
    i=str(i)
    if i==i[::-1]:
        if numtobinary(int(i)):
            final_set.add(int(i))
            print("Yo number mila reh",i)

print(sum(final_set))
