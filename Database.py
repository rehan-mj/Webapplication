####import mysql.connector
####
####mydb = mysql.connector.connect(
####  host="localhost",
####  user="root",
####  passwd="1234"
####)
####
####mycursor = mydb.cursor()
####
####mycursor.execute("SHOW DATABASES")
####
####for x in mycursor:
####  print(x)


##import mysql.connector
##import pymysql
##from tkinter import *
##from tkinter import messagebox
##
##def search():
##    try:
##        con=pymysql.connect(user='root', password='1234', \
##                            host='localhost', database='db')
##        cur=con.cursor()
##        sql="select * from student where rollno='%s'"%rollno.get()
##        cur.execute(sql)
##        result=cur.fetchone()
##        name.set(result[1])
##        age.set(result[2])
##        e1.configure(state='disable')
##        con.close()
##    except:
##        mwssagebox.showinfo('No Data', 'No such data available..')
##        clear()
##
##def clear():
##    rollno.set('')
##    name.set('')
##    age.set('')
##    e1.configure(state='normal')
##
##def add():
##    try:
##        con=pymysql.connect(user='root', password='1234', \
##                            host='localhost', database='db')
##        cur=con.cursor()
##        sql="insert into student values('%s','%s',%s)"\
##             %(rollno.get(), name.get(), age.get())
##        cur.execute(sql)
##        con.commit()
##        con.close()
##        messagebox.showinfo('Success','Record saved...')
##    except:
##        messagebox.showinfo('Error','Error in data entry...')
##    finally:
##        clear()
##
##
##def update():
##    try:
##        con=pymysql.connect(user='root', password='1234', \
##                            host='localhost', database='db')
##        cur=con.cursor()
##        sql="update student set name='%s where rollno='%s'"\
##             %(name.get(), age.get(), rollno.get())
##        cur.execute(sql)
##        con.commit()
##        con.close()
##        messagebox.showinfo('Success','Record updated...')
##    except:
##        messagebox.showinfo('Error','Error occured...')
##    finally:
##        clear()
##
##def delete():
##    try:
##        con=pymysql.connect(user='root', password='shajida', \
##                            host='localhost', database='db')
##        cur=con.cursor()
##        sql="delete from student where rollno='%s'"\
##             %(rollno.get())
##        cur.execute(sql)
##        con.commit()
##        con.close()
##        messagebox.showinfo('Success','Record deleted...')
##    except:
##        messagebox.showinfo('Error','Error occured...')
##    finally:
##        clear()
##
##w1=Tk()
##w1.title("MyApp")
##
##w1.geometry('500x200')
##ptitle=Lable(w1, text='''Program to add, delete and modify the records from the student table''')
##ptitle.grid(row=0, column=0, columnspan=2)
##
##rollno=StringVar()
##name=StringVar()
##age=StringVar()
##
##l1=Label(w1, text=' RollNo ')
##e1=Entry(w1, textvariable=rollno)
##l2=Label(w1, text=' Name ')
##e2=Entry(w1, textvariable=name)
##l3=Label(w1, text=' Age ')
##e3=Entry(w1, textvariable=age)
##
##b1=Button(w1, text=' Search ', command=search)
##b2=Button(w1, text=' Age ', command=sage)
##b3=Button(w1, text=' Update ', command=supdate)
##b4=Button(w1, text=' Delete ', command=delete)
##b5=Button(w1, text=' Clear ', command=clear)
##
##l1.grid(row=1, column=0)
##e1.grid(row=1, column=1)
##b1.grid(row=1, column=2)
##
##l2.grid(row=2, column=0)
##e2.grid(row=2, column=1)
##
##l3.grid(row=3, column=0)
##e3.grid(row=3, column=1)
##
##b2.grid(row=4, column=0)
##b3.grid(row=4, column=1)
##
##b4.grid(row=5, column=0)
##e5.grid(row=5, column=1)
##w1.mainloop()


##
import mysql.connector
import pymysql
from tkinter import *
from tkinter import messagebox


def search():
    try:
        con=pymysql.connect(user='root', password='1234', \
                            host='localhost', database='db')
        cur=con.cursor()
        sql="select * from bhavin where firstname='%s'"%fnametext.get()
        cur.execute(sql)
        result=cur.fetchone()
##        fnametext.set(result[1])
        lnametext.set(result[1])
        e1.configure(state='disable')
        con.close()
    except:
        messagebox.showinfo('No Data', 'No such data available..')
        clear()

def clear():
    fnametext.set('')
    lnametext.set('')
    e1.configure(state='normal')

def add():
    try:
        con=pymysql.connect(user='root', password='1234', \
                            host='localhost', database='db')
        cur=con.cursor()
        sql="insert into bhavin values('%s','%s')"\
             %(fnametext.get(), lnametext.get())
        cur.execute(sql)
        con.commit()
        con.close()
        messagebox.showinfo('Success','Record saved...')
    except:
        messagebox.showinfo('Error','Error in data entry...')
    finally:
        clear()


def update():
    try:
        con=pymysql.connect(user='root', password='1234', \
                            host='localhost', database='db')
        cur=con.cursor()
        sql="UPDATE SIDDHU_TEST SET LNAME = ‘%s'” % (fnametext.get) +” WHERE FNAME = ‘%s'” % (lnametext.get)
        cur.execute(sql)
        con.commit()
        con.close()
        messagebox.showinfo('Success','Record updated...')
    except:
        messagebox.showinfo('Error','Error occured...')
    finally:
        clear()

def delete():
    try:
        con=pymysql.connect(user='root', password='shajida', \
                            host='localhost', database='db')
        cur=con.cursor()
        sql="delete from bhavin where firstname=('%s')"\
             %(fnametext.get())
        cur.execute(sql)
        con.commit()
        con.close()
        messagebox.showinfo('Success','Record deleted...')
    except:
        messagebox.showinfo('Error','Error occured...')
    finally:
        clear()

w1=Tk()
w1.title("MyApp")

w1.geometry('500x200')



l1=Label(w1,text='First Name')
l1.grid(row=0,column=0)

l2=Label(w1,text='Last Name')
l2.grid(row=2,column=0)

fnametext=StringVar()
e1=Entry(w1,textvariable=fnametext)
e1.grid(row=0,column=1)

lnametext=StringVar()
e2=Entry(w1,textvariable=lnametext)
e2.grid(row=2,column=1)




b1=Button(w1, text=' Search ',command=search)
b2=Button(w1, text=' Insert ', command=add)
b3=Button(w1, text=' Update ', command=update)
b4=Button(w1, text=' Delete ', command=delete)
b5=Button(w1, text=' Clear ', command=clear)

b1.grid(row=6, column=0)

b2.grid(row=6, column=1)

b3.grid(row=6, column=2)

b4.grid(row=6, column=3)

b5.grid(row=6, column=4)


w1.mainloop()
























