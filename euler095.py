
from mylib.primes import primeList


NUM = 1000000

prmie_list = primeList(1000)

print(len(prmie_list))

def aliquot_sum(number):
    x = number
    res = 1
    for p in prmie_list:
        factor = 0
        while x % p == 0:
            x = x // p
            factor += 1
        if factor > 1:
            res *= (p ** (factor + 1) - 1) // (p - 1)
        elif factor == 1:
            res *= p + 1
        if x == 1:
            break
    if x!= 1:
        res *= (x+1)
    return res - number

next_one = [0, 0] + [aliquot_sum(i) for i in range(2, NUM+1)]

