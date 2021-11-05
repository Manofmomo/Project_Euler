multiple_3=[]
multiple_5=[]
for num in range(1000):
    if num%3==0:
        multiple_3.append(num)
    if num%5 == 0:
        multiple_5.append(num)
multiple_3_set = set(multiple_3)
multiple_5_set = set(multiple_5)

final_set = multiple_3_set.union(multiple_5_set)
final_list = list(final_set)
