while True:
    h, w = map(int, input().split())

    if h == 0 and w == 0:
        break

    for i in range(1, h+1):
        if i%2 == 1:
            for j in range(1, w+1):
                if j%2 == 1:
                    print("#", end="")
                else:
                    print(".", end="")
        else:
            for j in range(1, w+1):
                if j%2 == 1:
                    print(".", end="")
                else:
                    print("#", end="")
        print()
    print()