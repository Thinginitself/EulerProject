#Euler Project 30
#Thinginitself


pos = 5

f = []

for i in xrange(10):
	f.append(i ** pos)
c = [0] * 10
res = 0
print f
def ok(x):
	v = [0] * 10
	while x > 0:
		v[x % 10] += 1
		x = x / 10
	for i in xrange(1,10):
		if v[i] != c[i]:
			return False
	return True

def dfs(k, last, mysum):
	if k == 0:
		if ok(mysum):
			print mysum
			global res
			res += mysum 
		return 

	for i in xrange(last+1):
		newsum = mysum + f[k] * i
		c[k] = i
		dfs(k-1, last-i, newsum)

dfs(9, pos+2, 0)
print res-1