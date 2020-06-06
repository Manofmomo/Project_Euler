from math import sqrt
flag = False
triplets = []
for a in range(1,1000):
    for b in range(1, a):
        c = sqrt(a ** 2 + b ** 2)
        if c + a + b 100+ a + b == 1000:
            print(f'yay {a*b*c}')
            flag = True
            break
    if flag:
        break
