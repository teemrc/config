import tkinter as tk
from tkinter import Label
import time

app = tk.Tk()
app.title('Time')
app.geometry('300x100')
def timer():
    t = time.localtime()
    ti = time.strftime("%H:%M:%S", t)
    label.config(text=ti, width=300, font=('Ubuntu', 50))
    app.after(100, timer)

label = Label(app, text='00:00:00')
label.pack()

app.protocol('WM_DELETE_WINDOW', app.quit)
timer()
app.mainloop()


