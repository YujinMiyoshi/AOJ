n = int(input())

taro = 0
hanako = 0

for i in range(n):
    str1 , str2 = input().split()

    if str1 == str2:
        taro += 1
        hanako += 1

    elif str1 > str2:
        taro += 3

    elif str1 < str2:
        hanako += 3

print(taro, end="")
print(" ", end="")
print(hanako)