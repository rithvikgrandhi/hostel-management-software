from tkinter import *
import csv


def info(students):
    def checking():
        
        frame1 = Canvas(frame, height=225, width=1125, bg='white')
        frame1.place(relx=0.05, rely=0.44)

        x = srn.get()
        
        with open("studentinfo.csv", "r") as fh:
            flag = 0
            reader = csv.reader(fh)
            for row in reader:
                if row[1] == x:
                    flag = 1
                    l = row
                    break
                
        if flag == 1:
            
                name4 = Label(frame1, text='Name : '+l[0], font = ("times new roman",15))
                name4.place(relx = 0.1,rely = 0.1)
                #srn
                srn4 = Label(frame1, text='SRN : '+l[1], font = ("times new roman",15))
                srn4.place(relx = 0.1,rely = 0.35)
                #room no
                room_no4 = Label(frame1, text='Room Number : '+l[12], font = ("times new roman",15))
                room_no4.place(relx = 0.1,rely = 0.55)
                #dept
                dept4 = Label(frame1, text='Department : '+l[2], font = ("times new roman",15))
                dept4.place(relx = 0.1,rely = 0.75)
                #year
                year4 = Label(frame1, text='Year : '+l[3], font = ("times new roman",15))
                year4.place(relx = 0.55,rely = 0.1)
                #std phone no
                stdphno4 = Label(frame1, text='Student Phone No. : '+l[5], font = ("times new roman",15))
                stdphno4.place(relx = 0.55,rely = 0.35)
                #parent name
                pname4 = Label(frame1, text='Parent Name : '+l[6], font = ("times new roman",15))
                pname4.place(relx = 0.55,rely = 0.55)
                #parent ph no
                pphno = Label(frame1, text='Parent Phone No. : '+l[7], font = ("times new roman",15))
                pphno.place(relx = 0.55,rely = 0.75)
        
        else:
                error4 = Label(frame1, text='Error! SRN Does Not Exist.', font = ("times new roman",25))
                error4.place(relx = 0.35,rely = 0.44)
 
            
                
 
    


    root = Tk()
    root.title("STUDENT INFO")
    root.geometry("1550x1000+0+0")

    #header
    head = Label(root, text = 'STUDENT INFO.',font = ("times new roman",40 ,"bold"), bd = 10, bg = "light blue", fg = "white")
    head.place(relx=0.1, rely=0.01, relwidth=0.8, relheight=0.2)

    #frame
    frame = Canvas(root, height = 500, width = 1225, bg = "light blue")
    frame.place(relx = 0.1,rely = 0.25)

    #srn
    srn1 = Label(frame,text = 'SRN',font = ("times new roman",15,"bold"))
    srn1.place(relx = 0.36,rely = 0.09)
    srn = Entry(frame,width = 50)
    srn.insert(2,'')
    srn.place(relx = 0.45,rely = 0.1)

    #name
    '''name1 = Label(frame,text = 'Name',font = ("times new roman",15,"bold"))
    name1.place(relx = 0.36,rely = 0.29)
    name = Entry(frame,width = 50)
    name.insert(2,'')
    name.place(relx = 0.45,rely = 0.3)'''



    #check
    check = Button(frame,text = 'CHECK',font = ("times new roman",18 ,"bold"),padx = 20,pady =5,command = lambda:checking())
    check.place(relx = 0.45,rely = 0.25)



