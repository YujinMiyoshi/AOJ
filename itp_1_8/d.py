str1 = input()
str2 = input()

str1 += str1

if str1.find(str2) == -1:
    print("No")
else:
    print("Yes")