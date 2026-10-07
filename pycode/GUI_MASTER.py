from subprocess import call
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image, ImageTk
from tkinter import ttk
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.svm import SVC
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split, GridSearchCV
from joblib import dump

root = tk.Tk()
root.title("Stress Detection System")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
image2 = Image.open("../img/img6.jpg")
image2 = image2.resize((w,h), Image.LANCZOS)
background_image = ImageTk.PhotoImage(image2)
background_label = tk.Label(root, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0) 
label=tk.Label(root,text="Stress Detection",font=("times new roman",45),
               bg="#5c3b17", fg="white", width=55, height=1)
label.place(x=0,y=0)        

def Data_Preprocessing():
    data = pd.read_csv(r"../db/data_stress.csv")
    data.columns = [col.strip() for col in data.columns]
    
    data = data.dropna(subset=['Stress_Levels'])
    
    x = data.drop(['Stress_Levels'], axis=1)
    y = data['Stress_Levels']
    load = tk.Label(root, font=("Tempus Sans ITC", 15, "bold"), width=50, height=2, background="green",
                    foreground="white", text="Data Loaded => Splitted into 70% for Training & 30% for Testing")
    load.place(x=200, y=80)

def Model_Training():
    data = pd.read_csv(r"../db/data_stress.csv")
    data.columns = [col.strip() for col in data.columns]
    data = data.dropna(subset=['Stress_Levels'])
    
    x = data.drop(['Stress_Levels'], axis=1)
    y = data['Stress_Levels']
    
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=42, stratify=y)
    
    pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='median')),
        ('poly', PolynomialFeatures(degree=2, include_bias=False)),
        ('scaler', StandardScaler()),
        ('svm', SVC(kernel='linear'))
    ])
    

    param_grid = {
        'svm__C': [0.1, 1.0, 10.0]
    }
    grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='accuracy')
    grid_search.fit(x_train, y_train)
    
    best_model = grid_search.best_estimator_
    y_pred = best_model.predict(x_test)
    
    print("=" * 40)
    print("==========")
    print("Best Hyperparameters:", grid_search.best_params_)
    print("Classification Report : \n",(classification_report(y_test, y_pred)))
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = accuracy * 100
    repo = classification_report(y_test, y_pred)

    report_text = f"Best Params: {grid_search.best_params_}\n\n" + repo
    label4 = tk.Label(root,text =report_text,width=45,height=10,bg='khaki',fg='black',font=("Tempus Sans ITC",14))
    label4.place(x=205,y=200)
    
    label5 = tk.Label(root,text ="Accuracy  : "+str(round(ACC,2))+"%\nModel saved as Stress Detection.joblib",width=45,height=3,bg='khaki',fg='black',font=("Tempus Sans ITC",14))
    label5.place(x=205,y=420)
    
    dump(best_model, "../Stress Detection.joblib")
    print("Model saved as Stress Detection.joblib")
def call_file():
    import check1
    check1.Train()
def window():
    root.destroy()
button2 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"),
                    text="Data Preprocessing", command=Data_Preprocessing, width=15, height=2)
button2.place(x=20, y=120)
button3 = tk.Button(root, foreground="white", background="#008080", font=("Tempus Sans ITC", 14, "bold"),
                    text="Model Training", command=Model_Training, width=15, height=2)
button3.place(x=20, y=200)
button4 = tk.Button(root, foreground="white", background="#008080", font=("Tempus Sans ITC", 14, "bold"),
                    text="Stress Detection", command=call_file, width=15, height=2)
button4.place(x=20, y=280)
exit_btn = tk.Button(root, text="Exit", command=window, width=15, height=2, font=('times', 15, ' bold '),bg="red",fg="white")
exit_btn.place(x=20, y=380)
root.mainloop()
