a = []
for i in range(1, 10):
    b = []
    for j in range(1,10):
        b.append(str(i*j)+(3-len(str(i*j)))*' ')
    a.append(b)
for i in range(9):
    print(*a[i], end = '\n\n')