from utils import randbool

class Clauds:
    def __init__(self, w, h): 

        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)]for j in range(h)]

    def upd_clouds(self, r = 1, mxr = 20, g = 1, mxg = 10):
        for i in range(self.h):
            for j in range(self.w):
                if (randbool(r, mxr)):
                    self.cells[i][j] = 1
                    if (randbool(g, mxr)):
                        self.cells[i][j] = 2
                else:
                    self.cells[i][j] = 0

    def exdata(self):
        return {'cells': self.cells}

    def imdata(self, data):
        self.cells = data['cells'] or [[0 for i in range(self.w)] for j in range(self.h)]

