# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 11:04:19 2025

@author: 91749
"""

import tkinter as tk 
import tkinter
import sqlite3
import random
from tkinter import messagebox as ms
from PIL import Image,ImageTk
from tkinter.ttk import *

root=tk.Tk()
root.configure(background='white')

w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w,h))
root.title("Login Page")

image2=Image.open('./img/img4.jpg')
image2=image2.resize((w,h),Image.LANCZOS)

background_image = ImageTk.PhotoImage(image2)
background_label = tk.Label(root,image=background_image)
background_label.image = background_image
background_label.place(x=0,y=0)

#############################################################################################################


Email = tk.StringVar()
password = tk.StringVar() 
 
def login():
 

    with sqlite3.connect('./db/knee.db') as db:
         c = db.cursor()

        
         db = sqlite3.connect('./db/knee.db')
         cursor = db.cursor()
         cursor.execute("CREATE TABLE IF NOT EXISTS KneeReg"
                        "(name TEXT, address TEXT,  Email TEXT, country TEXT, Phoneno TEXT, Gender TEXT, password TEXT)")
         db.commit()
         
         
         find_entry = ('SELECT * FROM KneeReg WHERE Email = ? and password = ?')
         
         c.execute(find_entry, [(Email.get()), (password.get())])
         result = c.fetchall()
         if result:
            msg = ""
          
            print(msg)
            ms.showinfo("messege", "Login sucessfully")
            

            from subprocess import call
            call(['python','GUI_MASTER.py'])
            
           
         
         else:
           ms.showerror('Oops!', 'Username Or Password Did Not Found/Match.')





# New_Password=tk.StringVar()
# def forget():
#     con=sqlite3.connect("project11.db")
#     con.execute("""
#                 update registration set New_Password= Password where pass)

###############################################################################################################



a11=tk. Label(root,text='Login Here ',fg='black',bg ='Light gray',font=('Cambria',25)).place(x=200,y=50)

canvas1=tk.Canvas(root,background="light gray")
canvas1.place(x=50,y=100,widt=500,height=400)

#login=Label(root,text="Login",font=('Arial',25),foreground='green').place(x=270,y=350)
a11=tk. Label(root,text='Enter Email',bg='light gray',font=('Cambria',14)).place(x=100,y=140)
a12=tk. Label(root,text='Enter Password',bg='light gray',font=('Cambria',14)).place(x=100,y=180)

b11=tk.Entry(root,width=40, textvariable=Email).place(x=270,y=140,)
b12=tk. Entry(root,width=40,show='*', textvariable=password).place(x=270,y=180,)


def forgot():
    from subprocess import call
    call(['python','forgot password.py'])
    
def home():
    from subprocess import call
    call(['python','Gui_main.py'])


button2=tk.Button(root,text="Forgot Password?",fg='blue',bg='light gray',command=forgot)
button2.place(x=400,y=230)



button2=tk.Button(root,text="Login",font=("Bold",9),command=login,width=50,bg='light gray')
button2.place(x=130,y=360)

a=tk. Label(root,text='Not a Member?',font=('Cambria',11),bg='light gray').place(x=270,y=400)

def reg():
    from subprocess import call
    call(['python','registration.py'])

button1=tk.Button(root,text="Sign up",fg='blue',bg='light gray',command=reg)
button1.place(x=230,y=450,width=55)

button1=tk.Button(root,text="Home",fg='blue',bg='light gray',command=home)
button1.place(x=330,y=450,width=55)



root.mainloop()