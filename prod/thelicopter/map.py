from utils import randbool, randcell, randcell2

# 🌲 🌊 🟩  🏥  💵  🔥
#  0  1   2   3    4  5 


CELL_T = '🟩🌲🌊🏥💵🔥'
TREE_B = 100
UBG_C = 300
LIVE_C = 300

class Map:
              #________________________системные________________________________

    def __init__(self, w, h): #Генерация поля
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)]for j in range(h)]
        self.generate_f(3, 10)
        self.generate_r(10)
        self.generate_r(10)
        self.generate_r(10)
        self.gener_ubgshop()
        self.gener_ubgshop_live()

    def check_b(self, x, y):
        if (x < 0 or y < 0 or x >= self.h or y >= self.w):
            return False
        return True

    def print_map(self, helico, clouds):              #Вывод карты
        print('🔲' * (self.w + 2))
        for ri in range(self.h):
            print('🔲',end='')
            for ci in range(self.w):
                cell = self.cells[ri][ci]

                if (clouds.cells[ri][ci] == 1):
                    print('☁️ ', end= '')

                elif (clouds.cells[ri][ci] == 2):
                    print('⚡', end= '')

                elif (helico.x == ri and helico.y == ci):
                    print('🚁', end ='')

                elif (cell >= 0 and cell < len(CELL_T)):
                    print(CELL_T[cell], end = '')
            print('🔲',end='')
            print()
        print('🔲' * (self.w + 2))
       #_______________________генераторы_____________________
    def generate_r(self, l):          #Генерация реки
        rc = randcell(self.w, self.h)
        rx, ry = rc[0], rc[1]
        self.cells[rx][ry] = 2
        while l > 0:
            rc2 = randcell2(rx, ry)
            rx2, ry2 = rc2[0], rc2[1]
            if (self.check_b(rx2, ry2)):
                self.cells[rx2][ry2] = 2
                rx, ry = rx2, ry2
                l -= 1

    def generate_f(self, r, mxr):     #Генерция леса
        for ri in range(self.h):
            for ci in range(self.w):
                if randbool(r, mxr):
                    self.cells[ri][ci] = 1

    def generate_tree(self):                 
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if (self.cells[cx][cy] == 0):
            self.cells[cx][cy] = 1

    def gener_ubgshop(self):
        c= randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        self.cells[cx][cy] = 4

    def gener_ubgshop_live(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] != 4:
            self.cells[cx][cy] = 3
        else:
            self.gener_ubgshop_live()
    
              #____________________________огонь_____________________________

    def add_fire(self):              #добавление огня
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] == 1:
            self.cells[cx][cy] = 5

    def upd_fire(self):           #Обновление огня
        for ri in range(self.h):
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if cell == 5:
                    self.cells[ri][ci] = 0
        for i in range(10):
            self.add_fire()

#_________________________вертолёт____________________

    def prochelico(self, helico, clouds):
        c = self.cells[helico.x][helico.y]
        d = clouds.cells[helico.x][helico.y]

        if (c == 2):
            helico.tank = helico.max_tank

        if (c == 5 and helico.tank > 0):
            helico.tank -= 1
            helico.score += TREE_B
            self.cells[helico.x][helico.y] = 1

        if (c == 4 and helico.score >= UBG_C):
            helico.max_tank += 1
            helico.score -= UBG_C

        if (c == 3 and helico.score >= LIVE_C):
            helico.lives += 1
            helico.score -= LIVE_C

        if (d == 2):
            helico.lives -= 1
            if (helico.lives == 0):
                helico.gameOver()

    def exdata(self):
        return {'cells': self.cells}

    def imdata(self, data):
        self.cells = data['cells'] or [[0 for i in range(self.w)] for j in range(self.h)]

