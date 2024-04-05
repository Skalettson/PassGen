from tkinter import *
from random import choice


def randomize():
    PassLenght = e.get()
    e.delete(0, END)
    for i in range(int(PassLenght)):
        e.insert(0, choice(chars))


root = Tk()
root.title('Pass Gen')
root.geometry('480x300')
root.resizable(width=False, height=False)

chars = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
         'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
         'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
         'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_', '-', '@', '.', ',', '/',
         '|', '!', '#', '$', '%', '^', '&', '(', ')', '=', '+', '[', ']', '{', '}', ';', '"',
         '<', '>', '~']

user = Label(root, font='Downtown', text='Впишите число символов для пароля')
user.place(relx=0.5, y=20, anchor=CENTER)

e = Entry(root, font='Arial 13')
e.place(relx=0.5, y=50, anchor=CENTER)

btn = Button(root, text='Генерировать', font=('Downtown', 17, 'bold'), command=randomize)
btn.place(relx=0.5, y=120, anchor=CENTER)

root.mainloop()