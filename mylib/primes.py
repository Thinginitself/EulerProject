#It's a module about primes

import math

def primeList(n):
    mylist = []
    pl = [1] * (n+1)
    pl[0] = pl[1] = 0
    num = 2
    while num < n:
        mylist.append(num)
        x = num * num
        while x < n:
            pl[x] = 0
            x += num
        num += 1
        while not pl[num] and num<n:
            num += 1
    return mylist

def primeSet(n):
    mylist = set(primeList(n))
    return mylist

def isprime(n):
    if n < 2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
