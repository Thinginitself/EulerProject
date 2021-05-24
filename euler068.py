#Euler Project 68
#Thinginitself

from itertools import permutations
num = 0
res = []
for x in permutations(range(1,11)):
    flag = True
    if (x[0] > x[3]) or (x[0] > x[5]) or (x[0] > x[7]) or (x[0] > x[9]):
        continue
    num = x[0] + x[1] + x[2]
    for k in range(0, 8, 2):
        if x[k] + x[k+1] + x[k+2] != num:
            flag = False
            break
    if x[1] + x[8] + x[9] != num:
        flag = False
    if flag:
        x = [str(k) for k in x]
        tmp = \
            x[0] + x[1] + x[2] + \
            x[3] + x[2] + x[4] + \
            x[5] + x[4] + x[6] + \
            x[7] + x[6] + x[8] + \
            x[9] + x[8] + x[1]
        if len(tmp) == 16:
            res.append(tmp)
print(max(res))
