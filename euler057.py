#Euler Project 57
#Thinginitself

from fractions import Fraction

n = Fraction(3,2)

count = 0
for i in xrange(1000):
	n = 1 + 1/ (1+n)
	ln = len(str(n.numerator))
	ld = len(str(n.denominator))
	if ln > ld:
		count += 1

print count