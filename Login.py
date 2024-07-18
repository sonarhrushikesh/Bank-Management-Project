from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
window=Tk()

path=Image.open("D:\Images\lg.jpg")
render=ImageTk.PhotoImage(path)
img=Label(window,image=render)
img.pack(fill=BOTH,expand=True)
window.title("Login Window")
window.geometry("1200x670")

def login():
    uname = tu.get()
    pwd = tp.get()
    if uname == '' or pwd == '':
        messagebox.showinfo("Login System", "Please enter the Username and Password")
    else:
        if uname == "aeiou" and pwd == "password":
            import Display

        else:
            messagebox.showinfo("Login System", "Please enter correct credentials")

def show():
        if tp.cget('show') == '':
            tp.config(show='*')
            s1.config(text='Show Password')
        else:
            tp.config(show='')
            s1.config(text='Hide Password')


#For Design
c = Canvas(window, bg="white",width='380', height="250")
c.place(x=400, y=250)

l1=Label(window,bg='white',fg='blue',text="Login Here",font=("Garamond",22))
l1.place(x=520,y=265)
us=Label(window,bg='white',fg='Black',text="Username:-",font=("Times New Roman",17))
us.place(x=420,y=330)
tu=Entry(window,bd=3,width=30)
tu.place(x=540,y=335)
pas=Label(window,bg='white',fg='Black',text="Password:-",font=("Times New Roman",17))
pas.place(x=420,y=370)
tp=Entry(window,bd=3,show='*',width=30)
tp.place(x=540,y=375)
s1=Button(window,text='#F0fff0',relief=RAISED,bitmap='gray25',command=show)
s1.place(x=740,y=375)
log=Button(window,bg='#B2beb5',text="Login",font=("Helvetica",15,'bold'),command=login)
log.place(x=500,y=430)
q = Button(window,bg='#B2beb5', text="Cancel", font=("Helvetica", 15, 'bold'), command=quit)
q.place(x=600, y=430)
window.mainloop()
