import math

while True:
    n = int(input())

    if n == 0:
        break

    s = list(map(int, input().split()))

    sum1 = 0
    sum2 = 0

    for i in s:
        sum1 += i

    ave = sum1/n

    for i in s:
        sum2 += (i - ave)*(i - ave)

    a = math.sqrt(sum2/n)

    print(a)