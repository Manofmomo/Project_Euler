griddu=1001
list_numre=[i for i in range(1,griddu*griddu+1)]
gap=1
index=0
count=0
summu=0
while index<(griddu*griddu):
    # print(index)
    summu+=list_numre[index]
    count+=1
    index+=gap+1
    if count==4:
        count=0
        gap=gap+2


print(summu)
