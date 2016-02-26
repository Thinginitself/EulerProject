#Euler Project 493
#Thinginitself

#7*10 balls, pick 20 of them
from __future__ import division

dec = 161884603662657900
res = 0
s = [0,0,0,0,0,0,0,0]
z = 0

def fac(n):
	res = 1
	for i in xrange(1,n+1):
		res *= i
	return res

def kinds():
	res = 1
	for j in xrange(1,8):
		c = s[j]
		for i in xrange(c):
			res *= 10-i
			res /= i+1
	return res

def dfs(k,color,ball):
	global res,z
	if k==7:
		if ball>10:
			return 
		s[k] = ball
		if ball!=0:
			color += 1
		tmp = kinds()
		z += tmp
		res += color*tmp
		return 
	mymax = min(10,ball)
	for i in xrange(1,mymax+1):
		s[k] = i
		dfs(k+1,color+1,ball-i)
	s[k] = 0
	dfs(k+1,color,ball)

dfs(1,0,20)

print res/z



#this method is interesting
#writer: tehsp
def solve(colors, balls, expected):
    if balls == 50 or colors == 7:
        return expected * colors
    return solve(colors + 1, balls - 1, expected * ((7 - colors) * 10 / balls)) \
         + solve(colors, balls - 1, expected * ((balls - (7 - colors) * 10) / balls))

print solve(1, 69, 1)


#res = (1-c(60,20)/c(70,20))*7