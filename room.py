import tkinter as tk
from tkinter import font
from tkinter.constants import ANCHOR, BOTTOM, CENTER, CURRENT, INSERT
from typing import Text
# from openpyxl import *
import tkinter.ttk as ttk
from tkinter import *
import csv



def roominfo(students):
    def room_check(l):

        x = entry.get()
        print(x)
        l = []
        with open("studentinfo.csv", "r") as fh:
            flag = 0
            reader = csv.reader(fh)
            for row in reader:
                if row[12] == x:
                    l.append(row[0])
                    
        frame4 = tk.Canvas(window, height = 230, width =500)
        frame4.place(relx=.555,rely=.5)

        frame5 = tk.Canvas(window, height = 50, width =55)
        frame5.place(relx=.7,rely=.3)
        
        roomno4 = tk.Label(frame5, text = x, font = ("times new roman",20))
        roomno4.place(relx=.1,rely=.1)

        cnt = 0
        for i in l:
            roommates = tk.Label(frame4, text = i, font = ("times new roman",20))
            roommates.place(relx=0.1,rely=0.1+cnt*0.2)
            cnt+=1
        
        



        
    window = Tk()
    window.geometry("1920x1080")
    window.configure(bg="white")
    text=Text(window)


    frame2 = tk.Canvas(window, height = 500, width =550, bg = "light blue")
    frame2.place(relx=0.54, rely=0.22)

    frame3 = tk.Canvas(window, height = 500, width =550, bg = "light blue")
    frame3.place(relx=0.1, rely=0.22)

    roomno_label=tk.Label(window,text="Enter your room number",font =("times new roman",20, "bold"),bg="light blue")
    roomno_label.place(relx= 0.11,rely=0.5)

    entry=tk.Entry(window,width=10,font=("times new roman",20, "bold"))
    entry.place(relx=.33,rely=0.5)
    
    w =tk.Label(window, text="ROOM INFORMATION",bg="light blue",fg="white",font =("times new roman",40, "bold"),width=40,height=2)
    w.pack()

    button2= Button(window,text="check",width=10,height=1,bg="light grey",font=("times new roman",20,"bold"), command = lambda : room_check(students)).place(relx=0.22,rely=.7)

    l2=tk.Label(window,text="Select your block",bg="light blue",font =("times new roman",20, "bold"))
    l2.place(relx=0.11,rely=0.4)


    dept_combo2 = ttk.Combobox(window,font=("times new roman",20))
    dept_combo2['values'] = ("Mess block","IT block","NB block","NBX block")
    dept_combo2.place(relx=.25,rely=.4)


    output=tk.Label(window, text="Your room no is : ",font =("times new roman",20, "bold"),bg="light blue",fg="black").place(relx=.55,rely=.3)
    output2=tk.Label(window, text="Your roommates are : ",font =("times new roman",20, "bold"),bg="light blue",fg="black").place(relx=.55,rely=.45)
    window.mainloop()
