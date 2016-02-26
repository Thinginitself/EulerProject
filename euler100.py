#Euler Project 100
#Thinginitself

#Pell Equation
#(2*u-1)^2 - 2*(2*v-1)^2 = -1
#u is number of dics, v is number of blue dics.

x = y = 1
BIG = 2 * (10 ** 12)

while x<BIG:
	newx = 3*x+4*y
	newy = 2*x+3*y
	x,y = newx,newy

print (y+1)/2