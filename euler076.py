#Euler Project 76
#Thinginitself

num = 100

f = [0] * (num+2)
f[0] = 1
for i in range(1, num):
    for j in range(i, num+1):
        f[j] += f[j - i]
print f[num]