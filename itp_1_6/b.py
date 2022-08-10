cards="SHCD"

n = int(input())

exist=[[False]*14 for i in range(4)]

for i in range(n):
    c, N = input().split()
    N = int(N)
    exist[cards.find(c)][N] = True

for i in range(4):
    for j in range(1, 14):
        if not exist[i][j]:
            print(cards[i], j)
