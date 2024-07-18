from tkinter import *
from PIL import Image,ImageTk
win = Toplevel()

path = Image.open("d:\\Images\\Display2.jpg")
render = ImageTk.PhotoImage(path)
img= Label(win, image=render)
img.pack(fill=BOTH,expand=True)
win.title("Image Window")
win.geometry("1300x660")

def entry():
    import Entry
def deposit():
    import Deposit
def withdraw():
    import Withdraw
def closeac():
    import Closeac
def interest():
    import Interest


lo = Label(win, text='WELCOME TO GBI',bg='#F88379',fg='Black', font=("Arial", 30, 'bold'))
lo.place(x=400, y=50)
bl = Button(win, text="LOGOUT", bg='#Fc8eac',width=10, font=("Arial", 15, 'bold'),command=win.destroy)
bl.place(x=1000, y=60)
b1 = Button(win, text="APPLICANT", bg='#E6e6fa',width=15, font=("Arial", 20, 'bold'),command=entry)
b1.place(x=100, y=150)
b2 = Button(win, text="DEPOSIT",bg='#E6e6fa', width=15,font=("Arial", 20, 'bold'),command=deposit)
b2.place(x=250, y=250)
b3 = Button(win, text="WITHDRAW", bg='#E6e6fa',width=15, font=("Arial", 20, 'bold'),command=withdraw)
b3.place(x=400, y=350)
b4 = Button(win, text="CLOSEAC",bg='#E6e6fa',width=15, font=("Arial", 20, 'bold'),command=closeac)
b4.place(x=550, y=450)
b5 = Button(win, text="INTEREST",bg='#E6e6fa',width=15, font=("Arial", 20, 'bold'),command=interest)
b5.place(x=700, y=550)

win.mainloop()

