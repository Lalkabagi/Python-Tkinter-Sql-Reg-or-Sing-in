import tkinter as tk
from tkinter import messagebox
from tkinter import *
import pymysql

w = tk.Tk() 
connection = pymysql.connect(
                                host='localhost',
                                database='tksql',
                                user='root',
                                password='',
                                cursorclass=pymysql.cursors.DictCursor)

cursor = connection.cursor()  



def Button2():
        w.destroy()
        w1 = tk.Tk()
        w1.title("Register")

        def Button3():
                if e.get() !='' and e2.get() !='' and e3.get() !='':
                        if e2.get() == e3.get():
                                cursor.execute('INSERT INTO regtk (login,password) VALUES ("{}","{}")'.format(e.get(),e2.get()))
                                connection.commit()
                        else:
                                messagebox.showerror('Error','you entered the password incorrectly')        
                else:
                        messagebox.showerror('Error','The line is empty')

        frame = tk.Frame(master = w1,width = 50,height = 100,bg = "green")
        frame.pack(fill = tk.BOTH,expand = True)

        l = tk.Label(master = frame,text = "Please enter your login:",bg = "green",fg = "white")
        l.grid(row = 0 ,column = 1,padx = 10,pady = 10)

        e = tk.Entry(master = frame,width = 15)
        e.grid(row = 0 ,column = 3,padx = 10,pady = 10)

        l2 = tk.Label(master = frame,text = "Please enter your password:",bg = "green",fg = "white")
        l2.grid(row = 1 ,column = 1,padx = 10,pady = 10)

        e2 = tk.Entry(master = frame,width = 15)
        e2.grid(row = 1 ,column = 3,padx = 10,pady = 10)

        l3 = tk.Label(master = frame,text = "Repeat your password:",bg = "green",fg = "white")
        l3.grid(row = 2 ,column = 1,padx = 10,pady = 10)

        e3 = tk.Entry(master = frame,width = 15)
        e3.grid(row = 2 ,column = 3,padx = 10,pady = 10)

        frame1 = tk.Frame(master = w1,width = 600,height = 600,bg = "green")
        frame1.pack(fill = tk.BOTH,expand = True)

        b3 = tk.Button(master = frame1,text = "Register",width = 30,command = Button3)
        b3.pack()

        w1.mainloop()

def Button1():
        w.destroy()
        w2 = tk.Tk()
        w2.title("Log in")
        def Button4():
                log = e4.get()
                pas = e5.get()
                singin = cursor.execute('SELECT login,password FROM regtk WHERE login = %s and password = %s',(log,pas))
                if e4.get() !='' and e5.get() !='':
                        if cursor.fetchone():
                                messagebox.showinfo('INFORMATION','You is Sing in')
                        else:
                                messagebox.showinfo('INFORMATION','You is not Sing in')
                else:
                        messagebox.showinfo('The line is Empty')

        frame3 = tk.Frame(master = w2,width = 50,height = 100,bg = "green")
        frame3.pack(fill = tk.BOTH,expand = True)

        l4 = tk.Label(master = frame3,text = "Please enter your login:",bg = "green",fg = "white")
        l4.grid(row = 0 ,column = 1,padx = 10,pady = 10)

        e4 = tk.Entry(master = frame3,width = 15)
        e4.grid(row = 0 ,column = 3,padx = 10,pady = 10)

        l5 = tk.Label(master = frame3,text = "Please enter your password:",bg = "green",fg = "white")
        l5.grid(row = 1 ,column = 1,padx = 10,pady = 10)

        e5 = tk.Entry(master = frame3,width = 15)
        e5.grid(row = 1 ,column = 3,padx = 10,pady = 10)

        frame4 = tk.Frame(master = w2,width = 600,height = 600,bg = "green")
        frame4.pack(fill = tk.BOTH,expand = True)

        b4 = tk.Button(master = frame4,text = "Sing in",width = 30,command = Button4)
        b4.pack()

        w2.mainloop()



f2 = tk.Frame(master = w, width =300, height = 300, bg = "green")
f2.pack(fill = tk.BOTH,expand = True)

b2 = tk.Button(master = f2,text = "Register",width = 100,height = 5,command = Button2)
b2.pack(side = tk.TOP)

f = tk.Frame(master = w, width =300, height = 300, bg = "green")
f.pack(fill = tk.BOTH,expand = True)

b1 = tk.Button(master = f,text = "Log in",width = 100,height = 5,command = Button1)
b1.pack(side = tk.TOP)

w.mainloop()

cursor.close()