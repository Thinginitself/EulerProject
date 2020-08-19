from mylib import primes

def root_of_ten(n):
    x = 1
    for i in range(1, n):
        x *= 10
        x %= n
        if x == 1:
            return i
    return n-1

def is_ok(l, k):
    r = root_of_ten(k)
    return  l % r == 0


N = 10 ** 9

pl = primes.primeList(10000000)


res = 0
t = 0
for i in pl:
    if i > 5:
        if is_ok(N, i):
            res += i
            t += 1
            print(i, t)
            if t == 40:
                break
print("=======", res)
