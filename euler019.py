#Euler Project 19
#Thinginitself

import calendar

weekday = 1
res = 0
for i in xrange(1901,2000):
	for j in xrange(1,13):
		weekday += calendar.monthrange(i,j)[1]
		weekday %= 7
		if weekday == 0:
			res += 1
print res