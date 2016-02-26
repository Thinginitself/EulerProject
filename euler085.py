#Euler Project 85
#Thinginitself

#c(n+1,2)*c(m+1,2) = n(n+1)m(m+1)/4 ~= 2 * 10 ** 6
#n(n+1)m(m+1) ~= 8 * 10 ** 6

goal = 8 * 10 ** 6
dif = 10 ** 2

ans = 0

for i in xrange(1,2000):
	for j in xrange(1,2000):
		tmp = i*(i+1)*j*(j+1)
		if abs(tmp-goal) < dif:
			dif = abs(tmp-goal)
			ans = i*j
			print i,j

print ans
