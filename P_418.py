
for c in range(1,n):
    for b in range(1,c):
        for a in range(1,b):
            if a*b*c == n:
                if c/a < min:
                    min = c/a
                    minsum = a+b+c
                    print(minsum)
                break

2
