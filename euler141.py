#Euler Project 141
#Thinginitself

# a*b^3*x^2 + a^2*x = m^2 (a < b < m)

import math

MAX_NUM = 10 ** 12


def is_sqaure(x):
    a = int(math.sqrt(x))
    return a*a == x

max_b = int(MAX_NUM ** (1/3))

total = 0
used = set()

for b in range(2, max_b+1):
    max_x = int(math.sqrt(MAX_NUM/(b**3)))
    for x in range(1, max_x+1):
        tmp_max_a = int(MAX_NUM/(b**3)/(x*x))
        max_a = min(b-1, tmp_max_a)
        for a in range(1, max_a+1):
            res = a * b**3 * x*x + a*a*x
            if res > MAX_NUM or res in used:
                continue
            used.add(res)
            if is_sqaure(res):
                total += res
                print(a, b, x, res)
print(total)
