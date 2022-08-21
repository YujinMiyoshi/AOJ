n, m, l = map(int, input().split())

a = [[0]*m for i in range(n)]
b = [[0]*l for j in range(m)]
c = [[0]*l for k in range(n)]

for i in range(n):
    a[i] = list(map(int, input().split()))

for i in range(m):
    b[i] = list(map(int, input().split()))

for i in range(n):
    for j in range(l):
        for k in range(m):
            c[i][j] += a[i][k]*b[k][j]
        print(c[i][j], end="")
        if j < l-1:
            print(" ", end="")
    print()