#Euler Project 24
#Thinginitself
#ugly code

x = 1000000 - 1
num = 10

fac = [1]
for i in xrange (2,num+1):
	fac.append(fac[i-2]*i)

print fac
chosen = [0] * (num+1)
res = []


for item in range(num-1)[::-1]:
	k = x / fac[item]
	x = x % fac[item]
	res.append(k)

print res

for i in xrange(num-1):
	p = 0
	while chosen[p] != 0:
		p += 1
	for j in xrange(res[i]):
		p += 1
		while chosen[p] != 0:
			p += 1
	chosen[p] = 1
	print p,

p = 0
while chosen[p] != 0:
	p += 1
print p
