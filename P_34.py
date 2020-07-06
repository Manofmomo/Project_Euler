from math import factorial
def fact_digit(num):
    summu=0
    for i in str(num):
        summu+=factorial(int(i))

    if summu==num:
        return True
    else:
        return False
sum_final=set()
for digit in range(10,10000000):
    if factorial(9)*len(str(digit))<digit:
        print(digit," ke baad nahi karna")
        break
    if fact_digit(digit):
        print(digit)
        sum_final.add(digit)

print(sum(sum_final))
