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

d3 = Dice()
d4 = Dice()

num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

d3.input(num1[0], num1[1], num1[2], num1[3], num1[4], num1[5])
d4.input(num2[0], num2[1], num2[2], num2[3], num2[4], num2[5])

boolean = False
count = 0

for i in range(1000):
    d4.move(random.choice('NSEW'))

    for i in range(6):
        if d3.number[i] == d4.number[i]:
            count += 1
    if count == 6:
        boolean = True
    count = 0

if boolean:
    print('Yes')
else:
    print('No')