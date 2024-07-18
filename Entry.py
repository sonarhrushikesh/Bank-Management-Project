from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from tkcalendar import DateEntry
from dateutil.relativedelta import relativedelta
from datetime import date,datetime
import mysql.connector
from PIL import Image,ImageTk

win1 = Toplevel()

path = Image.open("d:\\Images\\entrypage.jpg")
render = ImageTk.PhotoImage(path)
img= Label(win1, image=render)
img.pack(fill=BOTH,expand=True)
win1.title("ENTRY WIN")
win1.geometry("1000x700")


def new():
    mydb = mysql.connector.connect(host='localhost', user='root', password='', database='bank', charset='utf8')
    mycur = mydb.cursor()
    mycur.execute("select max(apno) from applicant ")
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
    s6 = t6.get()
    s7 = t7.get()
    s8 = t8.get()
    s9 = t9.get()
    s10 =t10.get()

    if s2 == "":
        messagebox.showwarning('Warning', 'Plz Enter apname')
        return
    if s3 == "":
        messagebox.showwarning('Warning', 'Plz Enter apadd')
        return
    if s4 == "":
        messagebox.showwarning('Warning', 'Plz Enter city')
        return
    if s5 == "" or len(s5) < 10 or len(s5) > 11:
        messagebox.showwarning('Warning', 'Plz Enter contact')
        return
    if s6 == "":
        messagebox.showwarning('Warning', 'Plz Enter bdate')
        return
    if s7 == "":
        messagebox.showwarning('Warning', 'Plz Enter age')
        return
    if s8 == "":
        messagebox.showwarning('Warning', 'Plz Enter gender')
        return
    if s9 == "":
        messagebox.showwarning('Warning', 'Plz Enter nomini')
        return
    if s10 == "":
        messagebox.showwarning('Warning', 'Plz Enter opbal')
        return

    mydb = mysql.connector.connect(host='localhost', user='root', password='', database='Bank', charset='utf8')
    mycur = mydb.cursor()
    mycur.execute("insert into applicant value(" + s1 + ",'" + s2 + "','" + s3 + "','" + s4 + "','" + s5 + "','" + s6 + "'," + s7 + ",'" + s8 + "','" + s9 + "'," + s10 + ")")
    mydb.commit()
    messagebox.showinfo('confirm', 'rec is save')
    t1.delete(0, END)
    t2.delete(0, END)
    t3.delete(0, END)
    t4.delete(0, END)
    t5.delete(0, END)
    t6.delete(0, END)
    t7.delete(0, END)
    t8.delete(0, END)
    t9.delete(0, END)
    t10.delete(0, END)

def ser():
    t2.delete(0, END)
    t3.delete(0, END)
    t4.delete(0, END)
    t5.delete(0, END)
    t6.delete(0, END)
    t7.delete(0, END)
    t8.delete(0, END)
    t9.delete(0, END)
    t10.delete(0, END)
    s1 = t1.get()
    mydb = mysql.connector.connect(host='localhost', user='root', password='', database='Bank', charset='utf8')
    mycur = mydb.cursor()
    mycur.execute("select * from applicant where apno=" + s1)
    data = mycur.fetchone()
    if data is not None:
        t2.insert(0, data[1])
        t3.insert(0, data[2])
        t4.insert(0, data[3])
        t5.insert(0, data[4])
        t6.insert(0, data[5])
        t7.insert(0, data[6])
        t8.insert(0, data[7])
        t9.insert(0, data[8])
        t10.insert(0, data[9])
    else:
        messagebox.showinfo("warning", "rec is not found")

def update():
    s1 = t1.get()
    s2 = t2.get()
    s3 = t3.get()
    s4 = t4.get()
    s5 = t5.get()
    s6 = t6.get()
    s7 = t7.get()
    s8 = t8.get()
    s9 = t9.get()
    s10 = t10.get()

    if s2 == "":
        messagebox.showwarning('Warning', 'Plz Enter apname')
        return
    if s3 == "":
        messagebox.showwarning('Warning', 'Plz Enter apadd')
        return
    if s4 == "":
        messagebox.showwarning('Warning', 'Plz Enter city')
        return
    if s5 == "" or len(s5) < 10 or len(s5) > 11:
        messagebox.showwarning('Warning', 'Plz Enter contact')
        return
    if s6 == "":
        messagebox.showwarning('Warning', 'Plz Enter bdate')
        return
    if s7 == "":
        messagebox.showwarning('Warning', 'Plz Enter age')
        return
    if s8 == "":
        messagebox.showwarning('Warning', 'Plz Enter gender')
        return
    if s9 == "":
        messagebox.showwarning('Warning', 'Plz Enter nomini')
        return
    if s10 == "":
        messagebox.showwarning('Warning', 'Plz Enter opbal')
        return

    mydb = mysql.connector.connect(host='localhost', user='root', password='', database='Bank', charset='utf8')
    mycur = mydb.cursor()
    mycur.execute("update applicant set apname='" + s2 + "',apadd='" + s3 + "',city='" + s4 + "',contact='" + s5 + "',bdate='" + s6 + "',age=" + s7 + ",gender='" + s8 + "',nomini='" + s9 + "',opbal=" + s10 + " where apno=" + s1)
    mydb.commit()
    messagebox.showinfo('confirm', 'rec is update')
    t1.delete(0, END)
    t2.delete(0, END)
    t3.delete(0, END)
    t4.delete(0, END)
    t5.delete(0, END)
    t6.delete(0, END)
    t7.delete(0, END)
    t8.delete(0, END)
    t9.delete(0, END)
    t10.delete(0, END)

def delete():
    res = messagebox.askyesno("Warning", "Are u sure?")
    if res == True:
        s1 = t1.get()
        mydb = mysql.connector.connect(host='localhost', user='root', password='', database='Bank', charset='utf8')
        mycur = mydb.cursor()
        mycur.execute("delete from applicant where apno=" + s1)
        mydb.commit()
        messagebox.showinfo("Confirm", "rec is delete")
        t1.delete(0, END)
        t2.delete(0, END)
        t3.delete(0, END)
        t4.delete(0, END)
        t5.delete(0, END)
        t6.delete(0, END)
        t7.delete(0, END)
        t8.delete(0, END)
        t9.delete(0, END)
        t10.delete(0, END)

def clear():
        t1.delete(0, END)
        t2.delete(0, END)
        t3.delete(0, END)
        t4.delete(0, END)
        t5.delete(0, END)
        t6.delete(0, END)
        t7.delete(0, END)
        t8.delete(0, END)
        t9.delete(0, END)
        t10.delete(0, END)
        ld.config(text='')

d=['Male','Female'] #For Gender
#For Age Calculation:
global v1
v1=StringVar()
def age(*args):
    if(len(v1.get())>4):
        dob = datetime.strptime(v1.get(),'%m/%d/%y')
        dt=date.today()
        dt3=relativedelta(dt,dob)
        ld.config(text="Days:" + str(dt3.days) +"\n Months:"+ str(dt3.months) + "\n Years:"+ str(dt3.years) )

#For Design
c = Canvas(win1, bg="#fdd6e5",width='470', height="600")
c.place(x=135, y=40)

#Age Calculation Label
lc=Label(win1,text="mm/dd/yy",bg='#fdd6e5',fg='black')
lc.place(x=410, y=385)
ld=Label(win1,bg='#fdd6e5',fg='black')
ld.place(x=480, y=385)
v1.trace('w',age)


lo = Label(win1, text='Applicant Entry Form',bg='#fdd6e5',fg='black', font=("Arial", 20, 'bold'))
lo.place(x=230, y=60)
l1 = Label(win1, text="Apno", bg='#fdd6e5',fg='Black', width=8, font=("Arial", 15))
l1.place(x=150, y=130)
l2 = Label(win1, text="Apname", bg='#fdd6e5',fg='Black',width=8, font=("Arial", 15))
l2.place(x=150, y=180)
l3 = Label(win1, text="Apadd", bg='#fdd6e5',fg='Black',width=8, font=("Arial", 15))
l3.place(x=150, y=230)
l4 = Label(win1, text="City", bg='#fdd6e5',fg='Black',width=8, font=("Arial", 15))
l4.place(x=150, y=280)
l5 = Label(win1, text="Contact", bg='#fdd6e5',fg='Black',width=8, font=("Arial", 15))
l5.place(x=150, y=330)
l6 = Label(win1, text="Bdate", bg='#fdd6e5',fg='Black',width=8, font=("Arial", 15))
l6.place(x=150, y=380)
l7 = Label(win1, text="Age", bg='#fdd6e5',fg='Black',width=8, font=("Arial", 15))
l7.place(x=150, y=430)
l8 = Label(win1, text="Gender", bg='#fdd6e5',fg='Black',width=8, font=("Arial", 15))
l8.place(x=150, y=480)
l9 = Label(win1, text="Nomini", bg='#fdd6e5',fg='Black',width=8, font=("Arial", 15))
l9.place(x=150, y=540)
l10 = Label(win1, text="Opbal", bg='#fdd6e5',fg='Black',width=8, font=("Arial", 15))
l10.place(x=150, y=590)


t1 = Entry(win1, bd=3, width=50)
t1.place(x=260, y=135)
t2 = Entry(win1, bd=3, width=50)
t2.place(x=260, y=185)
t3 = Entry(win1, bd=3, width=50)
t3.place(x=260, y=235)
t4 = Entry(win1, bd=3, width=50)
t4.place(x=260, y=285)
t5 = Entry(win1, bd=3, width=50)
t5.place(x=260, y=335)
t6=DateEntry(win1,selectmode='day',textvariable=v1,bd=3, width=20)
t6.place(x=260, y=385)
t7 = Entry(win1, bd=3, width=23)
t7.place(x=260, y=435)
t8=Combobox(win1,values=d,width=20,state='readonly')
t8.place(x=260, y=485)
t9 = Entry(win1, bd=3, width=50)
t9.place(x=260, y=545)
t10 = Entry(win1, bd=3, width=50)
t10.place(x=260, y=595)

b1 = Button(win1, text="  NEW ", bg='#EFFD5F',width=8, font=("Arial", 15, 'bold'),command=new)
b1.place(x=650, y=200)
b2 = Button(win1, text=" SAVE ",bg='#EFFD5F', width=8,font=("Arial", 15, 'bold'),command=save)
b2.place(x=770, y=200)
b3 = Button(win1, text="  SER ", bg='#EFFD5F',width=8, font=("Arial", 15, 'bold'),command=ser)
b3.place(x=650, y=270)
b4 = Button(win1, text="UPDATE",bg='#EFFD5F',width=8, font=("Arial", 15, 'bold'),command=update)
b4.place(x=770, y=270)
b5 = Button(win1, text="DELETE", bg='#EFFD5F',width=8, font=("Arial", 15, 'bold'),command=delete)
b5.place(x=650, y=340)
b6 = Button(win1, text=" EXIT ", bg='#EFFD5F',width=8, font=("Arial", 15, 'bold'),command=win1.destroy)
b6.place(x=770, y=340)
b7 = Button(win1, text=" CLEAR", bg='#EFFD5F',width=8, font=("Arial", 15, 'bold'),command=clear)
b7.place(x=700, y=410)
win1.mainloop()