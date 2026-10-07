import tkinter
import tkinter as tk
import sqlite3
import random
from tkinter import messagebox as ms
from PIL import Image, ImageTk
import re

root = tk.Tk()
root.configure(background='white')
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Registration Page")

image2 = Image.open('../img/img2.jpg')
image2 = image2.resize((w, h), Image.LANCZOS)
background_image = ImageTk.PhotoImage(image2)
background_label = tk.Label(root, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0)

name = tk.StringVar()
address = tk.StringVar()
Email = tk.StringVar()
country = tk.StringVar()
PhoneNo = tk.IntVar()
var = tk.IntVar()
password = tk.StringVar()
password1 = tk.StringVar()

db = sqlite3.connect('../db/knee.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS KneeReg"
               "(name TEXT, address TEXT, Email TEXT, country TEXT, Phoneno TEXT, Gender TEXT, password TEXT)")
db.commit()

def password_check(passwd):
    SpecialSym = ['$', '@', '#', '%']
    val = True
    if len(passwd) < 6:
        print('length should be at least 6')
        val = False
    if len(passwd) > 20:
        print('length should be not be greater than 20')
        val = False
    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral')
        val = False
    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        val = False
    if not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter')
        val = False
    if not any(char in SpecialSym for char in passwd):
        print('Password should have at least one of the symbols $@#')
        val = False
    if val:
        return val

def insert():
    fname = name.get()
    addr = address.get()
    un = country.get()
    email = Email.get()
    mobile = PhoneNo.get()
    gender = var.get()
    pwd = password.get()
    cnpwd = password1.get()

    with sqlite3.connect('../db/knee.db') as db:
        c = db.cursor()

    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if re.search(regex, email):
        a = True
    else:
        a = False

    if fname.isdigit() or fname == "":
        ms.showinfo("Message", "please enter valid name")
    elif addr == "":
        ms.showinfo("Message", "Please Enter Address")
    elif email == "" or a == False:
        ms.showinfo("Message", "Please Enter valid email")
    elif len(str(mobile)) < 10 or len(str(mobile)) > 10:
        ms.showinfo("Message", "Please Enter 10 digit mobile number")
    elif un == "":
        ms.showinfo("Message", "Please Enter valid Country")
    elif pwd == "":
        ms.showinfo("Message", "Please Enter valid password")
    elif var == False:
        ms.showinfo("Message", "Please Enter gender")
    elif pwd == "" or password_check(pwd) != True:
        ms.showinfo("Message", "password must contain atleast 1 Uppercase letter,1 symbol,1 number")
    elif pwd != cnpwd:
        ms.showinfo("Message", "Password Confirm password must be same")
    else:
        conn = sqlite3.connect('../db/knee.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO KneeReg(name, address, Email, country, Phoneno, Gender, password) VALUES(?,?,?,?,?,?,?)',
                (fname, addr, email, un, mobile, gender, pwd))
            conn.commit()
            ms.showinfo('Success!', 'Account Created Successfully !')
            import subprocess, sys, os
            root.destroy()
            subprocess.Popen([sys.executable, 'login.py'], cwd=os.path.dirname(os.path.abspath(__file__)))

label = tk.Label(root, text="Registration Form", font=("Forte", 30), bg="black", fg="white")
label.place(x=180, y=90)
canvas = tk.Canvas(root, background="white", borderwidth=5)
canvas.place(x=150, y=150, width=400, height=590)

tk.Label(root, text="Name:", font=("Calibri", 10), bg="white").place(x=200, y=200)
tk.Entry(root, border=2, textvar=name).place(x=330, y=205)

tk.Label(root, text="Email:", font=("Calibri", 10), bg="white").place(x=200, y=250)
tk.Entry(root, border=2, textvar=Email).place(x=330, y=255)

tk.Label(root, text="Password:", font=("Calibri", 10), bg="white").place(x=200, y=300)
tk.Entry(root, border=2, show="*", textvar=password).place(x=330, y=305)

tk.Label(root, text="Re-Enter Password:", font=("Calibri", 10), bg="white").place(x=200, y=350)
tk.Entry(root, border=2, show="*", textvar=password1).place(x=330, y=355)

tk.Label(root, text="Address:", font=("Calibri", 10), bg="white").place(x=200, y=400)
tk.Entry(root, border=2, textvar=address).place(x=330, y=405)

tk.Label(root, text="Country:", font=("Calibri", 10), bg="white").place(x=200, y=450)
tk.Entry(root, border=2, textvar=country).place(x=330, y=455)

tk.Label(root, text="Phone no:", font=("Calibri", 10), bg="white").place(x=200, y=515)
tk.Entry(root, border=2, textvar=PhoneNo).place(x=330, y=520)

tk.Label(root, text="Gender:", font=("Calibri", 10), bg="white").place(x=200, y=590)
tk.Radiobutton(root, text="Male", font=("Calibri", 10), bg="white", value=1, variable=var).place(x=330, y=590)
tk.Radiobutton(root, text="Female", font=("Calibri", 10), bg="white", value=2, variable=var).place(x=400, y=590)

def reg():
    import subprocess, sys, os
    root.destroy()
    subprocess.Popen([sys.executable, 'login.py'], cwd=os.path.dirname(os.path.abspath(__file__)))

btn = tk.Button(root, text="Create Account", font=("Arial"), width=20, command=insert, bg="black", fg="white")
btn.place(x=250, y=650)

tk.Label(root, text="Already have an account? ", bg="white", font=('Cambria', 11)).place(x=330, y=700)
tk.Button(root, text="log in", fg='blue', bg='white', command=reg).place(x=500, y=700)

root.mainloop()
