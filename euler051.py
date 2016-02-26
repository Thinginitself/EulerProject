#Euler Project 51
#Thinginitself

from mylib import primes

tmp = primes.primeList(10 ** 6)

myset = set(tmp)

def int2list(n):
	mylist = []
	while n > 0:
		mylist.append(n%10)
		n /= 10
	return mylist

def list2int(l):
	myint = 0
	for i in l[::-1]:
		myint *= 10
		myint += i
	return myint

def test(l,k):
	if not k in set(l):
		return 
	num = 0
	length= len(l)
	for i in xrange(10):
		new = l[:]
		for j in xrange(length):
			if new[j]==k:
				new[j] = i
		if new[length-1] == 0:
			continue
		if list2int(new) in myset:
			num += 1
	if num > 7:
		return True
	return False


for i in tmp:
	mylist = int2list(i)
	if test(mylist,0):
		print i 
		break
	if test(mylist,1):
		print i 
		break
	if test(mylist,2):
		print i 
		break