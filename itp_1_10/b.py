import math

a, b, deg = map(int, input().split())

rad = math.radians(deg)

cos = math.cos(rad)
sin = math.sin(rad)

c = math.sqrt(a*a + b*b - 2*a*b*cos)
s = a*b*sin/2.0
h = s*2/a

l = a + b + c

print("%.8f %.8f %.8f" %(s, l, h))