W, H, x, y, r = map(int, input().split())

if 0 <= x-r and x+r <= W and 0 <= y-r and y+r <= H:
    print('Yes')
else:
    print('No')


"""
w, h, x, y, r = map(int, input().split())

if (x - r) >= 0 and (y - r) >= 0:
    if (x + r) <= w and (y + r) <= h:
        print("Yes")
    else:
        print("No")
else:
    print("No")
"""