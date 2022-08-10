n, m, l = map(int, input().split())

a = [[0]*m for i in range(n)]
b = [[0]*l for j in range(m)]
c = [[0]*m for k in range(m)]

for i in range(n):
    a[i] = list(map(int, input().split()))

for i in range(m):
    b[i] = list(map(int, input().split()))

print(a)
print(b)