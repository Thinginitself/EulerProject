#Euler Project 90
#Thinginitself

from itertools import combinations

def check(a, b):
    check_01 = (0 in a and 1 in b) or (1 in a and 0 in b)
    check_04 = (0 in a and 4 in b) or (4 in a and 0 in b)
    check_09 = (0 in a and 9 in b) or (9 in a and 0 in b) or (0 in a and 6 in b) or (6 in a and 0 in b)
    check_16 = (1 in a and 6 in b) or (6 in a and 1 in b) or (1 in a and 9 in b) or (9 in a and 1 in b)
    check_25 = (2 in a and 5 in b) or (5 in a and 2 in b)
    check_36 = (3 in a and 6 in b) or (6 in a and 3 in b) or (3 in a and 9 in b) or (9 in a and 3 in b)
    check_49 = (4 in a and 9 in b) or (9 in a and 4 in b) or (4 in a and 6 in b) or (6 in a and 4 in b)
    check_81 = (8 in a and 1 in b) or (1 in a and 8 in b)
    return check_01 and check_04 and check_09 and check_16 and check_25 and check_36 and check_49 and check_81

def order(x):
    res = 0
    for i in x:
        res = res * 10 + i
    return res

def change(x):
    if 6 in x and 9 in x:
        return x
    if 6 in x:
        return (*x, 9)
    if 9 in x:
        return tuple(sorted((*x, 6)))
    return x

res = 0
for a in combinations(range(10), 6):
    for b in combinations(range(10), 6):
        a = change(a)
        b = change(b)
        oa = order(a)
        ob = order(b)
        if ob > oa:
            continue
        if check(a, b):
            res += 1
print(res)
