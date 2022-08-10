while True:
    h, w = map(int, input().split())

    if h == 0 and w == 0:
        break

    for i in range(h):
        print("#", end="")

        if i == 0 or i == h-1:
            for j in range(w-2):
                print("#", end="")

        else:
            for j in range(w-2):
                print(".", end="")

        print("#")
    print()