from utils import randcell
import os

class Helicopter:

    def __init__(self, w, h):
        rc = randcell(w, h)
        rx, ry = rc[0], rc[1]
        self.x = rx
        self.y = ry
        self.h = h
        self.w = w
        self.tank = 0
        self.max_tank = 1
        self.score = 0
        self.lives = 20

    def move(self, dx, dy):
        nx, ny = dx + self.x, dy + self.y
        if (nx >= 0 and ny >= 0 and nx < self.h and ny < self.w):
            self.x, self.y = nx, ny

    def print_stats(self):
        print('🚰 ', self.tank, '/', self.max_tank, sep= '')
        print('🏆 ', self.score, end= ' | ')
        print('💛 ', self.lives)

    def gameOver(self):
        os.system("cls")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X                                 X")
        print("X                                 X")
        print("X  GAME OVER, YOUR SCORE IS", self.score, "    X")
        print("X                                 X")
        print("X                                 X")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        exit(0)

    def exdata(self):
        return{'score': self.score,
               'lives': self.lives,
               'x': self.x, 'y': self.y,
               'tank': self.tank, 'maxtank': self.max_tank}

    def importData(self, data):
        self.x = data['x'] or 0
        self.y = data['y'] or 0
        self.tank = data['tank'] or 0
        self.maxTank = data['maxtank'] or 1
        self.lives = data['lives'] or 20
        self.score = data['score'] or 0