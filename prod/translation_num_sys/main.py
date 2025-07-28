import tkinter as tk

class App():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.app = tk.Tk()
        self.app.geometry(f'{self.width}x{self.height}')
        self.app.title('Перевод систем счислений')
        self.entry_data =  tk.Entry(self.app)
        self.entry_data.place(x=10, y=30)
        self.entry_start = tk.Entry(self.app)
        self.entry_start.place(x=235, y=30)
        self.entry_end = tk.Entry(self.app)
        self.entry_end.place(x=425, y=30)
        self.label1 = tk.Label(self.app, text='Из', font=40)
        self.label1.place(x=190, y=27)
        self.label2 = tk.Label(self.app, text='В', font=40)
        self.label2.place(x=400, y=27)
        self.label_res = tk.Label(self.app, text='Результат: ', font=40)
        self.label_res.place(x=195, y=75)
        self.button = tk.Button(self.app, text='Перевести', command=self.clic)
        self.button.place(x=10, y=75)
        self.app.mainloop() 

    def int_to_other(self, end_num, data):
        res = ''
        while data >= end_num:
            res+=str(data%end_num)
            data//=end_num
        res+=str(data%end_num)
        return res[::-1]

    def clic(self):
        try:
            data = self.entry_data.get()
            start = int(self.entry_start.get())
            end = int(self.entry_end.get())
        except:
            return None
        
        if data == '':
            return None
        
        elif end == 16:
            self.res = hex(int(data, start))[2:]

        elif start == 10:
            self.res = self.int_to_other(end, int(data))

        elif end == 10:
            self.res = int(data, start)

        else:
            self.res = self.int_to_other(end, int(data, start))

        self.label_res.config(text=f'Результат: {self.res}')

if __name__ == '__main__':
    win = App(750, 220)
