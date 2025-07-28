import tkinter as tk
from tkinter import Button, Label

app = tk.Tk()
app.title('Calculator')
app.geometry('340x220')

list_oper =['7','8','9', '/', '4', '5', '6', '*', '1', '2', '3', '-','0', 'C', '=', '+'] #[0, 'C', '=', 1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 0
y = 50

lab = Label(app, text='', height=3, width=40, font=1)
lab.pack()

def print_but(t, x, y):
    but = Button(app, text=t, command=lambda : but_clic(t), width=10, height=2, font=20)
    but.place(x=x, y=y)

def but_clic(oper):
    if oper == 'C':
        lab.config(text='')
    elif oper == '=':
        exec('n = str('+ lab.config()['text'][-1]+')')
        lab.config(text=eval('n'))
    else:
        lab.config(text=lab.config()['text'][-1]+oper)    

for i in list_oper:
    print_but(i, x, y)
    x += 80
    if x > 240:
        x = 0
        y+=40

app.mainloop()
