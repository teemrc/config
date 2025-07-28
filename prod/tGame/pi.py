import os
from time import sleep
from pynput import keyboard
from random import randint

class Map:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.x, self.y = 0, 0
        self.line = [['◻' for a in range(self.h)] for f in range(self.w)]

    def g(self):
        for i in range(self.w):
            print(*self.line[i])

    def mov(self, w, h):

        x, y = h + self.x, w + self.y
        if (x >= 0 and y >= 0 and x < self.h and y < self.w):
            self.x, self.y = x, y

        self.up()
        
    def up(self):
        self.line = [['◻' for a in range(self.h)] for f in range(self.w)]

m = Map(10, 10)

def r():
    r1 = randint(1, 8)
    r2 = randint(1, 8)
    return r1, r2

def dam(r1, r2):
    m.line[r1][r2]= '🟎'

def ge():
    global rd
    while True:
        if m.line[rd[0]][rd[1]] == '🟎':
            rd = r()
        else:
            break

    m.line[rd[0]][rd[1]] = '🞕'

rd = r()
cnt = 0
h = 5
v = 0
t = 0

def rr():
    global li
    li = []
    while True:
        rs = r()
        if len(li) == 15:
            break
        if (rs[0] == m.y and rs[1] == m.x) or (m.line[rs[0]][rs[1]] == '🞕'):
            continue
        else:
            li.append(rs)
rr()
def gd():
    for i in li:
        dam(i[0], i[1])

def go():
    os.system('cls')
    with open('res.txt', 'r+') as f:
            rl = f.readline()
            if cnt > int(rl):
                f.seek(0)
                f.write(str(cnt))
    print('Игра окончена.')
    print(f'Ваш счёт: {cnt}')
    print(f'Лучший результат: {rl}')
    print(f'Время жизни: {s//60}:{s%60}')
    exit(0)

def two():
    TS = 0.00158 
    global cnt, h, rd, li, rl, v, t, s
    m.line[m.y][m.x] = '◼'
    t+=1
    s = t//64
    
    if not '🞕' in m.line:
        ge()

    if not '🟎' in m.line:
        gd()

    if m.y == rd[0] and m.x == rd[1]:
        cnt += 1
        m.line[rd[0]][rd[1]] = '◻'
        rd = r()
        ge()

    if m.line[m.y][m.x] == '🟎':
        h -= 1
        if len(li) == 15:
            m.up()
            rr()
        gd()

    if t % 1266 == 0:
        if len(li) == 15:
            m.up()
            rr()
        gd()

    if h == 0:
        go()
        
    m.g()
    print(f'Жизни: {h}')
    print(f'Результат: {cnt}')
    with open('res.txt', 'r') as f:
        rl = f.readline()
        print(f'Лучший результат: {rl}')
    print(f'{s//60}:{s%60}')

    sleep(TS)

MOVES = {'w': (-1, 0), 'd': (0, 1), 's': (1, 0), 'a': (0, -1)}
e = False

def proccess_key(key):
    global m, e
         
    c = key.char.lower()

    if c in MOVES.keys():
        w, h = MOVES[c][0], MOVES[c][1]
        m.mov(w, h)

    if c == 'e':
        e = True
    
    else:
        a = 0


listener = keyboard.Listener(
    on_press = None,
    on_release = proccess_key)
listener.start()

while True:
    os.system('cls')
    two()
    if e:
        go()
        break
