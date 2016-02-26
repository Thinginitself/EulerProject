#Euler Project 97
#Thinginitself

div = 10 ** 10

res = 28433

for i in xrange(7830457):
	res *= 2
	res %= div

print res+1