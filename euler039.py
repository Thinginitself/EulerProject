#Euler Project 39
#Thinginitself
res = 0
myp = 0
for p in xrange(12,1000):
	ans = 0
	for x in xrange(7,p):
		if (p-x) * (p-x) % x != 0:
			continue
		z = (p-x)*(p-x) / x
		if (z + x) % 2 == 0:
			ans += 1
	if ans > res:
		res = ans
		myp = p
print res,myp