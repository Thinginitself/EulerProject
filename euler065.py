#Euler Project 65
#Thinginitself

from fractions import Fraction 

res = Fraction(0)

for i in range(1,34)[::-1]:
	res = 1 / (1 + res)
	res = 1 / (2 * i + res)
	res = 1 / (1 + res)

res += 2

print sum(map(int,list(str(res.numerator))))