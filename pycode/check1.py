from tkinter import *
def Train():
    """GUI"""
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
    
    snoring_range= tk.IntVar()
    respiration_rate= tk.IntVar()
    body_temperature= tk.IntVar()
    limb_movement= tk.IntVar()
    blood_oxygen= tk.IntVar()
    eye_movement= tk.IntVar()
    hours_of_sleep= tk.IntVar()
    heart_rate= tk.IntVar()
    
    

    
    #========================================================================================
    def Detect():
     
        e1=body_temperature.get()
        print(e1)
        
        e2=blood_oxygen.get()
        print(e2)
        
        e3=heart_rate.get()
        print(e3)
        

        
##############################################################################################
        
        # from joblib import dump , load
        # import pandas as pd
        # a1=load('./joblib/Stress Detection.joblib')
        # v= a1.predict([[e1, e2, e3]], columns=['body_temperature', 'blood_oxygen', 'heart_rate'])
        # print(v)
        from joblib import dump, load
        import pandas as pd

        a1 = load('./joblib/Stress Detection.joblib')
        # print(a1.feature_names_in_)
        sample = pd.DataFrame(
            [[e1, e2, e3]],
            columns=['body_temperature', 'blood_oxygen ', 'heart_rate ']
        )

        v = a1.predict(sample)

        print(v)
        if v[0]==0:
            print("Low Stress")
            yes = tk.Label(root,text="Low Stress",background="green",foreground="white",font=('times', 20, ' bold '),width=30,borderwidth=2,relief='solid')
            yes.place(x=400,y=00)
            
            # label_l1 = tk.Label(root, text="If a baby is born preterm (before 37 weeks of gestation)\n it requires immediate medical attention and care to ensure their health and survival.",font=("Times New Roman",10),
            #                     background="white",borderwidth=2,relief='solid', fg="red",padx=5,pady=5)
            # label_l1.place(x=400, y=50)
                     
        elif v[0]==1:
            print("High Stress")
            yes = tk.Label(root,text="High Stress",background="red",foreground="white",font=('times', 20, ' bold '),width=30,borderwidth=2,relief='solid')
            yes.place(x=400,y=00)
            
        

    l1=tk.Label(root,text="body_temperature",background="#C0C0C0",font=('times', 20, ' bold '),width=20)
    l1.place(x=200,y=50)
    body_temperature=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=body_temperature)
    body_temperature.place(x=600,y=50)
   

    l2=tk.Label(root,text="blood_oxygen",background="#C0C0C0",font=('times', 20, ' bold '),width=20)
    l2.place(x=200,y=100)
    blood_oxygen=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=blood_oxygen)
    blood_oxygen.place(x=600,y=100)
   

    l4=tk.Label(root,text="heart_rate",background="#C0C0C0",font=('times', 20, ' bold '),width=20)
    l4.place(x=200,y=150)
    heart_rate=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=heart_rate)
    heart_rate.place(x=600,y=150)
 

    # l5=tk.Label(root,text="limb_movement",background="#C0C0C0",font=('times', 20, ' bold '),width=20)
    # l5.place(x=200,y=200)
    # limb_movement=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=limb_movement)
    # limb_movement.place(x=600,y=200)
    

    # l6=tk.Label(root,text="blood_oxygen",background="#C0C0C0",font=('times', 20, ' bold '),width=20)
    # l6.place(x=200,y=250)
    # blood_oxygen =tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=blood_oxygen)
    # blood_oxygen.place(x=600,y=250)
    
    # l6=tk.Label(root,text="eye_movement",background="#C0C0C0",font=('times', 20, ' bold '),width=20)
    # l6.place(x=200,y=300)
    # eye_movement=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=eye_movement)
    # eye_movement.place(x=600,y=300)

    # l6=tk.Label(root,text="hours_of_sleep",background="#C0C0C0",font=('times', 20, ' bold '),width=20)
    # l6.place(x=200,y=350)
    # hours_of_sleep=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=hours_of_sleep)
    # hours_of_sleep.place(x=600,y=350)


    # l7=tk.Label(root,text="heart_rate",background="#C0C0C0",font=('times', 20, ' bold '),width=20)
    # l7.place(x=200,y=400)
    # heart_rate=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=heart_rate)
    # heart_rate.place(x=600,y=400)

    button1 = tk.Button(root,text="Submit",command=Detect,font=('times', 20, ' bold '),width=10)
    button1.place(x=500,y=450)


    root.mainloop()

Train()