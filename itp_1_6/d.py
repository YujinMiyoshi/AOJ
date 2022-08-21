n ,m = map(int, input().split())

A = [[0]*m for i in range(n)]

for i in range(n):
    A[i] = list(map(int, input().split()))

B = [[0]*1 for i in range(m)]

for i in range(m):
    B[i] = int(input())

C = [0]*n
for i in range(n):
    for j in range(m):
        C[i] += A[i][j]*B[j]

for i in range(n):
    print(C[i])