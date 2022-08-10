x, y = map(int, input().split())

while True:
    if x == 0 and y == 0:
        break

    elif x > y:
        tmp = x
        x = y
        y = tmp
    
    print(x, y)

    x, y = map(int, input().split())