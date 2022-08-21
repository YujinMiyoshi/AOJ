while True:
    n = input()
    if int(n) == 0:
        break

    sum = 0

    for i in n:
        sum += int(i)

    print(sum)