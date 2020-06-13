a=1
b=1

handle = False
count = 2
while not handle:
    a=a+b
    count+=1

    print("-")
    if len(str(a)) ==  1000:
        handle = True
        print(count)
    b=a+b
    count+=1
    if len(str(b)) ==  1000:
        handle = True
        print(count)
