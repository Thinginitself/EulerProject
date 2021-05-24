#Euler Project 166
#Thinginitself

ll = [len(x) for x in format(10 ** 25, 'b').split('1')]
res = 1
A0 = A = 1
for a in ll[1:]:
    new_A0 = A0 * (a+1) + A
    new_A = A0 * a + A
    A0 = new_A0
    A = new_A

print(A)
