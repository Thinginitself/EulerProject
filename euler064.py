#Euler Project 141
#Thinginitself

import math

def gen_continued_fraction(N):
    r = int(math.sqrt(N))
    if r*r == N:
        return False
    a = [r]
    p = [0]
    q = [1]
    for i in range(N+1):
        p.append(a[i]*q[i]-p[i])
        q.append((N-p[i+1]*p[i+1])//q[i])
        if i>0 and p[i+1] == p[1] and q[i+1] == q[1]:
            break
        a.append(int((p[i+1]+math.sqrt(N))//q[i+1]))

    return len(a) % 2 == 0

res = 0

for i in range(2, 10001):
    if gen_continued_fraction(i):
        res += 1

print(res)