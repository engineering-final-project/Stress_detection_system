from tkinter import *
def Train():
    import tkinter as tk
    import numpy as np
    import pandas as pd
    from joblib import dump, load
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import LabelEncoder
    from sklearn.impute import SimpleImputer
    from tkinter import ttk
    
    root = tk.Tk()
    root.geometry("800x850+250+5")
    root.title("Stress Detection")
    root.configure(background="lightblue")
    
    body_temperature = tk.DoubleVar()
    blood_oxygen = tk.DoubleVar()
    heart_rate = tk.DoubleVar()
    hours_of_sleep = tk.DoubleVar()
    activity_level = tk.DoubleVar()
    
    def Detect():
        e1 = body_temperature.get()
        e2 = blood_oxygen.get()
        e3 = heart_rate.get()
        e4 = hours_of_sleep.get()
        e5 = activity_level.get()
        
        from joblib import dump, load
        import pandas as pd
        try:
            a1 = load('../Stress Detection.joblib')
        except FileNotFoundError:
            print("Model not found! Train the model first.")
            return
            
        sample = pd.DataFrame(
            [[e1, e2, e3, e4, e5]],
            columns=['body_temperature', 'blood_oxygen', 'heart_rate', 'hours_of_sleep', 'activity_level']
        )
        
        v = a1.predict(sample)
        print(v)
        
        if v[0] == 0:
            print("No Stress")
            yes = tk.Label(root,text="No Stress",background="green",foreground="white",font=('times', 20, ' bold '),width=30,borderwidth=2,relief='solid')
            yes.place(x=400,y=0)
        elif v[0] == 1:
            print("Medium Stress")
            yes = tk.Label(root,text="Medium Stress",background="orange",foreground="white",font=('times', 20, ' bold '),width=30,borderwidth=2,relief='solid')
            yes.place(x=400,y=0)
        elif v[0] == 2:
            print("High Stress")
            yes = tk.Label(root,text="High Stress",background="red",foreground="white",font=('times', 20, ' bold '),width=30,borderwidth=2,relief='solid')
            yes.place(x=400,y=0)
            
    l1=tk.Label(root,text="Body Temperature (F)",background="#C0C0C0",font=('times', 20, ' bold '),width=20)
    l1.place(x=150,y=50)
    body_temperature_entry=tk.Entry(root,bd=2,width=10,font=("TkDefaultFont", 20),textvar=body_temperature)
    body_temperature_entry.place(x=600,y=50)
    
    l2=tk.Label(root,text="Blood Oxygen (%)",background="#C0C0C0",font=('times', 20, ' bold '),width=20)
    l2.place(x=150,y=100)
    blood_oxygen_entry=tk.Entry(root,bd=2,width=10,font=("TkDefaultFont", 20),textvar=blood_oxygen)
    blood_oxygen_entry.place(x=600,y=100)
    
    l3=tk.Label(root,text="Heart Rate (BPM)",background="#C0C0C0",font=('times', 20, ' bold '),width=20)
    l3.place(x=150,y=150)
    heart_rate_entry=tk.Entry(root,bd=2,width=10,font=("TkDefaultFont", 20),textvar=heart_rate)
    heart_rate_entry.place(x=600,y=150)
    
    l4=tk.Label(root,text="Hours of Sleep",background="#C0C0C0",font=('times', 20, ' bold '),width=20)
    l4.place(x=150,y=200)
    hours_of_sleep_entry=tk.Entry(root,bd=2,width=10,font=("TkDefaultFont", 20),textvar=hours_of_sleep)
    hours_of_sleep_entry.place(x=600,y=200)
    
    l5=tk.Label(root,text="Activity Level (Steps)",background="#C0C0C0",font=('times', 20, ' bold '),width=20)
    l5.place(x=150,y=250)
    activity_level_entry=tk.Entry(root,bd=2,width=10,font=("TkDefaultFont", 20),textvar=activity_level)
    activity_level_entry.place(x=600,y=250)
    
    button1 = tk.Button(root,text="Submit",command=Detect,font=('times', 20, ' bold '),width=10)
    button1.place(x=500,y=450)
    
    root.mainloop()

if __name__ == "__main__":
    Train()
