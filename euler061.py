#Euler Project 61
#Thinginitself

def product(low,high,fuc):
	res = []
	for i in xrange(1,200):
		n = fuc(i)
		if n>low and n<high:
			res.append(n)
		if n>high:
			break
	return res

f = [0] * 6
f[0] = product(1000,10000,lambda x: x*(x+1)/2)
f[1] = product(1000,10000,lambda x: x*x)
f[2] = product(1000,10000,lambda x: x*(3*x-1)/2)
f[3] = product(1000,10000,lambda x: x*(2*x-1))
f[4] = product(1000,10000,lambda x: x*(5*x-3)/2)
f[5] = product(1000,10000,lambda x: x*(3*x-2)) 


q = []
for i in xrange(6):
	q += f[i]

s = [0] *6

def match(x,y):
	return (x/100)==(y%100)

end = 5
flag = [0] * 6
def dfs(k):
	if k==-1:
		if match(s[end],s[0]):
			print sum(s)
		return
	for j in xrange(6):
		if flag[j]==0:
			for i in f[j]:
				if k==end or match(i,s[k+1]):
					s[k] = i
					flag[j] = 1
					dfs(k-1)
					flag[j] = 0
					s[k] = 0

dfs(end)

