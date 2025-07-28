import arcade as ar
from random import randint
from time import sleep

class Maing(ar.Window):
    def __init__(self):
        self.h = 745 
        self.w = 475
        super().__init__(self.h, self.w, 'Helicopter')
        ar.set_background_color(ar.color.GRAY)
        self.center_window()

    def ra(self):
        while True:
            r1 = randint(58, 687)
            r2 = randint(158, 417)
            if (r1-21) % 37 == 0 and (r2-121) % 37 == 0:
                return r1, r2

    def ra1(self, x, y):
        moves = [(-37, 0), (0, 37), (37, 0), (0, -37)]
        t = randint(0, 3)
        dx, dy = moves[t][0], moves[t][1]                
        return (x + dx, y + dy)      



    def game_over(self):
        self.clear()
        ar.draw_text(f"Игра окончена.",5,440, ar.color.RED_BROWN,30,'left')
        ar.draw_text(f"Счёт: {self.cnt}",5,400, ar.color.RED_BROWN,30,'left')
        ar.draw_text(f"Время жизни: {self.time//60}:{self.time%60}",5,360, ar.color.RED_BROWN,30,'left')
        ar.draw_text(f"Нажмите R, чтобы начать сначала.",5,320, ar.color.RED_BROWN,30,'left')

    def generate_tree(self):
        while True:
            r = self.ra()
            if not (r in self.rl):
                break
        tree = ar.Sprite('img/tree.png')
        tree.center_x = r[0]
        tree.center_y = r[1]
        self.trees.append(tree)
        self.gt.append(r)

    def forest(self):
        while True:
            r = self.ra()
            if r in self.gt:
                break
        forest = ar.Sprite('img/danger.png')
        forest.center_x = r[0]
        forest.center_y = r[1]
        self.forests.append(forest)
        self.rf.append(r)

    def generate_river(self):
        river = ar.Sprite('img\sea.png')
        r = self.ra()    
        river.center_x = r[0]
        river.center_y = r[1]
        for i in range(10):                
                river = ar.Sprite('img\sea.png')
                river.center_x = r[0]
                river.center_y = r[1]
                self.rivers.append(river)
                self.rl.append(r)
                while True:
                    r = self.ra1(r[0], r[1])
                    if not (r[1] <116):
                        break

    def flash(self):
        while True:
            r = self.ra()
            if not (r in self.rl or r in self.gt):
                break
        fl = ar.Sprite('img/flash.png')
        fl.center_x = r[0]
        fl.center_y = r[1]
        self.flashs.append(fl)
        self.f.append(r)

    def upsh(self):
        rx = self.ra()
        ry = [121, 454]
        r2 = randint(0, 1)
        self.upshop = ar.Sprite('img\dollar.png', center_x=rx[0], center_y=ry[r2])

    def setup(self):
        self.object = ar.Sprite('img/helicopter.png', center_x=21, center_y=454)
        self.map = ar.SpriteList()
        self.trees = ar.SpriteList()
        self.rivers = ar.SpriteList()
        self.forests = ar.SpriteList()
        self.flashs = ar.SpriteList()
        self.cnt = 0
        self.h = 10
        self.b =True
        self.bu = False
        self.rf = []
        self.rl = []
        self.gt = [] 
        self.f = []
        self.tank = 0
        self.max_tank = 1
        self.t = 0
        self.ti = 1200
        self.x = 21
        self.y = 454    
        
        for i in range(10):
            for i in range(20):
                mapo = ar.Sprite('img/green.png')
                mapo.center_x = self.x
                mapo.center_y = self.y
                self.map.append(mapo)
                self.x += 37
            self.x = 21
            self.y -= 37
        for i in range(7):
            self.generate_river()            
        for i in range(60):
            self.generate_tree()
        for i in range(20):
            self.flash()
        self.upsh()

    def update(self, delta_time: float):
        self.object.update() 

        ob_wat = ar.check_for_collision_with_list(self.object, self.rivers)
        ob_for = ar.check_for_collision_with_list(self.object, self.forests)
        up = ar.check_for_collision(self.object, self.upshop)
        ob_fl = ar.check_for_collision_with_list(self.object, self.flashs)

        for d in ob_fl:
            self.h -= 1            
            self.f.clear()
            self.flashs.clear()
            for l in range(20):
                self.flash()

        if up:
            while self.cnt > 300:
                self.cnt -= 300
                self.max_tank += 1

        for k in ob_wat:
            self.tank = self.max_tank   

        for n in ob_for:
            if self.tank > 0:
                self.tank -= 1
                self.cnt += 100 
                c = (n.center_x, n.center_y)
                n.kill()
                ind = self.rf.index(c)
                self.rf.pop(ind)

        if self.h <= 0:
            self.b = False

        if self.t == 600:
            for i in range(15):
                self.forest()
            self.bu = True

        if self.t % 1200 == 0 and self.t != 0:
            self.f.clear()
            self.flashs.clear()
            for l in range(20):
                self.flash()

        if self.bu:
            self.ti -= 1
            if self.ti == 0:                            
                for i in self.rf:
                    if i in self.gt:
                        q = self.gt.index(i)
                        self.trees[q].kill()
                        self.gt.pop(q)
                self.forests.clear()
                for a in range(15):
                    self.forest()
                for l in range(5):
                    self.generate_tree()
                self.ti = 1200

    def on_draw(self):
        if self.b:
            self.clear()
            self.map.draw()
            self.trees.draw()
            self.forests.draw()
            self.rivers.draw()
            self.upshop.draw()
            self.flashs.draw()
            self.object.draw()
            
            self.time = self.t//60
            self.tim = self.ti//60
            self.t+=1
 
            ar.draw_text(f"Жизни: {self.h}",205,65, ar.color.BLACK,15,'left')
            ar.draw_text(f"Вода: {self.tank}/{self.max_tank}",385,65, ar.color.BLACK,15,'left')
            ar.draw_text(f"Счёт: {self.cnt}",205,47, ar.color.BLACK,15,'left')
            ar.draw_text(f"{self.time//60}:{self.time%60}",205,27, ar.color.BLACK,15,'left')
            if self.bu:
                ar.draw_text(f"{self.tim//60}:{self.tim%60}",550,40, ar.color.RED_BROWN,30,'left')
        if self.b == False:
            self.game_over()

    def on_key_press(self, symbol: int, modifiers: int):
        if self.b:
            if symbol == ar.key.D and self.object.center_x < 745 - (5 + self.object.height/2):
                self.object.center_x += 37 
            elif symbol == ar.key.A and self.object.center_x > 5 + self.object.height/2:
                self.object.center_x -= 37 
            elif symbol == ar.key.W and self.object.center_y < self.w - 5 - self.object.width/2:
                self.object.center_y += 37 
            elif symbol == ar.key.S and self.object.center_y > 5 + self.object.height/2+100:
                self.object.center_y -= 37 
            elif symbol == ar.key.G:
                self.b = False
        if self.b == False:
            if symbol == ar.key.R:
                self.setup()
            
game = Maing()
game.setup()
ar.run()