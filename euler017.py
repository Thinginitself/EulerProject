#Euler Project 17
#Thinginitself

# NOLOLON means number original list of letters  of numbers
#0~19
NOLOLON = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4,
		  3, 6, 6, 8, 8, 7, 7, 9, 8, 8]

#20
NOLOLON.extend(x+6 for x in NOLOLON[:10])
#30
NOLOLON.extend(x+6 for x in NOLOLON[:10])
#40
NOLOLON.extend(x+5 for x in NOLOLON[:10])
#50
NOLOLON.extend(x+5 for x in NOLOLON[:10])
#60
NOLOLON.extend(x+5 for x in NOLOLON[:10])
#70
NOLOLON.extend(x+7 for x in NOLOLON[:10])
#80
NOLOLON.extend(x+6 for x in NOLOLON[:10])
#90
NOLOLON.extend(x+6 for x in NOLOLON[:10])

#100~999
for i in NOLOLON[1:10]:
	NOLOLON.append(i+7) #"X hundred" has no "and"!
	NOLOLON.extend(x+i+10 for x in NOLOLON[1:100])
NOLOLON.append(11)
print sum(NOLOLON)