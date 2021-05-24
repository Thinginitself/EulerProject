#Euler Project 86
#Thinginitself

import math

num = 0
limit = 10 ** 6
M = 3000
for c in range(2, M+1):
    if num > limit:
        print(c-1)
        break
    for d in range(1, 2*c):
        ss = c * c + d * d
        tmp = int(math.sqrt(ss))
        if tmp*tmp == ss:
            max_b = min(c, d-1)
            min_b = (d+1) // 2
            num += max_b - min_b + 1
