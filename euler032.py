#Euler Project 32
#Thinginitself

res = 0

def ok(i,j,k):
	v = [0] * 10
	while i > 0:
		v[i%10] += 1
		i /= 10
	while j > 0:
		v[j%10] += 1
		j /= 10
	while k > 0:
		v[k%10] += 1
		k /= 10
	if v[0] != 0:
		return False 
	for l in xrange(1,10):
		if v[l] != 1:
			return False
	return True
prods=set()
for i in xrange(10,100):
	for j in xrange(100,1000):
		k = i * j
		if ok(i,j,k):
			print i, j, k
			prods.add(k)
for i in xrange(1,10):
	for j in xrange(1000,10000):
		k = i * j
		if ok(i,j,k):
			print i,j,k
			prods.add(k)

print sum(list(prods))
