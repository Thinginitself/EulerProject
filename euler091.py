#Euler Project 91
#Thinginitself

NUM = 50

def dot(x1, y1, x2, y2):
    return x1 * x2 + y1 * y2

num = 0

for x1 in range(NUM+1):
    for y1 in range(NUM+1):
        for x2 in range(NUM+1):
            for y2 in range(NUM+1):
                if (x1 == 0 and y1 == 0) or (x2 == 0 and y2 == 0) or (x1 == x2 and y1 == y2):
                    continue
                x3 = x1 - x2
                y3 = y1 - y2
                if dot(x1, y1, x2, y2) == 0 or dot(x1, y1, x3, y3) == 0 or dot(x3, y3, x2, y2) == 0:
                    num += 1
print(num//2)