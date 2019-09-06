from tkinter import *
from tkinter import ttk
import sqlite3
    
def done():
    global root,l,rollnolist,combo1,total_cla,total_pre,code
    conn=sqlite3.connect("joined.db")
    for j,i in enumerate(rollnolist):
        conn.execute(f"update {code} set total_c=({total_cla[j]}+1) where r_no='{i}'")
        if l[j].get()=='P':
            conn.execute(f"update {code} set present=({total_pre[j]}+1) where r_no='{i}'")
    conn.commit()
    conn.close()
    total=len(l)
    present=0
    for j,i in enumerate(l):
        if i.get()=='P':
            present+=1
    absent=total-present
    la=Label(root,text=f'total student:{total}',font='arial 10 bold',bg='#fff',fg='#03f')
    la.place(relx=0.233,rely=0.85,relwidth=0.12)
    la=Label(root,text=f'present student:{present}',font='arial 10 bold',bg='#fff',fg='#03f')
    la.place(relx=0.511,rely=0.85,relwidth=0.12)
    la=Label(root,text=f'absent student:{absent}',font='arial 10 bold',bg='#fff',fg='#03f')
    la.place(relx=0.788,rely=0.85,relwidth=0.12)

def fun(index):
    pass

def g():
    global root,listbutton,c1,c2,c3
    view = Toplevel(root)
    view.title("View")
    view.configure(bg='black')
    view.geometry("1100x575+200+200")
    img=PhotoImage(file="image2.png")
    Label(view,image=img,bg="black",width=500,height=500).place(relx=400,rely=110)
    list1=["Roll No.:","Name:","Father name:","Mob no:","Father mob no:","Father's Occupation:",
           "Gender:","DOB:","Address:","College name:","Branch:","Semester:","Total Classes:",
           "Total Present:"]
    Y=150
    l1=[]
    l2=[]
    stime=c3.split()[0]
    etime=c3.split()[2]
    branch=c3.split()[4]
    conn=sqlite3.connect("coaching.db")
    rows=conn.execute(f"select * from student where r_no='{listbutton[index]['text']}'").fetchall()
    row=conn.execute(f'''select * from joined where code='{c1}' and sub='{c2}' and
                        stime='{stime}' and etime='{etime}' and branch="{branch}" and
                        r_no="{listbutton[index]['text']}"''').fetchall()
    
    for j,i in enumerate(list1):
        if j%2==0:
            X=20
            Y=Y+50
        if j<12:
            l=Label(view,text=f"{i}   {rows[0][j]}",font='arial 15 bold',bg='black',width=25,fg='yellow')
            l.place(relx=X,rely=Y)
            X=X+1000
        elif j==12:
            l=Label(view,text=f"{i}   {row[0][7]}",font='arial 15 bold',bg='black',width=25,fg='yellow')
            l.place(relx=X,rely=Y)
            X=X+1000
        elif j==13:
            l=Label(view,text=f"{i}   {row[0][8]}",font='arial 15 bold',bg='black',width=25,fg='yellow')
            l.place(relx=X,rely=Y)
            X=X+1000
    conn.close()    
    view.mainloop()

def ok(root1,cc1,cc2):
    global root,l,f,rollnolist,total_cla,total_pre,listbutton,c1,c2,code
    root=root1
    c1=cc1.get()
    c2=cc2.get()
    label=Label(root,fg='#1800f5',bg='#fff',font='arial 15 bold')
    label.place(relx=0.0,rely=0.01,relwidth=1.0)
    label['text']='     '+c1+'          '+c2

    rollnolist=[]
    total_cla=[]
    total_pre=[]
    X=0.005
    for i in ['Roll no','Name','Attendence','Total_classes','Total_present']:
        label=Label(root,text=i,font='arial 10 bold',bg='#fff',fg='#03f')
        label.place(relx=X,rely=0.085,relwidth=0.15)
        X=X+0.17
    Y=0.155
    l=[]
    code=c2.split(' : ')[0]
    time=c2.split(' : ')[2]
    stime=time.split()[0]
    etime=time.split()[2]
    branch=time.split()[4]
    conn=sqlite3.connect("joined.db")
    rows=conn.execute(f'''select * from {code}''')
    rows=rows.fetchall()
    listbutton=[]
    c=0
    for i in rows:
        X=0.005
        listbutton.append(Button(root,text=i[0],font='arial 10 bold',bg='#fff',fg='#03f',
                                 command= lambda o=c:fun(o)))
        listbutton[-1].place(relx=X+0.01,rely=Y,relwidth=0.05)
        rollnolist.append(i[0])
        X+=0.17
        c=c+1
        Label(root,text=i[1],font='arial 10 bold',bg='#fff',fg='#03f',
              ).place(relx=X,rely=Y,relwidth=0.12)
        X+=0.17
        combo=ttk.Combobox(root)
        combo['values']=("P","A")
        combo.current(0)
        combo.place(relx=X,rely=Y)
        l.append(combo)
        X+=0.17
        Label(root,text=i[2],font='arial 10 bold',bg='#fff',fg='#03f'
              ).place(relx=X,rely=Y,relwidth=0.1)
        total_cla.append(i[2])
        X+=0.17
        Label(root,text=i[3],font='arial 10 bold',bg='#fff',fg='#03f',
              ).place(relx=X,rely=Y,relwidth=0.1)
        total_pre.append(i[3])
        Y+=0.07
        
    conn.close()
    button=Button(root,text="Done",font='arial 15 bold',bg='#fff',fg='#03f',
                        command=done)
    button.place(relx=0.02,rely=0.85,relwidth=0.1)
