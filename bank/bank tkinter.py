from tkinter import *
from Bank1 import bank
root=Tk()
root.title("Lib")
root.geometry("1000x1000")
B1=bank()
def clear():
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    listbox.delete(0,END)
def view():
    listbox.delete(0,END)
    e3['state']='normal'
    l=B1.viewall()
    for i in l:
        listbox.insert(END,i)


def deposit():
    T3=text3.get()
    T4=text4.get()
    B1.Deposit(T3,T4)

def update():
    T1=text1.get()
    T3=text3.get()
    B1.update(T1,T3)
    
def search():
    T3=text3.get()
    s=B1.search(T3)
    listbox.delete(0,END)
    listbox.insert(END,s)

def withdraw():
    T3=text3.get()
    T4=text4.get()
    B1.withdraw(T3,T4)
    
def add():
    l=[]
    
    
    T1=text1.get()
    T2=text2.get()
    
    T4=text4.get()
    text3.set(B1.create(T1,T2,T4))
    T3=text3.get()
    l.append(T1)
    l.append(T2)
    l.append(T3)
    l.append(T4)
    listbox.insert(END,l)



#create entry
text1=StringVar()
t1=Label(root,text="NAME",font=("verdana",12,"bold"),bg="powder blue",fg="red",width=19,height=2)
t1.grid(row=0,column=0,padx=5,sticky='nswe',pady=5)
e1=Entry(root,width=23,textvariable=text1,font=("verdana",20,"bold"),relief=RAISED,
        bd=3,justify="right",bg="pink")
e1.grid(row=0,column=1,padx=5,sticky='nswe',pady=5)

text2=StringVar()
t2=Label(root,text="TYPE",font=("verdana",12,"bold"),bg="powder blue",fg="red",width=19,height=2)
t2.grid(row=0,column=2,padx=5,sticky='nswe',pady=5)
e2=Entry(root,width=23,textvariable=text2,font=("verdana",20,"bold"),relief=RAISED,
        bd=3,justify="right",bg="pink")
e2.grid(row=0,column=3,padx=5,sticky='nswe',pady=5)

text3=StringVar()
t3=Label(root,text="ACCOUNT NO.",font=("verdana",12,"bold"),bg="powder blue",fg="red",width=19,height=2)
t3.grid(row=1,column=0,padx=5,sticky='nswe',pady=5)
e3=Entry(root,width=23,textvariable=text3,state='disable',font=("verdana",20,"bold"),relief=RAISED,
        bd=3,justify="right",bg="pink")
e3.grid(row=1,column=1,padx=5,sticky='nswe',pady=5)

text4=StringVar()
t4=Label(root,text="AMMOUNT",font=("verdana",12,"bold"),bg="powder blue",fg="red",width=19,height=2)
t4.grid(row=1,column=2,padx=5,sticky='nswe',pady=5)
e4=Entry(root,width=23,textvariable=text4,font=("verdana",20,"bold"),relief=RAISED,
        bd=3,justify="right",bg="pink")
e4.grid(row=1,column=3,padx=5,sticky='nswe',pady=5)


#create button
b=Button(root,width=23,text="Create New",font=("verdana",20,"bold"),relief=RAISED,
        bd=3,justify="right",bg="pink",command=add)
b.grid(row=2,column=3,padx=5,sticky='nswe',pady=5)
b=Button(root,width=23,text="View All",font=("verdana",20,"bold"),relief=RAISED,
        bd=3,justify="right",bg="pink",command=view)
b.grid(row=3,column=3,padx=5,sticky='nswe',pady=5)
b=Button(root,width=23,text="Deposit",font=("verdana",20,"bold"),relief=RAISED,
        bd=3,justify="right",bg="pink",command=deposit)
b.grid(row=4,column=3,padx=5,sticky='nswe',pady=5)
b=Button(root,width=23,text="Update Name",font=("verdana",20,"bold"),relief=RAISED,
        bd=3,justify="right",bg="pink",command=update)
b.grid(row=5,column=3,padx=5,sticky='nswe',pady=5)
b=Button(root,width=23,text="Search",font=("verdana",20,"bold"),relief=RAISED,
        bd=3,justify="right",bg="pink",command=search)
b.grid(row=6,column=3,padx=5,sticky='nswe',pady=5)
b=Button(root,width=23,text="Withdraw",font=("verdana",20,"bold"),relief=RAISED,
        bd=3,justify="right",bg="pink",command=withdraw)
b.grid(row=7,column=3,padx=5,sticky='nswe',pady=5)

#list box
listbox=Listbox(root,bg='yellow',height=25,width=150,fg='red',font=("verdana",10,"bold"))
listbox.grid(row=2,column=0,sticky='nswe',padx=5,pady=5,rowspan=6,columnspan=3)

for x in range(8):
    root.grid_rowconfigure(x,weight=2)
for x in range(4):
    root.grid_columnconfigure(x,weight=2)

root.mainloop()
