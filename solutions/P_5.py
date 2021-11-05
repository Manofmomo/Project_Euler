your_dict = {2 : 0 ,3 : 0 ,5 : 0,7 : 0,11 : 0,13 : 0,17:0,19 : 0 }
for num in range(1, 21):
    for prime_num, count in your_dict.items():
        check=0
        copy=num
        while copy % prime_num == 0:
            copy=copy/prime_num
            check=check+1
        if check > count:
            your_dict[prime_num] = check
product=1
for prime_num, count in your_dict.items():
    product=product*(prime_num ** count)

print(product)
