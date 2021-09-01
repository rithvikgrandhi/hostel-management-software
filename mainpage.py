import student_info
from tkinter import *
from checkin import *
from room import *
root = Tk()
root.title("PES BOYS HOSTEL")
root.geometry("1550x1000+0+0")

students = [['Rohan Lakshman Shetty','PES1UG20CS347','Computer Science Engineering','1st Year','Bannerghatta Road','7259676347','Lakshman Shetty','9883516987','Anita Shetty','9986316093','HDFC Bank','Hostel Mess','2'],
            ['Sankalp Kulkarni', 'PES1UG20CS384', 'Computer Science Engineering', '1st Year', 'Bannerghatta Road', '9535398910', 'Naveenachandra Kulkarni', '7259014795', 'Sampada Kulkarni', '9945301204', 'HDFC Bank', 'Namdhari', '22'],
            ]

mylabel = Label(root, text = 'PES BOYS HOSTEL',font = ("times new roman",40 ,"bold"), bd = 10, bg = "light blue", fg = "white")
mylabel.place(relx=0.1, rely=0.01, relwidth=0.8, relheight=0.2)

#frame
frame = Canvas(root, height = 500, width = 1225, bg = "light blue")
frame.place(relx = 0.1,rely = 0.25)

#check in
check = Button(frame,text = 'CHECK IN',font = ("times new roman",17 ,"bold"),padx = 100,pady = 15,command = lambda : check_in())
check.place(relx = 0.36,rely = 0.1)

#room info
room = Button(frame,text = 'ROOM INFO.',font = ("times new roman",17 ,"bold"),padx = 85,pady = 15, command = lambda : roominfo(students))
room.place(relx = 0.36,rely = 0.3)

#student info
student = Button(frame,text = 'STUDENT INFO.',font = ("times new roman",17 ,"bold"),padx = 69,pady = 15,command = lambda : student_info.info(students))
student.place(relx = 0.36,rely = 0.5)

#exit
exit1 = Button(frame,text = 'EXIT',font = ("times new roman",17 ,"bold"),padx = 133,pady = 15,command = lambda : exit() )
exit1.place(relx = 0.36,rely = 0.7)

root.mainloop()



