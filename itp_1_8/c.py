a = "abcdefghijklmnopqrstuvwxyz"

A = [0]*26

while True:
    try:
        str = input().lower()
    except EOFError:
        break
    for i in str:
        x = 0
        for j in a:
            if i == j:
                A[x] += 1
            x += 1

x = 0
for i in a:
    print(i, ":", A[x])
    x += 1