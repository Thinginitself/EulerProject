#Euler Project 59
#Thinginitself

symbol = set("~@#$%^&*>")

def decipher(a,b,c,text):
	newtext = str()
	for i in xrange(len(text)):
		if i%3 == 0:
			char = (chr(text[i] ^ a))
		elif i%3 == 1:
			char = (chr(text[i] ^ b))
		elif i%3 == 2:
			char = (chr(text[i] ^ c))
		else:
			pass
		if char in symbol:
			return -1
		newtext += char
	return newtext


with open('euler059_cipher.txt','r') as f:
	s = f.read()
text = map(int,s.split(','))

letter = []
for i in xrange(26):
	letter.append(chr(97+i))

for i in letter:
	for j in letter:
		for k in letter:
			res = decipher(ord(i),ord(j),ord(k),text)
			if res != -1:
				print i,j,k,res
				print sum(map(ord,res))