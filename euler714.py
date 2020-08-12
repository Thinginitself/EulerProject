#Euler Project 714
#Thinginitself
#not a good way

from itertools import product


def listToNum(s):
    res = 0
    for c in s:
        res *= 10
        res += c
    return res

def genDuoDigits():
    res = []
    for i in range(1,10):
            for l in range(1, 21):
                for k in product((i,0), repeat=l):
                    res.append(listToNum(k)*10)
    res = list(set(res))
    res = sorted(res)
    return res

r = genDuoDigits()

print("finish duo!")
print(len(r))

res = 97523234075736996

last = [8910
, 9890
, 17820
, 19780
, 20410
, 26730
, 29670
, 32290
, 32570
, 34130
, 35640
, 39530
, 39560
, 40820
, 43270
, 44550
, 44710
, 45190
, 47090
, 49450]
for i in last:
    flag = False
    for k in r:
        if k > 0:
            if k % i == 0:
                res += k
                flag = True
                break
    if not flag:
        print("bad", i)

print(res)
        