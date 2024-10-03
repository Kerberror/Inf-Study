b = []
a = []
while a!=[0]:
    a = list(map(int, input().split()))
    if a == [0]:
        break
    b.append(a)
c = list(zip(*b))
m = []
for i in range(len(c)):
    k = list(c[i])
    m.append(k)
m.reverse()
for i in range(len(c)):
    for j in range(len(m[i])):
        print(str(m[i][j])+(4-len(str(m[i][j])))*' ',end='')
    print('\n')