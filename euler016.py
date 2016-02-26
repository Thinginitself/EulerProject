#Euler Project 16
#Thinginitself
#naive method

x =  2 ** 1000

res = 0
while x > 0:
	res +=  x % 10
	x /= 10
print res