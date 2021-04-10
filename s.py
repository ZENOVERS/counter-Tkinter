import tkinter as tk

count = 0

def countUP():
    global count
    count += 1
    label1.config(text=str(count))
    
def countDOWN():
    global count
    count -= 1
    label1.config(text=str(count)) 

win = tk.Tk()

win.title('Counter')
win.geometry('270x180')
win.resizable(1, 1)

label1 = tk.Label(win, text='NaN', width=15, heigh=5,fg='green', relief='solid')
label1.pack()

button1 = tk.Button(win, text='+', overrelief='solid', width=15, command=countUP, repeatdelay=1000, repeatinterval=100)
button1.pack()

button2 = tk.Button(win, text='-', overrelief='solid', width=15, command=countDOWN, repeatdelay=1000, repeatinterval=100)
button2.pack()

win.mainloop()
