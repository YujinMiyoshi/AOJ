str1 = input()
q = int(input())

for i in range(q):
    order = list(input().split())

    a = int(order[1])
    b = int(order[2])

    if order[0] == 'print':
        print(str1[a:b+1])

    elif order[0] == 'reverse':
        str1 = str1[:a] + str1[a:b+1][::-1] + str1[b+1:]

    else:
        str1 = str1[:a] + order[3] + str1[b+1:]