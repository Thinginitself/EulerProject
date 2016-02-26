#Euler Project 92
#Thinginitself

f = [0] * (10 ** 8)
f[1] = 1
f[89] = 89

def next(n):
	res = 0
	while n > 0:
		z = n % 10
		n /= 10
		res += z * z
	return res


for i in xrange(2,10**7):
	chainlen = 0
	n = i
	while not f[n]:
		 n = next(n)
	x = f[n]
	n = i
	while not f[n]:
		f[n] = x
		n = next(n)
	if i%10000==0:
		print i

count = 0
for i in f:
	if i == 89:
		count += 1
print count

