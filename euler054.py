#Euler Project 54
#Thinginitself

def change(c):
	if c[0] == "T":
		num = 10
	elif c[0] == "J":
		num = 11
	elif c[0] == "Q":
		num = 12
	elif c[0] == "K":
		num = 13
	elif c[0] == "A":
		num = 14
	else:
		num = int(c[0])
	return (num, c[1])

with open('euler054_poker.txt','r') as f:
	s = f.read()
card = map(change, s.split())



def changeorder(numlist):
	new = []
	for i in numlist:
		c = 0
		for j in numlist:
			if i == j:
				c += 1
		new.append((c,i))
	new.sort()
	z = [x[1] for x in new][::-1]
	return z

def higher(myhand, yourhand):
	mynum = [x[0] for x in myhand]
	yournum = [x[0] for x in yourhand]
	mynew = changeorder(mynum)
	yournew = changeorder(yournum)
	for i in xrange(len(mynew)):
		if mynew[i] > yournew[i]:
			return True
		elif mynew[i] < yournew[i]:
			return False


	return False

def onepair(hand):
	tmp = [0] * 15
	for i in hand:
		tmp[i[0]] += 1
	for i in tmp:
		if i >= 2:
			return True
	return False

def twopairs(hand):
	tmp = [0] * 15
	count = 0
	for i in hand:
		tmp[i[0]] += 1
	for i in tmp:
		if i >= 2:
			count += 1
	if count == 2:
		return True
	return False

def threeofaking(hand):
	tmp = [0] * 15
	for i in hand:
		tmp[i[0]] += 1
	for i in tmp:
		if i >= 3:
			return True
	return False

def straight(hand):
	new = [x[0] for x in hand]
	new.sort()
	flag = True
	for i in xrange(1,len(new)):
		if new[i]-new[i-1] != 1:
			flag = False
			break
	if flag:
		return True
	if new[4]==14 and new[0]==2 and new[1]==3 and new[2]==4 and new[3]==5:
		return True
	return False

def flush(hand):
	color = hand[0][1]
	for i in hand:
		if i[1] != color:
			return False
	return True

def fullhouse(hand):
	return threeofaking(hand) and onepair(hand)

def fourofaking(hand):
	tmp = [0] * 15
	for i in hand:
		tmp[i[0]] += 1
	for i in tmp:
		if i >= 4:
			return True
	return False

def straightflush(hand):
	return straight(hand) and flush(hand)

def royalflush(hand):
	new = set([x[0] for x in hand])
	if not (14 in new and 13 in new):
		return False
	return straightflush(hand)

getpoint = [royalflush,straightflush,fourofaking,fullhouse,flush,straight,threeofaking,twopairs,onepair]

def point(hand):
	p = 0
	for i in xrange(len(getpoint)):
		if getpoint[i](hand):
			p += (11-i)*100
			return p
	return p


def win(myhand,yourhand):
	mypoint = point(myhand)
	yourpoint = point(yourhand)
	if mypoint > yourpoint:
		return True
	elif mypoint == yourpoint and higher(myhand,yourhand):
		return True
	return False

def main():
	res = 0
	for i in xrange(1000):
		if win(card[i*10:i*10+5], card[i*10+5:i*10+10]):
			res += 1
	print res
main()