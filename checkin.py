import tkinter as tk
import csv 
from tkinter import ttk
        

def check_in():
    
    
    def submit():
        name4 = name_entry.get()
        print(name4)
        srn4 = srn_entry.get()
        print(srn4)
        dept4 = dept_combo.get()
        print(dept4)
        year4 = year_combo.get()
        print(year4)
        address4 = address_entry.get('100.0')
        std_phone4 = std_phone_entry.get()
        parent_name4 = parent_name_entry.get()
        parent_number4 = parent_number_entry.get()
        LG_name4 = LG_name_entry.get()
        LG_number4 = LG_number_entry.get()
        payment4 = payment_combo.get()
        food4 = food_entry.get()
        block4 = block_entry.get()
        
        with open("studentinfo.csv", "a") as fh:
            writer = csv.writer(fh,lineterminator = '')
            l = [name4, srn4, dept4, year4, 'Bangalore', std_phone4, parent_name4, parent_number4, LG_name4, LG_number4, payment4, food4, block4]
            print(l)
            writer.writerow(l)

        
        done = tk.Label(root, text = "Submitted Successfully !!", font =("times new roman",10, "bold"))
        done.place(relx=0.35, rely=0.85, relwidth=0.3, relheight=0.03)





        
    root = tk.Tk()
    root.title("Check-In")
    root.geometry("1550x1000+0+0")

    #-------------TITLE/HEADER---------------------
    title = tk.Label(root, text = " CHECK IN ", font = ("times new roman", 40, "bold"), bd = 10, bg = "light blue", fg = "white")
    title.place(relx=0.1, rely=0.01, relwidth=0.8, relheight=0.2)

    #------------SUBMIT BUTTON---------------------
    button = tk.Button(root, text="Submit", font = ("times new roman", 25, "bold"), bd = 3, bg="light grey", fg = "white", command = lambda : submit())
    button.place(relx=0.4, rely=0.9, relwidth=0.2, relheight=0.075)

    #---------------LEFT CANVAS--------------------
    frame = tk.Canvas(root, height = 500, width = 1225, bg = "light blue")
    frame.place(relx=0.1, rely=0.25)

    #--------------NAME LABEL--------------------
    name_title = tk.Label(frame, text = "Name", font =("times new roman",20, "bold"))
    name_title.grid(row = 0, columnspan = 2, padx = 20, pady = 20)

    #--------------NAME ENTRY--------------------
    name_entry = tk.Entry(frame, width = 50)
    name_entry.grid(row = 0, column = 3, columnspan = 2, padx = 20, pady = 20)

    #--------------SRN LABEL--------------------
    srn_title = tk.Label(frame, text = "SRN", font =("times new roman",20, "bold"))
    srn_title.grid(row = 2, column = 0, columnspan = 2, padx = 20, pady = 20)

    #--------------SRN ENTRY--------------------
    srn_entry = tk.Entry(frame, width = 50, bd = 0, bg = "white")
    srn_entry.grid(row = 2, column = 3, columnspan = 2, padx = 20, pady = 20)

    #--------------DEPARTMENT LABEL--------------------
    dept_title = tk.Label(frame, text = "Department", font =("times new roman",20, "bold"))
    dept_title.grid(row = 3, columnspan = 2, padx = 20, pady = 20)

    #--------------DEPARTMENT COMBOBOX(DROPDOWN MENU)--------------------
    dept_combo = ttk.Combobox(frame,font =("times new roman",))
    dept_combo['values'] = ("Computer Science Engineering", "Electronics and Communication Engineering", "Electrical and Electronics Engineering", "Mechanical Engineering", "Civil Engineering", "Chemical Engineering", "BioTechnology")
    dept_combo.grid(row = 3, column = 3, columnspan = 2, padx = 20, pady = 20)

    #--------------YEAR LABEL--------------------
    year_title = tk.Label(frame, text = "Year", font =("times new roman",20, "bold"))
    year_title.grid(row = 4, columnspan = 2, padx = 20, pady = 20)

    #--------------YEAR COMBOBOX(DROPDOWN MENU)--------------------
    year_combo = ttk.Combobox(frame, font =("times new roman",))
    year_combo['values'] = ("1st Year", "2nd Year", "3rd Year", "4th Year")
    year_combo.grid(row = 4, column = 3, columnspan = 2, padx = 20, pady = 20)

    #--------------ADDRESS LABEL--------------------
    address_title = tk.Label(frame, text = "Address", font =("times new roman",20, "bold"))
    address_title.grid(row = 5, columnspan = 2, padx = 20, pady = 20)

    #--------------ADDRESS ENTRY--------------------
    address_entry = tk.Text(frame, width = 37, height = 4.4)
    address_entry.grid(row = 5, column = 3, columnspan = 2, padx = 20, pady = 20)

    #--------------STUDENT PH.NO LABEL--------------------
    std_phone_title = tk.Label(frame, text = "Student Phone Number", font =("times new roman",17, "bold"))
    std_phone_title.grid(row = 6, columnspan = 2, padx = 20, pady = 20)

    #--------------STUDENT PH.NO ENTRY--------------------
    std_phone_entry = tk.Entry(frame, width = 50)
    std_phone_entry.grid(row = 6, column = 3, columnspan = 2, padx = 20, pady = 20)

    #--------------RIGHT CANVAS--------------------
    frame1 = tk.Canvas(root, height = 500, width = 1225, bg = "light blue")
    frame1.place(relx=0.529, rely=0.25)

    #--------------PARENT NAME LABEL--------------------
    parent_name_title = tk.Label(frame1, text = "Parent Name", font =("times new roman",20, "bold"))
    parent_name_title.grid(row = 0, columnspan = 2, padx = 20, pady = 20)

    #---------------PARENT NAME ENTRY-------------------
    parent_name_entry = tk.Entry(frame1, width = 50)
    parent_name_entry.grid(row = 0, column = 3, columnspan = 2, padx = 20, pady = 20)

    #--------------PARENT PH.NO LABEL--------------------
    parent_number_title = tk.Label(frame1, text = "Parent Number", font =("times new roman",20, "bold"))
    parent_number_title.grid(row = 1, columnspan = 2, padx = 20, pady = 20)

    #--------------PARENT PH.NO ENTRY--------------------
    parent_number_entry = tk.Entry(frame1, width = 50)
    parent_number_entry.grid(row = 1, column = 3, columnspan = 2, padx = 20, pady = 20)

    #--------------LG NAME LABEL--------------------
    LG_name_title = tk.Label(frame1, text = "Local Gaurdian Name", font =("times new roman",15, "bold"))
    LG_name_title.grid(row = 2, columnspan = 2, padx = 20, pady = 20)

    #--------------LG NAME ENTRY--------------------
    LG_name_entry = tk.Entry(frame1, width = 50)
    LG_name_entry.grid(row = 2, column = 3, columnspan = 2, padx = 20, pady = 20)

    #--------------LG PH.NO LABEL--------------------
    LG_number_title = tk.Label(frame1, text = "Local Gaurdian Number", font =("times new roman",13, "bold"))
    LG_number_title.grid(row = 3, columnspan = 2, padx = 20, pady = 20)

    #--------------LG PH.NO ENTRY--------------------
    LG_number_entry = tk.Entry(frame1, width = 50)
    LG_number_entry.grid(row = 3, column = 3, columnspan = 2, padx = 20, pady = 20)

    #--------------PAYMENT LABEL--------------------
    payment_title = tk.Label(frame1, text = "Payment", font =("times new roman",20, "bold"))
    payment_title.grid(row = 5, columnspan = 2, padx = 20, pady = 20)

    #--------------PAYMENT COMBOBOX(DROPDOWN MENU)--------------------
    payment_combo = ttk.Combobox(frame1, font =("times new roman",))
    payment_combo['values'] = ("HDFC Bank", "SBI Bank", "Axis Bank", "ICICI Bank", "City Bank")
    payment_combo.grid(row = 5, column = 3, columnspan = 2, padx = 20, pady = 20)

    #--------------FOOD COUPON LABEL--------------------
    food_title = tk.Label(frame1, text = "Food Coupon", font =("times new roman",13, "bold"))
    food_title.grid(row = 6, columnspan = 2, padx = 20, pady = 20)

    #--------------FOOD COUPON ENTRY--------------------
    food_entry = tk.Entry(frame1, width = 50)
    food_entry.grid(row = 6, column = 3, columnspan = 2, padx = 20, pady = 20)

    #--------------BLOCK LABEL--------------------
    block_title = tk.Label(frame1, text = "Room Number", font =("times new roman",13, "bold"))
    block_title.grid(row = 7, columnspan = 2, padx = 20, pady = 20)

    #--------------BLOCK ENTRY--------------------
    block_entry = tk.Entry(frame1, width = 50)
    block_entry.grid(row = 7, column = 3, columnspan = 2, padx = 20, pady = 20)

