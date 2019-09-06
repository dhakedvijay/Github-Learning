import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
import addstudent

def setid():
    conn=sqlite3.connect("teacher.db")
    rows=conn.execute("select * from allteacher")
    rows=rows.fetchall()
    for i in rows:
        sn=i[0]
    conn.close()
    return sn

#==============================================================================================

def setbatchid():
    conn=sqlite3.connect("teacher.db")
    rows=conn.execute("select * from allbatch")
    rows=rows.fetchall()
    for i in rows:
        sn=i[0]
    conn.close()
    return sn

#==============================================================================================

def createdb():
    try:
        conn=sqlite3.connect("teacher.db")
    except:
        pass
    else:
        conn.close()
        
#==============================================================================================
        
def createtable():
    try:
        conn=sqlite3.connect("teacher.db")
        conn.execute(f'''create table if not exists allbatch(batchcode text primary key not null,
                        id text not null,sub text not null,stime text not null,etime text
                        not null,branch text not null)''')
        conn.execute(f'''create table allteacher(id text primary key not null,
                        name text not null,code text not null,gender text not null,mob text
                        not null)''')
        conn.execute("insert into allteacher values('MCTE0','_','_','_','_')")
        conn.execute("insert into allbatch values('MCBA0','_','_','_','_','_')")
    except:
        pass
    finally:
        conn.commit()
        conn.close()

#==============================================================================================

def new():
    global root,combo1,list2
    ID=list2[0].get()
    NAM=list2[1].get()+' '+list2[2].get()
    MOB=list2[4].get()
    GENDER=combo1.get()
    CODE=list2[3].get()
    conn=sqlite3.connect("teacher.db")
    conn.execute(f'''insert into allteacher values('{ID}','{NAM}','{CODE}',
                                '{GENDER}','{MOB}')''')
    conn.commit()
    conn.close()

#==============================================================================================
def addteacher(Tk1):
    global root,combo1,list2
    root=Tk1
    createdb()
    createtable()
    l=Label(root,text="Teacher Details",font='arial 20 bold',bg='#fff',fg='#03f')
    l.place(relx=0.001,rely=0.001)
    list1=["ID","First name","Last name","Name Code","Mob no*","Gender*"]
    Y=0.135
    l1=[]
    l2=[]
    for j,i in enumerate(list1):
        if j%2==0:
            X=0.05
            Y=Y+0.07
        l=Label(root,text=i,font='arial 12 bold',bg='#fff',fg='#03f')
        l.place(relx=X,rely=Y)
        X=0.53
        l1.append(l)

    list2=[StringVar(),StringVar(),StringVar(),StringVar(),StringVar()]
    X=0.21
    Y=0.135
    list3=[]
    for j,i in enumerate(list2):
        if j%2==0:
            X=0.21
            Y=Y+0.07
        list3.append(Entry(root,text=i,font='arial 12 bold',bg='#fff',fg='#03f'))
        list3[-1].place(relx=X,rely=Y)
        X=0.69
        l2.append(l)

    list3[0]['state']='disable'
    idt=setid()
    list2[0].set(f'{idt[:4]}{str(int(idt[4:])+1)}')
    combo1=ttk.Combobox(root)
    combo1['values']=('M','F')
    combo1.place(relx=0.69,rely=0.354)

    B=Button(root,text='Save',bg='#05f2e2',fg='black',font='arial 12 bold',command=new)
    B.place(relx=0.35,rely=0.44,relwidth=0.35)
    
#==============================================================================================

def addbatch():
    global root,combo1,list2,combo2,C
    BATCHID=C.get()
    ID=list2[0].get()
    STIME=list2[1].get()
    ETIME=list2[2].get()
    SUB=combo1.get()
    BRANCH=combo2.get()
    conn=sqlite3.connect("teacher.db")
    conn.execute(f'''insert into allbatch values('{BATCHID}','{ID}','{SUB}','{STIME}',
                                        '{ETIME}','{BRANCH}')''')
    conn.commit()
    conn.close()
    addstudent.tobatch(root,BATCHID)

#==============================================================================================

def createbatch(Tk1):
    global root,combo1,list2,combo2,C
    root=Tk1
    createtable()
    l=Label(root,text="New Batch",font='arial 17 bold',bg='#fff',fg='#03f')
    l.place(relx=0.001,rely=0.001)

    l=Label(root,text="Batch code",font='arial 12 bold',bg='#fff',fg='#03f')
    l.place(relx=0.05,rely=0.15)
    C=StringVar()
    l=Entry(root,text=C,font='arial 12 bold',bg='#fff',state='disable',fg='#03f')
    l.place(relx=0.21,rely=0.15)
    idt=setbatchid()
    C.set(f'{idt[:4]}{str(int(idt[4:])+1)}')
    
    list1=['ID','Stime','Etime','sub','branch']
    Y=0.15
    l1=[]
    l2=[]
    for j,i in enumerate(list1):
        if j%2==0:
            X=0.05
            Y=Y+0.07
        l=Label(root,text=i,font='arial 12 bold',bg='#fff',fg='#03f')
        l.place(relx=X,rely=Y)
        X=0.53
        l1.append(l)
    list2=[StringVar(),StringVar(),StringVar()]
    X=0.21
    Y=0.15
    for j,i in enumerate(list2):
        if j%2==0:
            X=0.21
            Y=Y+0.07
        if j!=5:
            l=Entry(root,text=i,font='arial 12 bold',bg='#fff',fg='#03f')
            l.place(relx=X,rely=Y)
            X=0.69
        l2.append(l)
    combo1=ttk.Combobox(root)
    combo1['values']=('Python','Dsa','Java','Django')
    combo1.place(relx=0.69,rely=.29)
    combo2=ttk.Combobox(root)
    combo2['values']=("Mansarovar","Pratap Nagar")
    combo2.place(relx=0.21,rely=.36)

    B=Button(root,text='Save',bg='#05f2e2',fg='black',font='arial 12 bold',command=addbatch)
    B.place(relx=0.35,rely=.5,relwidth=0.35)
