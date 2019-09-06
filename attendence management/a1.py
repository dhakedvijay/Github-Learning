from tkinter import *
from tkinter import ttk
import databaseteacher
import databasestudent
import sqlite3
import take_attendence
import jaipurtemp

root=Tk()
root.title("Attendence record")
label=0
def createlabel():
    global label,t,mainframe
    l=Label(mainframe,fg='#1800f5',bg='#fff',image=image222)
    l.place(relx=0.0,rely=0.0,relheight=1.0,relwidth=1.0)
    if label==0:
        t="temp: "+str(jaipurtemp.temp())
    label=Label(mainframe,fg='#1800f5',bg='#fff',font='arial 15 bold')
    label.place(relx=0.0,rely=0.95,relwidth=1.0)
    label['text']=t
    
def createbatch():
    createlabel()
    databaseteacher.createbatch(mainframe)

def teacher():
    createlabel()
    databaseteacher.addteacher(mainframe)

def comboevent5(event):
    global combo3,combo4,combo5
    createlabel()
    start=combo5.get().split()[1]
    end=combo5.get().split()[3]
    conn=sqlite3.connect("course.db")
    rows=conn.execute(f'''select * from {combo4.get()} where branch_prefer='{combo3.get()}'
                                and stime="{start}" and etime="{end}"''')
    rows=rows.fetchall()
    conn.close()
    X=0.2
    for i in ['Roll no','Name','Mob No.']:
        label=Label(mainframe,text=i,font='arial 15 bold',bg='#fff',fg='#03f')
        label.place(relx=X,rely=.03)
        X=X+0.2222222
    Y=.13
    for i in rows:
        X=0.2
        label=Label(mainframe,text=i[0],font='arial 12 bold',bg='#fff',fg='#03f')
        label.place(relx=X,rely=Y)
        X=X+0.2222222
        label=Label(mainframe,text=i[1],font='arial 12 bold',bg='#fff',fg='#03f')
        label.place(relx=X,rely=Y)
        X=X+0.2222222
        label=Label(mainframe,text=i[3],font='arial 12 bold',bg='#fff',fg='#03f')
        label.place(relx=X,rely=Y)
        Y=Y+0.07

def comboevent4(event):
    global combo3,combo5,combo4
    l=Label(mainframe,text="Select Time Slot",fg='#1800f5',font='arial 15 bold',bg='#fff')
    l.place(relx=0.05,rely=0.28)
    conn=sqlite3.connect("course.db")
    rows=conn.execute(f"select * from {combo4.get()} where branch_prefer='{combo3.get()}'")
    rows=rows.fetchall()
    lis=[]
    for i in rows:
        lis.append(f"from {i[12]} to {i[13]}")
    conn.close()
    lis=list(set(lis))
    lis.sort()
    combo5=ttk.Combobox(mainframe)
    combo5['values']=tuple(lis)
    combo5.place(relx=0.35,rely=0.28)
    combo5.bind("<<ComboboxSelected>>", comboevent5)

def comboevent3(event):
    global combo3,combo4
    l=Label(mainframe,text="Select Subject",fg='#1800f5',font='arial 15 bold',bg='#fff')
    l.place(relx=0.05,rely=0.18)
    combo4=ttk.Combobox(mainframe)
    combo4['values']=("Python","Dsa","Django","Java")
    combo4.place(relx=0.35,rely=0.18)
    combo4.bind("<<ComboboxSelected>>", comboevent4)

def viewstudent():
    global combo3
    createlabel()
    l=Label(mainframe,text="Select Branch",fg='#1800f5',font='arial 15 bold',bg='#fff')
    l.place(relx=0.05,rely=0.08)
    combo3=ttk.Combobox(mainframe)
    combo3['values']=("Mansarovar","Pratap Nagar")
    combo3.place(relx=0.35,rely=0.08)
    combo3.bind("<<ComboboxSelected>>", comboevent3)
    
    
def comboevent2(event):
    global combo1,combo2
    createlabel()
    take_attendence.ok(mainframe,combo1,combo2)

def comboevent(event):
    global combo1,combo2
    l=Label(mainframe,text="Select Subject info.",fg='#1800f5',font='arial 15 bold',bg='#fff')
    l.place(relx=0.05,rely=0.18)
    conn=sqlite3.connect("teacher.db")
    rows=conn.execute(f"select * from allbatch where id='{combo1.get()}'")
    rows=rows.fetchall()
    lis=[]
    for i in rows:
        lis.append(f"{i[0]} : {i[2]} : {i[3]} to {i[4]} at {i[5]}")
    conn.close()
    lis=list(set(lis))
    lis.sort()
    combo2=ttk.Combobox(mainframe)
    combo2['values']=tuple(lis)
    combo2['width']=40
    combo2.place(relx=0.35,rely=0.18)
    combo2.bind("<<ComboboxSelected>>", comboevent2)

def takeattendence():
    global combo1
    createlabel()
    l=Label(mainframe,text="Select your ID",fg='#1800f5',font='arial 15 bold',bg='#fff')
    l.place(relx=0.05,rely=0.08)
    combo1=ttk.Combobox(mainframe)
    conn=sqlite3.connect("teacher.db")
    rows=conn.execute("select * from allteacher")
    rows=rows.fetchall()
    lis=[]
    for i in rows:
        lis.append(i[0])
    conn.close()
    lis=list(set(lis))
    lis.sort()
    combo1['values']=tuple(lis[1:])
    combo1.place(relx=0.35,rely=0.08)
    combo1.bind("<<ComboboxSelected>>", comboevent)

def newenquire():
    createlabel()
    databasestudent.addentry(mainframe)
    
checkv=0
checka=0
#root.geometry("1200x800+100+50")

image222=PhotoImage(file="acad3.png")

f=Frame(root,bg='yellow',relief=SOLID)
f.place(relx=0.0,rely=0.0,relheight=0.13, relwidth=1.0)
img=PhotoImage(file="matrix.png")
Label(f,image=img,bg='#fff').place(relx=0.0,relheight=1.0,rely=0.0)


l=Label(f,text="Welcome To Matrix Computers, Jaipur",fg='#1800f5'
        ,font='arial 30 bold',bg='#fff')
l.place(relx=0.5,rely=0.5,anchor=CENTER)
Label(f,image=img,bg='#fff').place(relx=0.792,relheight=1.0,rely=0.0)


f=Frame(root,bg='green',relief=SOLID)
f.place(relx=0.8,rely=0.13,relheight=0.87, relwidth=.2)

b=Button(f,text="New Enquire",fg="#1800f5",font='arial 18 bold',command=newenquire)
b.place(relx=0.003703,rely=0.02,relwidth=1.0)

b=Button(f,text="New teacher",fg="#1800f5",font='arial 18 bold',command=teacher)
b.place(relx=0.003703,rely=0.15,relwidth=1.0)

b=Button(f,text="Create Batch",fg="#1800f5",font='arial 18 bold',command=createbatch)
b.place(relx=0.003703,rely=0.28,relwidth=1.0)

b=Button(f,text="Take Attendence",fg="#1800f5",font='arial 18 bold',command=takeattendence)
b.place(relx=0.003703,rely=0.41,relwidth=1.0)

b=Button(f,text="View student",fg="#1800f5",font='arial 18 bold',command=viewstudent)
b.place(relx=0.003703,rely=0.54,relwidth=1.0)

mainframe=Frame(root,bg='blue',relief=SOLID)
mainframe.place(relx=0.0,rely=0.13,relheight=0.87, relwidth=0.8)
createlabel()

root.mainloop()
