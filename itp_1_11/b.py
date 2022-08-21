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

d2 = Dice()

num = list(map(int, input().split()))
d2.input(num[0], num[1], num[2], num[3], num[4], num[5])

q = int(input())

for i in range(q):
    a, b = map(int, input().split())

    while True:
        if d2.dir[0] == a and d2.dir[1] == b:
            print(d2.dir[2])
            break

        d2.move(random.choice('NSEW'))