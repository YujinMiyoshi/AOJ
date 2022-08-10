r, c = map(int, input().split())
t = [[0]*(c+1) for i in range(r+1)]

for i in range(r):
    T = list(map(int, input().split()))
    for j in range(c):
        t[i][j] = T[j]

for i in range(r):
    for j in range(c):
        t[i][c] += t[i][j]

for j in range(c+1):
    for i in range(r):
        t[r][j] += t[i][j]

for i in range(0, r+1):
    for j in range(0, c+1):
        if j > 0:
            print(" ", end="")
        print(t[i][j], end="")
    print()