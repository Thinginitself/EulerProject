#Euler Project 9
#Thinginitself

def stangeProduct(n):
	for i in range(1,n/2):
		for j in range(1,n/2):
			if i*i + j*j == (n-i-j)*(n-i-j):
				return i*j*(n-i-j)


n = input()
print stangeProduct(n)