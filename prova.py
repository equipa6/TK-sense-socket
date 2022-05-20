from tkinter import *
master = Tk()
buttons = []
n = 9

def prova(boto_clicat):
    print("S'clicat el numero {}".format(boto_clicat))
for i in range(n):
    button = Button(master, text = str(i), command=lambda i=i:prova(str(i)))
    button.pack()
    buttons.append(button)
master.mainloop()