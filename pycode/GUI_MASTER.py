from subprocess import call
import tkinter as tk
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image, ImageTk
from tkinter import ttk
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

root = tk.Tk()
root.title("")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))

image2 = Image.open("./img/img6.jpg")
image2 = image2.resize((w,h), Image.LANCZOS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) 


label=tk.Label(root,text="Stress Detection",font=("times new roman",45),
               bg="#5c3b17",
               width=55,
               height=1)
label.place(x=0,y=0)        


def Data_Preprocessing():
    data = pd.read_csv(r"./db/data_stress.csv")
    data.head()

    data = data.dropna()

    """One Hot Encoding"""
    # le = LabelEncoder()
    # data['Age'] = le.fit_transform(data['Age'])
    # data['Body Temperature'] = le.fit_transform(data['Body Temperature'])
    # data['Heart rate'] = le.fit_transform(data['Heart rate'])
    # data['Systolic Blood Pressure'] = le.fit_transform(data['Systolic Blood Pressure'])
    # data['Diastolic Blood Pressure'] = le.fit_transform(data['Diastolic Blood Pressure'])
    # data['BMI'] = le.fit_transform(data['BMI'])
    # data['Blood Glucose'] = le.fit_transform(data['Blood Glucose'])

    
    """Feature Selection => Manual"""
    x = data.drop(['Stress_Levels'], axis=1)
    data = data.dropna()
    
    print(type(x))
    y = data['Stress_Levels']
    print(type(y))
    x.shape
    
    

    # from sklearn.model_selection import train_test_split
    # x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20)

    

    load = tk.Label(root, font=("Tempus Sans ITC", 15, "bold"), width=50, height=2, background="green",
                    foreground="white", text="Data Loaded=>Splitted into 80% for Training & 20% for Testing")
    load.place(x=200, y=80)




def Model_Training():
    data = pd.read_csv(r"./db/data_stress.csv")
    data.head()

    data = data.dropna()

    """One Hot Encoding"""

    # le = LabelEncoder()
    # data['Age'] = le.fit_transform(data['Age'])
    # data['Body Temperature'] = le.fit_transform(data['Body Temperature'])
    # data['Heart rate'] = le.fit_transform(data['Heart rate'])
    # data['Systolic Blood Pressure'] = le.fit_transform(data['Systolic Blood Pressure'])
    # data['Diastolic Blood Pressure'] = le.fit_transform(data['Diastolic Blood Pressure'])
    # data['BMI'] = le.fit_transform(data['BMI'])
    # data['Blood Glucose'] = le.fit_transform(data['Blood Glucose'])
    
    """Feature Selection => Manual"""
    x = data.drop(['Stress_Levels'], axis=1)
    data = data.dropna()

    print(type(x))
    y = data['Stress_Levels']
    print(type(y))
    x.shape
    
    #### DecisionTree
    # from sklearn.model_selection import train_test_split
    # x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30,random_state=111)

     
    # from sklearn.tree import DecisionTreeClassifier
    # svcclassifier = DecisionTreeClassifier()
    # svcclassifier.fit(x_train, y_train)
    
    
    # y_pred = svcclassifier.predict(x_test)
    # print(y_pred) 
    
    
    ### svm
    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30,random_state=1)
    from sklearn.svm import SVC
    svcclassifier = SVC(kernel='linear')
    svcclassifier.fit(x_train, y_train)

    y_pred = svcclassifier.predict(x_test)
    print(y_pred)
    
    ## RandomForest
   #  from sklearn.model_selection import train_test_split
   #  x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20,random_state=1234)

   # #from sklearn.svm import SVC
   #  from sklearn.ensemble import RandomForestClassifier

   #  svcclassifier = RandomForestClassifier()
   #  svcclassifier.fit(x_train, y_train)

   #  y_pred = svcclassifier.predict(x_test)
   #  print(y_pred)
   
   
    ###  naive_bayes
   #  from sklearn.model_selection import train_test_split
   #  x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20,random_state=1111)

   # #from sklearn.svm import SVC
   #  from sklearn.naive_bayes import GaussianNB

   #  svcclassifier = GaussianNB()
   #  svcclassifier.fit(x_train, y_train)

   #  y_pred = svcclassifier.predict(x_test)
   #  print(y_pred)
    
   
    
   #  from sklearn.model_selection import train_test_split
   #  x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20,random_state=11111)

   # #from sklearn.svm import SVC
   #  from xgboost import XGBClassifier

   #  xgb_classifier = XGBlassifier(use_label_encoder=False, eval_metric='logloss')
   #  xgb_classifier.fit(x_train, y_train)

   #  y_pred = xgb_classifier.predict(x_test)
   #  print(y_pred)
# Evaluate the model
#rt:\n", classification_report(y_test, y_pred))
    
    print("=" * 40)
    print("==========")
    print("Classification Report : ",(classification_report(y_test, y_pred)))
    print("Accuracy : ",accuracy_score(y_test,y_pred)*100)
    accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    ACC = (accuracy_score(y_test, y_pred) * 100)
    repo = (classification_report(y_test, y_pred))
    
    label4 = tk.Label(root,text =str(repo),width=45,height=10,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label4.place(x=205,y=200)
    
    label5 = tk.Label(root,text ="Accuracy  : "+str(ACC)+"%\nModel saved as Stress Detection.joblib",width=45,height=3,bg='khaki',fg='black',font=("Tempus Sanc ITC",14))
    label5.place(x=205,y=420)
    from joblib import dump
    dump (svcclassifier,"Stress Detection.joblib")
    print("Model saved as Stress Detection.joblib")



def call_file():
    import check1
    check1.Train()




def window():
    root.destroy()

button2 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"),
                    text="Data_Preprocessing", command=Data_Preprocessing, width=15, height=2)
button2.place(x=20, y=120)

button3 = tk.Button(root, foreground="white", background="#008080", font=("Tempus Sans ITC", 14, "bold"),
                    text="Model Training", command=Model_Training, width=15, height=2)
button3.place(x=20, y=200)

button4 = tk.Button(root, foreground="white", background="#008080", font=("Tempus Sans ITC", 14, "bold"),
                    text="Stress Detection", command=call_file, width=15, height=2)
button4.place(x=20, y=280)
exit = tk.Button(root, text="Exit", command=window, width=15, height=2, font=('times', 15, ' bold '),bg="red",fg="white")
exit.place(x=20, y=380)

root.mainloop()

'''+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'''