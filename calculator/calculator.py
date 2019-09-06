from tkinter import *
import time
root=Tk()
root.title("Cal")

def f(x):
    global s
    if s=='0':
        s=''
    if x=='r':
        if int(s)>=0:
            s=int(s)**.5
            text.set(s)
        else:
            s=''
            text.set("error")
    elif x=='s':
        s=int(s)**2
        text.set(s)
    elif x=='q':
        s=int(s)**3
        text.set(s)
    elif x=='b':
        s=1/int(s)
        text.set(s)    
    else:
        s=s+x
        text.set(s)

def result():
    global s
    t=text.get()
    try:
        s=str(eval(t))
        text.set(s)
    except Exception as e:
        s=''
        text.set(e)

def clear():
    global s
    s='0'
    text.set(s)

def clear1():
    global s
    s=s[:len(s)-1]
    text.set(s)

def con():
    label['text']=time.ctime()
    label.after(1000,con)
    
text= StringVar()
s='0'
e=Entry(root,width=35,textvariable=text,font=("verdana",20,"bold"),relief=RAISED,bd=10,
        justify="right",bg="pink")
e.grid(padx=5,pady=5,sticky='nswe',columnspan=5)
l=['%','r789*','s456-','q123+','b0.']
k=1

for t in l:
    c=0
    for j in t:
        Button(root,text=j,bg="pink",command=lambda x=j:f(x),font=("verdana",20,"bold"),width=6).grid(padx=5,sticky='nswe',pady=5,row=k,column=c)
        c=c+1
    k=k+1
    
Button(root,text="CE",bg="pink",command=clear1,font=("verdana",20,"bold"),width=6).grid(padx=5,pady=5,sticky='nswe',row=1,column=1)
Button(root,text="c",bg="pink",command=clear,font=("verdana",20,"bold"),width=13).grid(padx=5,pady=5,sticky='nswe',row=1,column=2,columnspan=2)
Button(root,text="=",bg="pink",command=result,font=("verdana",20,"bold"),width=13).grid(padx=5,pady=5,sticky='nswe',row=5,column=3,columnspan=5)
Button(root,text="√",command=lambda x='r':f(x),bg="pink",font=("verdana",20,"bold"),width=6).grid(padx=5,sticky='nswe',pady=5,row=2,column=0)
Button(root,text="1/x",command=lambda x='b':f(x),bg="pink",font=("verdana",20,"bold"),width=6).grid(padx=5,sticky='nswe',pady=5,row=5,column=0)
Button(root,text="x²",command=lambda x='s':f(x),bg="pink",font=("verdana",20,"bold"),width=6).grid(padx=5,sticky='nswe',pady=5,row=3,column=0)
Button(root,text="x³",command=lambda x='q':f(x),bg="pink",font=("verdana",20,"bold"),width=6).grid(padx=5,sticky='nswe',pady=5,row=4,column=0)
Button(root,text="/",command=lambda x='/':f(x),bg="pink",font=("verdana",20,"bold"),width=6).grid(padx=5,pady=5,row=1,sticky='nswe',column=4)
label=Label(root,bg='pink',font=("verdana",20,"bold"),height=1,width=35)
label.grid(columnspan=5,row=6,padx=5,pady=5,sticky='nswe',column=0)
Button(root,text='close',command=root.destroy,bg='pink',font=("verdana",20,"bold"),width=35).grid(columnspan=5,row=7,sticky='nswe',column=0)
con()

for x in range(8):
    root.grid_rowconfigure(x,weight=2)
for x in range(5):
    root.grid_columnconfigure(x,weight=2)

root.mainloop()
