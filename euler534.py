#Euler Project 534
#Thinginitself

#weak queens puzzle


res = 0

def dfs(row,ld,rd):
	if row == FULL:
		global res
		res += 1
		return 
	pos = ~(row | ld | rd) & FULL
	while pos != 0:
		q = pos & -pos
		pos = pos - q
		dfs(row + q, \
			((ld + q) << 1)&FULL, \
			((rd + q) >> 1)&FULL) 

n = 14
FULL = (1 << n) - 1
dfs(0,0,0)
print res