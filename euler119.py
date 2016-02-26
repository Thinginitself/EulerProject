#Euler Project 119
#Thinginitself

import  math

def num_sum(n):
	res = 0
	while n > 0:
		res += n % 10
		n /= 10
	return res

ans = list()

for i in xrange(2, 100):
	res = i * i
	l = math.log(res)/2.3
	while l < i:
		if num_sum(res) == i:
			ans.append(res)
		res *= i
		l = math.log(res)/2.3
ans.sort()
print ans[29]