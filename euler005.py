#Euler Project 5
#Thinginitself

def gdb( x, y):
	if x < y:
		x = x ^ y
		y = x ^ y
		x = x ^ y
	if x % y == 0:
		return y
	return gdb( y, x%y)

n = input()
x = 1
for i in xrange(1,n+1):
	x = x * i / gdb(x,i)
print x
