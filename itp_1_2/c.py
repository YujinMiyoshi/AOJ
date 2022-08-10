a = list(map(int, input().split()))

for i in range(len(a)-1, 0, -1):
    k = 0
    while k < i:
        if a[k] > a[k+1]:
            tmp = a[k+1]
            a[k+1] = a[k]
            a[k] = tmp
        k += 1

print(a[0], a[1], a[2])