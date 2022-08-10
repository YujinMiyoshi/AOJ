B = [[[0]*10 for i in range(3)] for j in range(4)]

n = int(input())

for i in range(n):
    b, r, f, v = map(int, input().split())

    B[b-1][r-1][f-1] += v

for i in range(4):
    for j in range(3):
        for k in range(10):
            print("", B[i][j][k], end="")
        print()
    if i < 3:
        print("#"*20)
