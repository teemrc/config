import os, time

map = [['=' for i in range(20)] for j in range(10)]

x = 0
y = 0

def pr():
    map[y][x] = '*'
    for i in map:
        print(*i)

while True:
    os.system('clear')
    pr()
    time.sleep(0.2)