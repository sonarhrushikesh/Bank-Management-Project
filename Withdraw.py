from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from tkcalendar import DateEntry
import mysql.connector
from PIL import Image,ImageTk

win = Toplevel()
path = Image.open("d:\\Images\\withdraw.jpg")
render = ImageTk.PhotoImage(path)
img= Label(win, image=render)
img.pack(fill=BOTH,expand=True)
win.title("WITHDRAWL WIN")
win.geometry("900x650")

def new():
    mydb = mysql.connector.connect(host='localhost', user='root', password='', database='Bank', charset='utf8')
    mycur = mydb.cursor()
    mycur.execute("select max(slno) from withdraw ")
    data = mycur.fetchone()
    cnt = int(data[0])
    cnt = cnt + 1
    t1.delete(0, END)
    t1.insert(0, cnt)

def withdraw():
    s1 = t1.get()
    s2 = t2.get()
    s3 = t3.get()
    s4 = t4.get()
    s5 = t5.get()
    if s2 == "":
        messagebox.showwarning('Warning', 'Plz Enter sldate')
        return
    if s3 == "":
        messagebox.showwarning('Warning', 'Plz Enter apno')
        return
    if s4 == "":
        messagebox.showwarning('Warning', 'Plz Enter perticular method')
        return
    if s5 == "":
        messagebox.showwarning('Warning', 'Plz Enter amount')
        return
    #Opening Balence
    mydb = mysql.connector.connect(host='localhost', user='root', password='', database='Bank', charset='utf8')
    mycur = mydb.cursor()
    mycur.execute("select opbal from applicant where apno=" + s3)
    data = mycur.fetchone()
    for x in data:
        a = str(x)
    #After Deposition
    mydb = mysql.connector.connect(host='localhost', user='root', password='', database='Bank', charset='utf8')
    mycur = mydb.cursor()
    mycur.execute("select sum(amount) from deposit where apno=" + s3)
    data = mycur.fetchone()
    for y in data:
        if y is not None:
            b = str(y)
            c = int(a) + int(b)
        else:
            c=int(a)
    #after transition
    mydb = mysql.connector.connect(host='localhost', user='root', password='', database='Bank', charset='utf8')
    mycur = mydb.cursor()
    mycur.execute("select sum(amount) from withdraw where apno=" + s3)
    data = mycur.fetchone()
    for z in data:
        if z is not None:
            d = str(z)
            am = int(c) - int(d)
            ld.config(text=str(d))
            lc.config(text=str(am))
            if int(am)>int(s5):
                mydb = mysql.connector.connect(host='localhost', user='root', password='', database='Bank', charset='utf8')
                mycur = mydb.cursor()
                mycur.execute("insert into withdraw value('" + s1 + "','" + s2 + "'," + s3 + ",'" + s4 + "'," + s5 + ")")
                mydb.commit()
                messagebox.showinfo('confirm', 'Amount Withdraw Successfully')
                t1.delete(0, END)
                t2.delete(0, END)
                t3.delete(0, END)
                t4.delete(0, END)
                t5.delete(0, END)
                ls.config(text='')
                lc.config(text='')
                ld.config(text='')
            else:
                messagebox.showinfo('confirm', 'Insufficient Balence')
        else:
            if int(c)>int(s5):
                mydb = mysql.connector.connect(host='localhost', user='root', password='', database='Bank', charset='utf8')
                mycur = mydb.cursor()
                mycur.execute("insert into withdraw value('" + s1 + "','" + s2 + "'," + s3 + ",'" + s4 + "'," + s5 + ")")
                mydb.commit()
                messagebox.showinfo('confirm', 'Amount Withdraw Successfully')
                t1.delete(0, END)
                t2.delete(0, END)
                t3.delete(0, END)
                t4.delete(0, END)
                t5.delete(0, END)
                ls.config(text='')
                lc.config(text='')
                ld.config(text='')
            else:
                messagebox.showinfo('confirm', 'Insufficient Balence')


def info(*args):
    s3=t3.get()
    mydb = mysql.connector.connect(host='localhost', user='root', password='', database='Bank', charset='utf8')
    mycur = mydb.cursor()
    mycur.execute("select apname from applicant where apno="+s3)
    data=mycur.fetchone()
    for x in data:
        ls.config(text=str(x))
    #Opening Balence
    mydb = mysql.connector.connect(host='localhost', user='root', password='', database='Bank', charset='utf8')
    mycur = mydb.cursor()
    mycur.execute("select opbal from applicant where apno=" + s3)
    data = mycur.fetchone()
    for x in data:
        a = str(x)
    #After Deposition
    mydb = mysql.connector.connect(host='localhost', user='root', password='', database='Bank', charset='utf8')
    mycur = mydb.cursor()
    mycur.execute("select sum(amount) from deposit where apno=" + s3)
    data = mycur.fetchone()
    for y in data:
        if y is not None:
            b = str(y)
            c = int(a) + int(b)
        else:
            c=int(a)
    #Current Balence
    mydb = mysql.connector.connect(host='localhost', user='root', password='', database='Bank', charset='utf8')
    mycur = mydb.cursor()
    mycur.execute("select sum(amount) from withdraw where apno=" + s3)
    data = mycur.fetchone()
    for z in data:
        if z is not None:
            d = str(z)
            am = int(c) - int(d)
            ld.config(text=str(d))
            lc.config(text=str(am))
        else:
            ld.config(text='NONE')
            lc.config(text=str(c))

def ser():
    t2.delete(0, END)
    t3.delete(0, END)
    t4.delete(0, END)
    t5.delete(0, END)
    ls.config(text='')
    lc.config(text='')
    ld.config(text='')
    s1 = t1.get()
    mydb = mysql.connector.connect(host='localhost', user='root', password='', database='Bank', charset='utf8')
    mycur = mydb.cursor()
    mycur.execute("select * from withdraw where slno=" + s1)
    data = mycur.fetchone()
    if data is not None:
        t2.insert(0, data[1])
        t3.insert(0, data[2])
        t4.insert(0, data[3])
        t5.insert(0, data[4])
    else:
        messagebox.showinfo("warning", "rec is not found")
    s3 = t3.get()
    mydb = mysql.connector.connect(host='localhost', user='root', password='', database='Bank', charset='utf8')
    mycur = mydb.cursor()
    mycur.execute("select apname from applicant where apno=" + s3)
    data = mycur.fetchone()
    for x in data:
        ls.config(text=str(x))

def update():
    s1 = t1.get()
    s2 = t2.get()
    s3 = t3.get()
    s4 = t4.get()
    s5 = t5.get()
    if s2 == "":
        messagebox.showwarning('Warning', 'Plz Enter sldate')
        return
    if s3 == "":
        messagebox.showwarning('Warning', 'Plz Enter apno')
        return
    if s4 == "":
        messagebox.showwarning('Warning', 'Plz Enter perticular method')
        return
    if s5 == "":
        messagebox.showwarning('Warning', 'Plz Enter amount')
        return
    mydb = mysql.connector.connect(host='localhost', user='root', password='', database='Bank', charset='utf8')
    mycur = mydb.cursor()
    mycur.execute("update withdraw set sldate='" + s2 + "',apno=" + s3 + ",perticular='" + s4 + "',amount=" + s5 + " where slno=" + s1)
    mydb.commit()
    messagebox.showinfo('confirm', 'Withdrawl Slip Updated Successfully')
    t1.delete(0, END)
    t2.delete(0, END)
    t3.delete(0, END)
    t4.delete(0, END)
    t5.delete(0, END)
    ls.config(text='')
    lc.config(text='')
    ld.config(text='')

def cancel():
    res = messagebox.askyesno("Warning", "Are u sure?")
    if res == True:
        s1 = t1.get()
        mydb = mysql.connector.connect(host='localhost', user='root', password='', database='Bank', charset='utf8')
        mycur = mydb.cursor()
        mycur.execute("delete from withdraw where slno=" + s1)
        mydb.commit()
        messagebox.showinfo("Confirm", "Withdrawl Cancel")
        t1.delete(0, END)
        t2.delete(0, END)
        t3.delete(0, END)
        t4.delete(0, END)
        t5.delete(0, END)
        ls.config(text='')
        lc.config(text='')
        ld.config(text='')

def clear():
    t1.delete(0, END)
    t2.delete(0, END)
    t3.delete(0, END)
    t4.delete(0, END)
    t5.delete(0, END)
    ls.config(text='')
    lc.config(text='')
    ld.config(text='')

#For apno combobox
global d
mydb = mysql.connector.connect(host='localhost', user='root', password='', database='Bank', charset='utf8')
mycur = mydb.cursor()
mycur.execute("select apno from applicant")
data = mycur.fetchall()
d = []
for i in data:
    d.append(i)

#For particular
global p
p=['DEBIT CARD','CHECK','UPI','DD','NET BANKING']

c = Canvas(win, bg="Ivory",width='510', height="550")
c.place(x=135, y=40)

lo = Label(win, text='WITHDRAWL',bg='Ivory',fg='Black',width=15, font=("Arial", 22, 'bold'))
lo.place(x=250, y=50)
l1 = Label(win, text="Slno:", bg='Ivory',fg='Black', width=8, font=("Arial", 15))
l1.place(x=160, y=120)
l2 = Label(win, text="Sldate:", bg='Ivory',fg='Black',width=8, font=("Arial", 15))
l2.place(x=160, y=170)
l3 = Label(win, text="Apno:", bg='Ivory',fg='Black',width=8, font=("Arial", 15))
l3.place(x=160, y=220)
l4 = Label(win, text="Particular:", bg='Ivory',fg='Black',width=8, font=("Arial", 15))
l4.place(x=160, y=270)
l5 = Label(win, text="Amount:", bg='Ivory',fg='Black',width=8, font=("Arial", 15))
l5.place(x=160, y=320)

t1 = Entry(win, bd=3, width=27)
t1.place(x=270, y=125)
t2=DateEntry(win,selectmode='day',bd=3, width=22)
t2.place(x=270, y=175)
t3=Combobox(win,values=d,width=22)
t3.bind("<<ComboboxSelected>>",info)
t3.place(x=270, y=225)
t4 =Combobox(win,values=p,width=22,state='readonly')
t4.place(x=270, y=275)
t5 = Entry(win, bd=3, width=27)
t5.place(x=265, y=325)

#For Info
ls= Label(win,text='', bg='Ivory',fg='Black', font=("Arial", 12))
ls.place(x=440, y=220)
#Current Balence
lm=Label(win,text='Current Balence*:', bg='Ivory',fg='Black', font=("Arial", 14))
lm.place(x=165, y=365)
lc= Label(win,text='', bg='skyblue',fg='Black', font=("Arial", 12))
lc.place(x=320, y=368)
#For Withdrawl
lt=Label(win,text='Total Withdrawl*:', bg='Ivory',fg='Black', font=("Arial", 14))
lt.place(x=420, y=365)
ld= Label(win,text='', bg='Ivory',fg='Black', font=("Arial", 12))
ld.place(x=565, y=368)

b1 = Button(win, text="NEW", bg='#Ffb347',width=9, font=("Arial", 15, 'bold'),command=new)
b1.place(x=180, y=420)
b2 = Button(win, text="WITHDRAW",bg='#Ffb347', width=10,font=("Arial", 15, 'bold'),command=withdraw)
b2.place(x=310, y=420)
b3 = Button(win, text="SEARCH", bg='#Ffb347',width=9, font=("Arial", 15, 'bold'),command=ser)
b3.place(x=450, y=420)
b4 = Button(win, text="UPDATE",bg='#Ffb347',width=9, font=("Arial", 15, 'bold'),command=update)
b4.place(x=180, y=480)
b5 = Button(win, text="CANCEL", bg='#Ffb347',width=10, font=("Arial", 15, 'bold'),command=cancel)
b5.place(x=310, y=480)
b6 = Button(win, text="EXIT", bg='#Ffb347',width=9, font=("Arial", 15, 'bold'),command=win.destroy)
b6.place(x=450, y=480)
b7 = Button(win, text="CLEAR", bg='#Ffb347',width=10, font=("Arial", 15, 'bold'),command=clear)
b7.place(x=310, y=540)

win.mainloop()