from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from tkcalendar import DateEntry
import mysql.connector
from PIL import Image,ImageTk

win = Toplevel()
path = Image.open("d:\\Images\\Interest.jpg")
render = ImageTk.PhotoImage(path)
img= Label(win, image=render)
img.pack(fill=BOTH,expand=True)
win.title("INTEREST WIN")
win.geometry("900x650")

def new():
    mydb = mysql.connector.connect(host='localhost', user='root', password='', database='Bank', charset='utf8')
    mycur = mydb.cursor()
    mycur.execute("select max(trno) from interest ")
    data = mycur.fetchone()
    cnt = int(data[0])
    cnt = cnt + 1
    t1.delete(0, END)
    t1.insert(0, cnt)

def save():
    s1 = t1.get()
    s2 = t2.get()
    s3 = t3.get()
    s4 = t4.get()
    s5 = t5.get()
    s6 = t6.cget("text")
    if s2 == "":
        messagebox.showwarning('Warning', 'Plz Enter trdate')
        return
    if s3 == "":
        messagebox.showwarning('Warning', 'Plz Enter apno')
        return
    if s4 == "":
        messagebox.showwarning('Warning', 'Plz Enter ifrom')
        return
    if s5 == "":
        messagebox.showwarning('Warning', 'Plz Enter ito')
        return
    mydb = mysql.connector.connect(host='localhost', user='root', password='', database='Bank', charset='utf8')
    mycur = mydb.cursor()
    mycur.execute("insert into interest value('" + s1 + "','" + s2 + "'," + s3 + ",'" + s4 + "','" + s5 + "'," + s6 + ")")
    mydb.commit()
    messagebox.showinfo('confirm', 'Interest amount added successfully')
    t1.delete(0, END)
    t2.delete(0, END)
    t3.delete(0, END)
    t4.delete(0, END)
    t5.delete(0, END)
    t6.config(text='')
    ls.config(text='')

def info(*args):
    s3=t3.get()
    mydb = mysql.connector.connect(host='localhost', user='root', password='', database='Bank', charset='utf8')
    mycur = mydb.cursor()
    mycur.execute("select apname from applicant where apno="+s3)
    data=mycur.fetchone()
    for x in data:
        ls.config(text=str(x))

    t6.config(text='')
    # Opening Balence
    mydb = mysql.connector.connect(host='localhost', user='root', password='', database='Bank', charset='utf8')
    mycur = mydb.cursor()
    mycur.execute("select opbal from applicant where apno=" + s3)
    data = mycur.fetchone()
    for x in data:
        a = str(x)
    # After Deposition
    mydb = mysql.connector.connect(host='localhost', user='root', password='', database='Bank', charset='utf8')
    mycur = mydb.cursor()
    mycur.execute("select sum(amount) from deposit where apno=" + s3)
    data = mycur.fetchone()
    for y in data:
        if y is not None:
            b = str(y)
            c = int(a) + int(b)
        else:
            c = int(a)
    # Current Balence
    mydb = mysql.connector.connect(host='localhost', user='root', password='', database='Bank', charset='utf8')
    mycur = mydb.cursor()
    mycur.execute("select sum(amount) from withdraw where apno=" + s3)
    data = mycur.fetchone()
    for z in data:
        if z is not None:
            d = str(z)
            am = int(c) - int(d)
        else:
            am = int(c)
    n = 1
    r = 5
    si = float(am * n * r) / 100
    t6.config(text=str(si))


def ser():
    t2.delete(0, END)
    t3.delete(0, END)
    t4.delete(0, END)
    t5.delete(0, END)
    t6.config(text='')
    ls.config(text='')
    s1 = t1.get()
    mydb = mysql.connector.connect(host='localhost', user='root', password='', database='Bank', charset='utf8')
    mycur = mydb.cursor()
    mycur.execute("select * from interest where trno=" + s1)
    data = mycur.fetchone()
    if data is not None:
        t2.insert(0, data[1])
        t3.insert(0, data[2])
        t4.insert(0, data[3])
        t5.insert(0, data[4])
    else:
        messagebox.showinfo("warning", "rec is not found")
    mycur.execute("select interest from interest where trno=" + s1)
    data = mycur.fetchone()
    t6.config(text=data)
    s3 = t3.get()
    mydb = mysql.connector.connect(host='localhost', user='root', password='', database='Bank', charset='utf8')
    mycur = mydb.cursor()
    mycur.execute("select apname from applicant where apno=" + s3)
    data = mycur.fetchone()
    for i in data:
        ls.config(text=str(i))


def update():
    s1 = t1.get()
    s2 = t2.get()
    s3 = t3.get()
    s4 = t4.get()
    s5 = t5.get()
    s6 = t6.cget("text")
    if s2 == "":
        messagebox.showwarning('Warning', 'Plz Enter trdate')
        return
    if s3 == "":
        messagebox.showwarning('Warning', 'Plz Enter apno')
        return
    if s4 == "":
        messagebox.showwarning('Warning', 'Plz Enter ifrom')
        return
    if s5 == "":
        messagebox.showwarning('Warning', 'Plz Enter ito')
        return
    mydb = mysql.connector.connect(host='localhost', user='root', password='', database='Bank', charset='utf8')
    mycur = mydb.cursor()
    mycur.execute("update interest set trdate='" + s2 + "',apno=" + s3 + ",ifrom='" + s4 + "',ito='" + s5 + "' where trno=" + s1)
    mydb.commit()
    messagebox.showinfo('confirm', 'Slip Updated Successfully')
    t1.delete(0, END)
    t2.delete(0, END)
    t3.delete(0, END)
    t4.delete(0, END)
    t5.delete(0, END)
    t6.config(text='')
    ls.config(text='')


def cancel():
    res = messagebox.askyesno("Warning", "Are u sure?")
    if res == True:
        s1 = t1.get()
        mydb = mysql.connector.connect(host='localhost', user='root', password='', database='Bank', charset='utf8')
        mycur = mydb.cursor()
        mycur.execute("delete from interest where trno=" + s1)
        mydb.commit()
        messagebox.showinfo("Confirm", "Interest Cancel")
        t1.delete(0, END)
        t2.delete(0, END)
        t3.delete(0, END)
        t4.delete(0, END)
        t5.delete(0, END)
        t6.config(text='')
        ls.config(text='')


def clear():
    t1.delete(0, END)
    t2.delete(0, END)
    t3.delete(0, END)
    t4.delete(0, END)
    t5.delete(0, END)
    t6.config(text='')
    ls.config(text='')

#For apno combobox
global d
mydb = mysql.connector.connect(host='localhost', user='root', password='', database='Bank', charset='utf8')
mycur = mydb.cursor()
mycur.execute("select apno from applicant")
data = mycur.fetchall()
d = []
for i in data:
    d.append(i)

c = Canvas(win, bg="honeydew",width='480', height="580")
c.place(x=135, y=40)

lo = Label(win, text='INTEREST SEC', bg='honeydew', fg='Black', width=15, font=("Arial", 22, 'bold'))
lo.place(x=250, y=50)
l1 = Label(win, text="Trno:", bg='honeydew', fg='Black', width=8, font=("Arial", 15))
l1.place(x=160, y=120)
l2 = Label(win, text="Trdate:", bg='honeydew', fg='Black', width=8, font=("Arial", 15))
l2.place(x=160, y=170)
l3 = Label(win, text="Apno:", bg='honeydew', fg='Black', width=8, font=("Arial", 15))
l3.place(x=160, y=220)
lw = Label(win, text="Interest span should be 1 year", bg='honeydew', fg='Black', font=("Arial", 11))
lw.place(x=250, y=255)
l4 = Label(win, text="Ifrom:", bg='honeydew', fg='Black', width=8, font=("Arial", 15))
l4.place(x=160, y=280)
l5 = Label(win, text="Ito:", bg='honeydew', fg='Black', width=8, font=("Arial", 15))
l5.place(x=160, y=330)
l5 = Label(win, text="Interest:", bg='honeydew', fg='Black', width=8, font=("Arial", 15))
l5.place(x=160, y=380)

t1 = Entry(win, bd=3, width=27)
t1.place(x=270, y=125)
t2 = DateEntry(win, selectmode='day', bd=3, width=22)
t2.place(x=270, y=175)
t3 = Combobox(win, values=d, width=22)
t3.bind("<<ComboboxSelected>>",info)
t3.place(x=270, y=225)
t4 = DateEntry(win, selectmode='day', bd=3, width=22)
t4.place(x=270, y=285)
t5 = DateEntry(win, selectmode='day', bd=3, width=22)
t5.place(x=270, y=335)
t6 =Label(win, text="", bg='honeydew', fg='Black', font=("Arial", 12))
t6.place(x=270, y=385)

#For Info
ls= Label(win,text='', bg='honeydew',fg='Black', font=("Arial", 12))
ls.place(x=440, y=222)

b1 = Button(win, text="NEW", bg='#Fbceb1',width=9, font=("Arial", 15, 'bold'),command=new)
b1.place(x=180, y=460)
b2 = Button(win, text="SAVE",bg='#Fbceb1', width=9,font=("Arial", 15, 'bold'),command=save)
b2.place(x=310, y=460)
b3 = Button(win, text="SEARCH", bg='#Fbceb1',width=9, font=("Arial", 15, 'bold'),command=ser)
b3.place(x=440, y=460)
b4 = Button(win, text="UPDATE",bg='#Fbceb1',width=9, font=("Arial", 15, 'bold'),command=update)
b4.place(x=180, y=515)
b5 = Button(win, text="CANCEL", bg='#Fbceb1',width=9, font=("Arial", 15, 'bold'),command=cancel)
b5.place(x=310, y=515)
b6 = Button(win, text="EXIT", bg='#Fbceb1',width=9, font=("Arial", 15, 'bold'),command=win.destroy)
b6.place(x=440, y=515)
b7 = Button(win, text="CLEAR", bg='#Fbceb1',width=9, font=("Arial", 15, 'bold'),command=clear)
b7.place(x=310, y=565)


win.mainloop()