#Euler Project 74
#Thinginitself


fac = [1]

for i in xrange(1,10):
	fac.append(fac[i-1]*i)

def mynext(n):
	res = 0
	while n>0:
		res += fac[n%10]
		n /= 10
	return res

def chainnum(n):
	res = 1
	myset = set()
	myset.add(n)
	tmp = mynext(n)
	while not (tmp in myset):
		res += 1
		myset.add(tmp)
		tmp = mynext(tmp)
	return res

res = 0
for i in xrange(1,10 ** 6):
	if chainnum(i) == 60:
		res += 1

print res