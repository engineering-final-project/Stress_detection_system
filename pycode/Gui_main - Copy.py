import tkinter as tk
from PIL import Image,ImageTk



root=tk.Tk()
root.configure(background='white')
w,h=root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w,h))
root.title("Main Page")

image2=Image.open("./img/img1.jpg")
image2=image2.resize((w,h),Image.LANCZOS)

background_image= ImageTk.PhotoImage(image2)

background_label=tk.Label(root,image=background_image)

background_label.image=background_image
  
background_label.place(x=0,y=0)

label=tk.Label(root,text="Stress Detection",font=("times new roman",45),
               bg="#a8ecf5",
               width=55,
               height=1)
label.place(x=0,y=0)        


def reg():
    from subprocess import call
    call(["python","registration.py"])

def log():
    from subprocess import call
    call(["python","login.py"])
    
def window():
  root.destroy()


button1 = tk.Button(root, text="LOGIN", command=log, width=14, height=1,font=('times', 20, ' bold '), bg="#999999", fg="white")
button1.place(x=300, y=300)

button2 = tk.Button(root, text="REGISTER",command=reg,width=14, height=1,font=('times', 20, ' bold '), bg="#999999", fg="white")
button2.place(x=300, y=400)

button3 = tk.Button(root, text="Exit",command=window,width=14, height=1,font=('times', 20, ' bold '), bg="red", fg="white")
button3.place(x=300, y=500)

root.mainloop()

