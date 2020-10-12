#Euler Project 66
#Thinginitself

#pell equation

from fractions import Fraction
import math

def gen_continued_fraction(N):
    r = int(math.sqrt(N))
    if r*r == N:
        return []
    a = [r]
    p = [0]
    q = [1]
    for i in range(N+1):
        p.append(a[i]*q[i]-p[i])
        q.append((N-p[i+1]*p[i+1])//q[i])
        if i>0 and p[i+1] == p[1] and q[i+1] == q[1]:
            break
        a.append(int((p[i+1]+math.sqrt(N))//q[i+1]))
    return a

def gen_fraction_by_list(a):
    res = Fraction(0)
    for i in a[-2::-1]:
        if res == 0:
            res = i + res
        else:
            res = i + 1 / res
    return res

def find_p(N):
    c_list = gen_continued_fraction(N)
    if len(c_list) == 0:
        return -1
    fra = gen_fraction_by_list(c_list)
    p = fra.numerator
    if len(c_list) % 2 == 1:
        return p
    else:
        return 2*p*p + 1

max_p = 0
max_n = 0

for n in range(2,1001):
    p = find_p(n)
    if p > max_p:
        max_p = p
        max_n = n

print(max_n, max_p)