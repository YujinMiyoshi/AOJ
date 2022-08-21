import random

class Dice():
    def __init__(self):
        self.number = [i for i in range(6)]
        self.dir = [i for i in range(6)]

    def input(self, n1, n2, n3, n4, n5, n6):
        self.number[0] = n1
        self.number[1] = n2
        self.number[2] = n3
        self.number[3] = n4
        self.number[4] = n5
        self.number[5] = n6

    def move(self, way):
        for i in range(6):
            self.dir[i] = self.number[i]

        if way == 'N':
            self.input(self.dir[1], self.dir[5], self.dir[2], self.dir[3], self.dir[0], self.dir[4])

        elif way == 'E':
            self.input(self.dir[3],self.dir[1],self.dir[0],self.dir[5],self.dir[4],self.dir[2])

        elif way == 'W':
            self.input(self.dir[2],self.dir[1],self.dir[5],self.dir[0],self.dir[4],self.dir[3])

        elif way == 'S':
            self.input(self.dir[4],self.dir[0],self.dir[2],self.dir[3],self.dir[5],self.dir[1])

    def print(self):
        print(self.number[0])

n = int(input())

dice = []

for i in range(n):
    a = list(map(int, input().split()))
    d = Dice()
    d.input(a[0], a[1], a[2], a[3], a[4], a[5])
    dice.append(d)

flag = True

for i in range(n-1):
    for j in range(i+1, n):
        boolean = False
        count = 0

        for k in range(100):
            dice[i].move(random.choice('NSEW'))
            for l in range(6):
                if dice[i].number[l] == dice[j].number[l]:
                    count += 1
            if count == 6:
                boolean = True
            count = 0
        if boolean:
            flag = False
            break

if flag:
    print('Yes')
else:
    print('No')
