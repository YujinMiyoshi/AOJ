import math

x1, y1, x2, y2 = map(float, input().split())

X = (x1 - x2)*(x1 - x2)
Y = (y1 - y2)*(y1 - y2)
P = X + Y

p = math.sqrt(P)

print(p)