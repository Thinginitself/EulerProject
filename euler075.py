#Euler Project 75
#Thinginitself

# a^2 + b^2 = c^2
# a = l * (m^2 - n^2)
# b = l * (2 * m * n)
# c = l * (m^2 + n^2)

import math
MAXN = 1500000
good = [0 for i in range(MAXN)]
max_m = int(math.sqrt(MAXN/2))
for m in range(2, max_m+1):
    max_n = int((MAXN-m*m*2)/2/m)
    for n in range(1, min(max_n,m)+1):
        a = m*m-n*n
        b = 2*m*n
        if math.gcd(a,b) != 1:
            continue
        tmp = 2*m*m + 2*m*n
        max_l = int(MAXN/tmp)
        for l in range(1, max_l+1):
            res = tmp*l
            if res < MAXN:
                good[res] += 1

res = len([x for x in good if x == 1])
print(res)