count = 0
w = input().lower()
while True:
    e = input()
    if e == "END_OF_TEXT":
        break

    t = e.lower().split()

    for i in t:
        if i == w:
            count += 1

print(count)