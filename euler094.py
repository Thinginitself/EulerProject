#Euler Project 94
#Thinginitself

#pell equation 
#t^2 - 3*z^2 = 4
#t = 3*a +- 4, a is width

import Queue

MAXNUM = 10 ** 9 + 2
q = Queue.Queue(maxsize = -1)
q.put([14,8])

set_of_t = set()
set_of_t.add(4)
set_of_t.add(14)

res = 0
while not q.empty():
	item = q.get()
	t = item[0]
	z = item[1]
	if t%3 == 1:
		res += t + 2
	else:
		res += t - 2
	t1 = 2*t+3*z
	z1 = t+2*z
	if t1 < MAXNUM and not (t1 in set_of_t):
		set_of_t.add(t1)
		q.put([t1,z1])
	t1 = 2*t-3*z
	z1 = t-2*z
	if t1 < MAXNUM and not (t1 in set_of_t):
		set_of_t.add(t1)
		q.put([t1,z1])

print res