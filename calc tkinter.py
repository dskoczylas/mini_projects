from tkinter import *

root = Tk()
root.title("Simple calculator")
e = Entry(root, width=35, borderwidth=5)
e.grid(column=0, row=0, columnspan=3, padx=10, pady=10)

def button_add():
    return

button7 = Button(text='7', padx=40, pady=20, command=button_add).grid(column=0, row=1)
button8 = Button(text='8', padx=40, pady=20, command=button_add).grid(column=1,row=1)
button9 = Button(text='9', padx=40, pady=20, command=button_add).grid(column=2,row=1)

button4 = Button(text='4', padx=40, pady=20, command=button_add).grid(column=0,row=2)
button5 = Button(text='5', padx=40, pady=20, command=button_add).grid(column=1,row=2)
button6 = Button(text='6', padx=40, pady=20, command=button_add).grid(column=2,row=2)

button1 = Button(text='1', padx=40, pady=20, command=button_add).grid(column=0,row=3)
button2 = Button(text='2', padx=40, pady=20, command=button_add).grid(column=1,row=3)
button3 = Button(text='3', padx=40, pady=20, command=button_add).grid(column=2,row=3)



root.mainloop()