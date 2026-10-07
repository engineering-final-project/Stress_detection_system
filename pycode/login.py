import tkinter as tk
import sqlite3
from tkinter import messagebox as ms
from PIL import Image, ImageTk
import subprocess
import sys
import os

root = tk.Tk()
root.configure(background='white')
root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
root.title("Login Page")

bg_img = Image.open('../img/img4.jpg')
bg_img = bg_img.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_img)
bg_label = tk.Label(root, image=bg_photo)
bg_label.image = bg_photo
bg_label.place(x=0, y=0)

Email = tk.StringVar()
Password = tk.StringVar()

def login():
    with sqlite3.connect('../db/knee.db') as db:
        cursor = db.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS KneeReg (name TEXT, address TEXT, Email TEXT, country TEXT, Phoneno TEXT, Gender TEXT, password TEXT)"
        )
        db.commit()
        cursor.execute(
            "SELECT * FROM KneeReg WHERE Email = ? AND password = ?",
            (Email.get(), Password.get()),
        )
        result = cursor.fetchall()
        if result:
            ms.showinfo("Message", "Login successful")
            root.destroy()
            subprocess.Popen([sys.executable, 'GUI_MASTER.py'], cwd=os.path.dirname(os.path.abspath(__file__)))
        else:
            ms.showerror('Error', 'Username or password not found')

def open_forgot():
    root.destroy()
    subprocess.Popen([sys.executable, 'forgot password.py'], cwd=os.path.dirname(os.path.abspath(__file__)))

def open_register():
    root.destroy()
    subprocess.Popen([sys.executable, 'registration.py'], cwd=os.path.dirname(os.path.abspath(__file__)))

tk.Label(root, text='Login Here', fg='black', bg='light gray', font=('Cambria', 25)).place(x=200, y=50)
canvas = tk.Canvas(root, background='light gray')
canvas.place(x=50, y=100, width=500, height=400)
tk.Label(root, text='Enter Email', bg='light gray', font=('Cambria', 14)).place(x=100, y=140)
tk.Label(root, text='Enter Password', bg='light gray', font=('Cambria', 14)).place(x=100, y=180)
tk.Entry(root, width=40, textvariable=Email).place(x=270, y=140)
tk.Entry(root, width=40, show='*', textvariable=Password).place(x=270, y=180)
tk.Button(root, text='Forgot Password?', fg='blue', bg='light gray', command=open_forgot).place(x=400, y=230)
tk.Button(root, text='Login', font=('Bold', 9), command=login, width=50, bg='light gray').place(x=130, y=360)
tk.Label(root, text='Not a Member?', font=('Cambria', 11), bg='light gray').place(x=270, y=400)
tk.Button(root, text='Sign up', fg='blue', bg='light gray', command=open_register).place(x=230, y=450, width=55)

root.mainloop()
