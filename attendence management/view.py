import sqlite3
from tkinter import *

def enter(rol_no):
    global root
    conn=sqlite3.connect("college.db")
    print(rol_no)
    if rol_no[2:4]=='MT':
        rows=conn.execute(f"select * from Mtech where r_no='{rol_no}'")
    if rol_no[2:4]=='BT':
        rows=conn.execute(f"select * from Btech where r_no='{rol_no}'")
    rows=rows.fetchall()
    conn.close()
    list1=['Sr no of student is: ',"Roll no  of student is: ","Name of student is: ",
           "Branch code of student is: ","Year of admission is: ","Semester of student is:",
           "Jee main score is: ","Section of student is:","Age of student is: ",
            "Percentage in 10th class is: ","Percentage in 12th class is:"]
    Y=20
    for j,i in enumerate(list1):
        l=Label(root,text=f"{i}   {rows[0][j]}",font='arial 20 bold',bg='pink')
        l.place(x=5,y=Y)
        Y+=50
        
def view_profile(root1,roll_no):
    global root
    root1.destroy()
    root=Tk()
    root.geometry("1200x800+100+50")
    root.title("View Profile")
    root.configure(bg='pink')
    enter(roll_no)
    root.mainloop()

def viewteacher(root1,id1):
    root1.destroy()
    root=Tk()
    root.geometry("1200x800+100+50")
    root.title("View Profile")
    root.configure(bg='pink')
    list1=['Sr no is: ',"ID is:","Teacher name is: ","Name code is:","Mob no is:",
           "Salary is:","Course code is: ","Year of joining is: ","Branch code is: ",
           "Enter semester: ","Section is: ","Subject is:","Age is: "]
    Y=20
    conn=sqlite3.connect("college.db")
    rows=conn.execute(f"select * from Teacher where ID='{id1}'")
    rows=rows.fetchall()
    conn.close()
    for j,i in enumerate(list1):
        l=Label(root,text=f"{i}   {rows[0][j]}",font='arial 20 bold',bg='pink')
        l.place(x=5,y=Y)
        Y+=50


    root.mainloop()



