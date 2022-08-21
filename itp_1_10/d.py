import math

n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

sum = 0

for i in range(n):
    sum += math.sqrt((x[i] - y[i])*(x[i] - y[i]))

d1 =sum
sum = 0

for i in range(n):
    sum += (x[i] - y[i])*(x[i] - y[i])

d2 = math.sqrt(sum)
sum = 0

for i in range(n):
    sum += math.sqrt((x[i] - y[i])*(x[i] - y[i]))*(x[i] - y[i])*(x[i] - y[i])

d3 = math.pow(sum, 1/3)
sum = 0

dinf = max([math.sqrt((a - b)*(a - b)) for a, b in zip(x, y)])


print(d1)
print(d2)
print(d3)
print(dinf)