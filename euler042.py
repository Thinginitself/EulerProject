#Euler Project 42
#Thinginitself

def triangles(n):
	y = 0
	res = set()
	for i in xrange(1,n):
		y += i
		res.add(y)
	return res

triangleSet = triangles(100)

def isTriangleWord(word):
	res = 0
	for c in word:
		res += ord(c) - ord('A') + 1
	return res in triangleSet

with open('euler042_words.txt','r') as f:
	s = f.read()
mywords = filter(lambda x: x != ',' and x != '', s.split("\""))

count = 0
for x in mywords:
	if isTriangleWord(x):
		count += 1
print count