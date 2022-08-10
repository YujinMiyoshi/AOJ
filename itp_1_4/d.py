n = int(input())
l = list(map(int, input().split()))

min = l[0]
max = l[0]
sum = 0

for i in l:
    sum += i

    if min > i:
        tmp = i
        i = min
        min = tmp

    elif max < i:
        tmp = i
        i = max
        max = tmp

print(min, max, sum)