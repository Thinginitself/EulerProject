#Euler Project 91
#Thinginitself

NUM = 80
matrix = [[] for i in range(NUM)]
with open("/Users/xiaoning_work/Documents/CodeBase/EulerProject/p082_matrix.txt") as fin:
    for line in fin:
        tmp = [int(x) for x in line.strip().split(",")]
        for i in range(NUM):
            matrix[i].append(tmp[i])

sum_from_top = []
for i in range(NUM):
    tmp = []
    now = 0
    for j in range(NUM):
        now += matrix[i][j]
        tmp.append(now)
    sum_from_top.append(tmp)

def get_distance(i, a, b):
    if a < b:
        a, b = b, a
    sum_b = 0 if b == 0 else sum_from_top[i][b-1]
    sum_a = sum_from_top[i][a]
    return sum_a - sum_b

best = [0 for i in range(NUM)]
for i in range(NUM):
    new_best = []
    for j in range(NUM):
        best_num = -1
        for k in range(NUM):
            now_num = get_distance(i, j, k) + best[k]
            if best_num == -1 or now_num < best_num:
                best_num = now_num
        new_best.append(best_num)
    best = new_best

print(min(best))