#Euler Project 78
#Thinginitself


#Read the wiki of Partition 
#and "The Pentagonal Number Theorem and All That" by Dick Koch

div = 10 ** 6
mymax = 10 ** 7
p = []
p.append(1)

n = 1
while True:
	k = 1
	ans = 0
	while True:
		sign = (-1) ** (k+1%2)
		g1 = (3*k-1)*k/2
		g2 = (3*k+1)*k/2
		if g1>n:
			break
		ans += p[n-g1] * sign
		ans %= div
		if g2>n:
			break
		ans += p[n-g2] * sign
		ans %= div
		k += 1
	if ans%div == 0:
		print n
		break
	p.append(ans)
	n += 1




