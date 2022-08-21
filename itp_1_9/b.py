while True:
    str1 = input()

    if str1 == "-":
        break

    m = int(input())

    for i in range(m):
        j = int(input())

        str2 = str1[0:j]
        str1 += str2
        str1 = str1[j:len(str1)]

    print(str1)