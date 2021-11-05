# hi
# 20 left 20 down
# l,d,l,d
# 40!/20!20!
from math import factorial
def cool(n):
    num = factorial(2 * n) /(factorial(n) * factorial(n))
    print(num)

cool(2)
