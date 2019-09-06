import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time


def createdb():
    try:
        conn=sqlite3.connect("course.db")
    except:
        pass
    else:
        conn.close()
#==============================================================================================
        
def createtable():
    try:
        conn=sqlite3.connect("course.db")
        for i in [('Python','MCPY0'),('Django','MCDJ0'),('Java','MCJA0'),('Dsa','MCDS0')]:
            conn.execute(f'''create table IF NOT EXISTS {i[0]}(r_no text primary key not null,
                    name text not null,father_name text not null,mob_no text not null,fmob_no
                    text not null,occupation text not null,gender text not null,dob text not
                    null,address text not null,college text not null,branch text not null,
                    semester int not null,stime text not null,etime text not null,
                    branch_prefer text not null)''')
            conn.execute(f'''insert into {i[0]} values("{i[1]}","_","_","_","_","_","_","_",
                                                "_","_","_",0,"_","_","_")''')

    except:
        pass
    finally:
        conn.commit()
        conn.close()

#=============================================================================================
def setroll():
    global combo1
    conn=sqlite3.connect("course.db")
    rows=conn.execute(f"select * from {combo1.get()}")
    rows=rows.fetchall()
    for i in rows:
        sn=i[0]
    conn.close()
    return sn

#=============================================================================================

def new():
    global combo1,root,combo2,combo3,list2,I,text
    ROLL=I.get()
    NAM=list2[0].get()+' '+list2[1].get()
    MOB=list2[2].get()
    GENDER=combo2.get()
    FATHER_NAME=list2[4].get()
    FMOB=list2[5].get()
    OCC=list2[6].get()
    DOB=list2[7].get()
    ADD=text.get(0.0,END)
    COLL=list2[9].get()
    BRANCH=list2[10].get()
    SEMESTER=list2[11].get()
    ETIME=list2[13].get()
    STIME=list2[12].get()
    BRANCH_PREFER=combo3.get()
    conn=sqlite3.connect("course.db")
    conn.execute(f'''insert into {combo1.get()} values('{ROLL}','{NAM}','{FATHER_NAME}',
                '{MOB}','{FMOB}','{OCC}','{GENDER}','{DOB}','{ADD}','{COLL}','{BRANCH}',
                {SEMESTER},'{STIME}','{ETIME}','{BRANCH_PREFER}')''')
    conn.commit()
    conn.close()
    
#=============================================================================================

def comboevent1(event):
    global combo1,root,combo2,combo3,list2,I,text
    l=Label(root,text="Roll no:",font='arial 12 bold',bg='#fff',fg='#03f')
    l.place(relx=0.53,rely=0.135294117)
    I=StringVar()
    l=Entry(root,text=I,font='arial 12 bold',bg='#fff',fg='#03f',state='disable')
    l.place(relx=0.69,rely=0.135294117)
    roll_no=setroll()
    I.set(roll_no[:4]+str(int(roll_no[4:])+1))

    list1=["First name*","Last name*","Mob no*","Gender*","Father name*","Father mob no*",
           "Father's Occupation","DOB","Address*","College name","Branch","Semester",
           "Start time","End time","Branch prefer"]
    X=0.050
    Y=0.135294117
    l1=[]
    l2=[]
    for j,i in enumerate(list1):
        if j%2==0:
            X=0.05
            Y=Y+0.07
        if i=="Address*":
            l=Label(root,text=i,font='arial 12 bold',bg='#fff',fg='#03f')
            l.place(relx=0.05,rely=Y)
            Y=Y+0.14
        if i!="Address*":
            l=Label(root,text=i,font='arial 12 bold',bg='#fff',fg='#03f')
            l.place(relx=X,rely=Y)
            X=0.53
        l1.append(l)
    
    

    list2=[StringVar(),StringVar(),StringVar(),'_',StringVar(),StringVar(),StringVar(),
           StringVar(),'_',StringVar(),StringVar(),IntVar(),StringVar(),StringVar()]
    X=0.21
    Y=0.135294117
    for j,i in enumerate(list2):
        if j==3:
            pass
        if j==8:
            text=Text(root,font='arial 12 bold',bg='#fff',fg='#03f')
            text.place(relx=0.21,rely=Y+.07,relwidth=.75,relheight=.1)
            Y=Y+0.14
        if j%2==0:
            X=0.21
            Y=Y+0.07
        if j==9:
            l=Entry(root,text=i,font='arial 12 bold',bg='#fff',fg='#03f',width=80)
            l.place(relx=X,rely=Y)
        if j!=8 and j!=3 and j!=9:
            l=Entry(root,text=i,font='arial 12 bold',bg='#fff',fg='#03f')
            l.place(relx=X,rely=Y)
            X=0.69
        l2.append(l)

    combo2=ttk.Combobox(root,font='arial 12 bold')
    combo2['values']=('M','F')
    combo2.place(relx=0.69,rely=0.28)

    combo3=ttk.Combobox(root,font='arial 12 bold')
    combo3['values']=("Mansarovar","Pratap Nagar")
    combo3.place(relx=0.21,rely=0.84)

    B=Button(root,text='Save',bg='#05f2e2',fg='black',font='arial 12 bold',command=new)
    B.place(relx=0.53,rely=0.84,relwidth=.35)

#==============================================================================================
    
def addentry(Tk1):
    global combo1,root
    root=Tk1   
    createdb()
    createtable()    
    l=Label(root,text="Student Details",font='arial 20 bold',bg='#fff',fg='#03f')
    l.place(relx=0.00148,rely=0.00588)
    
    l=Label(root,text="Select Subject",font='arial 15 bold',bg='#fff',fg='#03f')
    l.place(relx=0.050,rely=0.135294117)

    combo1=ttk.Combobox(root,font='arial 12 bold')
    combo1['values']=('Python','Dsa','Java','Django')
    combo1.place(relx=0.21,rely=0.135294117)
    combo1.bind("<<ComboboxSelected>>", comboevent1)
