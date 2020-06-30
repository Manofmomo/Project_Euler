def bad_maths(numerator,denominator):
    fraction = numerator / denominator
    numerator = str(numerator)
    denominator = str(denominator)
    numerator_set = set(numerator)
    denominator_set = set(denominator)
    common = numerator_set.intersection(denominator_set)
    if len(common) == 1 :
        for i in common:
            i=str(i)
        if i=='0':
            return False
        numerator = numerator.replace(str(i),'')
        denominator = denominator.replace(str(i),'')
        if len(numerator)*len(denominator)>0:
            if int(denominator)!=0:
                if int(numerator) / int(denominator) == fraction:
                    return True
    return False

set_final=set()
for i in range(2, 100):
    print("apan idhar hai",i)
    for j in range(1, i):
        if bad_maths(j,i):
            set_final.add((j,i))
print("idhar bhe aa gaya")
numerator=1
denominator=1
for i,j in set_final:
    numerator*=i
    denominator*=j
print(set_final)
i=2
print("so far so good")
while i<=numerator:
    if numerator%i==0 and denominator%i==0:
        print(i,"se kata be")
        numerator=numerator/i
        denominator=denominator/i
    else:
        i+=1

print(denominator)
44/48
