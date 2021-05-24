#Euler Project 125
#Thinginitself

turns = 15
f = [0 for i in range(turns+1)]
f[0] = 1
for t in range(1, turns+1):
    for i in range(t+1)[::-1]:
        if i != 0:
            f[i] = f[i] + f[i-1] * t
print(sum(f)//sum(f[:8]))
