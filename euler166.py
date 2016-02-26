#Euler Project 166
#Thinginitself
#ugly and naive

most = 10
f = [[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]]

def mytry(j, mysum):
	f[2][0] = j
	f[2][1] = f[0][0] + f[1][0] + f[2][0] - f[0][3] - f[1][2]
	f[2][2] = (mysum - f[2][0] - f[2][1] - f[0][0] - f[1][1] + f[0][3] + f[1][3]) / 2
	f[2][3] = mysum - f[2][0] - f[2][1] - f[2][2]
	if (f[2][1] > 9) or f[2][1] < 0 or f[2][2] < 0 or f[2][2] > 9 or f[2][3]<0 or f[2][3]>9:
		return 0
	for i in xrange(4):
		f[3][i] = mysum - f[0][i] - f[1][i] - f[2][i]
		if f[3][i] > 9 or f[3][i] < 0:
			return 0
	if (f[0][0]+f[1][0]+f[2][0]+f[3][0]) != mysum:
		return 0
	if (f[0][1]+f[1][1]+f[2][1]+f[3][1]) != mysum:
		return 0
	if (f[0][2]+f[1][2]+f[2][2]+f[3][2]) != mysum:
		return 0
	if (f[0][3]+f[1][3]+f[2][3]+f[3][3]) != mysum:
		return 0
	return 1

def dfs(dep, mysum):
	if dep == 2:
		xx = 0
		for j in xrange(most):
			xx += mytry(j,mysum)
		return xx
	x = 0
	for i in xrange(most):
		if i > mysum:
			break
		f[dep][0] = i
		for j in xrange(most):
			if i+j > mysum:
				break
			f[dep][1] = j
			for k in xrange(most):
				if i+j+k > mysum:
					break
				elif mysum-i-j-k > 9:
					continue
				f[dep][2] = k
				f[dep][3] = mysum - i - j - k
				z = dfs(dep+1, mysum)
				x += z
	return x

res = 0
for i in xrange(17):
	res += dfs(0, i) * 2
res += dfs(0, 18)
print res