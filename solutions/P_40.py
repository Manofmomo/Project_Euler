num=10
current_digit=0
alternate_digit=0
check=2
productt=1
while check<7:
    for i in range(0,10):
        current_digit=alternate_digit
        num+=len(str(current_digit))

        if num==10**check:
            check+=1
            print("The",10**check,"is",current_digit)
            productt*=current_digit
        current_digit=i
        num+=len(str(current_digit))

        if num==10**check:
            check+=1
            print("The",10**check,"is",current_digit)
            productt*=current_digit

    alternate_digit+=1

print(productt)
