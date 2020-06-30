CHECK_WITH = list('123456789')

def checkdigit(num1,num2):
    num3=num1*num2
    digitaye=list(str(num1)+str(num2)+str(num3))
    digitaye.sort()
    if digitaye == CHECK_WITH:
        return True
    else:
        return False

print(checkdigit(39, 186))
set_final=set()
for i in range(2,100):
    for j in range(100,10000):
        if checkdigit(i,j):
            set_final.add(int(i*j))
#
for i in range(10,100):
    for j in range(100,1000):
        if checkdigit(i,j):
            set_final.add(int(i*j))
print(sum(set_final))
if 7254 in set_final:
    print("oho")
