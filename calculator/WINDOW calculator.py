from tkinter import *
import time
import math
import jaipurtemp

root=Tk()
root.title("Cal")
root.configure(bg='black')

def f(x):
    global s,label2
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
    label2text()

def result():
    global s,list1,label2
    t=text.get()
    try:
        s=str(eval(t))
        text.set(s)
    except Exception as e:
        s=''
        text.set(e)
    label2text()
    list1.insert(END,f"{t}={label2['text']}")

def label2text():
    global s,label2
    t=text.get()
    try:
        w=str(eval(t))
        label2['text']=w
    except Exception as e:
        pass

def clear():
    global s,label2
    s='0'
    text.set(s)
    label2['text']=''

def clear1():
    global s
    s=s[:len(s)-1]
    text.set(s)

def con():
    label['text']=time.ctime()
    label.after(1000,con)

def g(z):
    global text,s,but,radian
    result()
    if s=='0':
        s=''
    if z in ('(',')'):
        s=s+z
        text.set(s)
        return
    if z=='rad':
        if radian:
            but['text']='deg'
            radian=False
        else:
            but['text']='rad'
            radian=True
        return
    if but['text']=='deg':
        s=math.radians(float(s))
    if z=='sin':
        text.set(math.sin(float(s)))
    if z=='cos':
        text.set(math.cos(float(s)))
    if z=='tan':
        text.set(math.tan(float(s)))
    if z=='ln':
        text.set(math.log(float(s)))
    if z=='log':
        text.set(math.log10(float(s)))
    if z=='!':
        text.set(math.factorial(int(s)))
    if z=='π':
        s=s+'(3.14)'
        text.set(s)
    if z=='e':
        print(s)
        s=s+'(2.7)'
        text.set(s)
    if z=='^':
        s=s+'**'
        text.set(s)
    label2text()
        
text= StringVar()
s='0'
radian=True
label2=Label(root,bg="black",fg="yellow",justify=LEFT,font=("verdana",20,"bold"),relief=SOLID,
            height=1,state='disable')
label2.grid(columnspan=8,row=0,sticky='nswe',column=0)

e=Entry(root,textvariable=text,font=("verdana",20,"bold"),relief=SOLID,
        justify="right",bg="black",fg='yellow')
e.grid(padx=5,pady=5,sticky='nswe',columnspan=11,row=1,column=0)

l=[('sin','cos','tan'),('ln','log','!'),('π','e','^'),('(',')','rad')]
k=2
for i in l:
    c=0
    for j in i:
        but=Button(root,text=j,bg="black",fg='yellow',font=("verdana",20,"bold")
                   ,command=lambda x=j:g(x),relief=SOLID)
        but.grid(sticky='nswe',row=k,column=c)
        c=c+1
    k=k+1
        
l=['%','r789*','s456-','q123+','b0.']
k=2


for t in l:
    c=3
    for j in t:
        Button(root,text=j,bg="black",fg='yellow',command=lambda x=j:f(x),font=("verdana",20,"bold")
               ,relief=SOLID,width=5).grid(sticky='nswe',row=k,column=c)
        c=c+1
    k=k+1
    
b=Button(root,text="CE",bg="black",fg='yellow',command=clear1,relief=SOLID,
         font=("verdana",20,"bold"))
b.grid(sticky='nswe',row=2,column=4)
b=Button(root,text="c",bg="black",fg='yellow',command=clear,relief=SOLID,
         font=("verdana",20,"bold"))
b.grid(sticky='nswe',row=2,column=5,columnspan=2)
b=Button(root,text="=",bg="black",fg="yellow",command=result,relief=SOLID
         ,font=("verdana",20,"bold"))
b.grid(sticky='nswe',row=6,column=6,columnspan=2)
b=Button(root,text="√",command=lambda x='r':f(x),bg="black",relief=SOLID,fg="yellow",font=("verdana",20,"bold"))
b.grid(sticky='nswe',row=3,column=3)
b=Button(root,text="1/x",command=lambda x='b':f(x),bg="black",relief=SOLID,fg="yellow",font=("verdana",20,"bold"))
b.grid(sticky='nswe',row=6,column=3)
b=Button(root,text="x²",command=lambda x='s':f(x),bg="black",relief=SOLID,fg="yellow",font=("verdana",20,"bold"))
b.grid(sticky='nswe',row=4,column=3)
b=Button(root,text="x³",command=lambda x='q':f(x),bg="black",relief=SOLID,fg="yellow",font=("verdana",20,"bold"))
b.grid(sticky='nswe',row=5,column=3)
b=Button(root,text="/",command=lambda x='/':f(x),bg="black",relief=SOLID,fg="yellow",font=("verdana",20,"bold"))
b.grid(row=2,sticky='nswe',column=7)
label=Label(root,bg="black",fg="yellow",font=("verdana",20,"bold"),relief=SOLID,height=1)
label.grid(columnspan=3,row=6,sticky='nswe',column=0)
b=Button(root,text='close',command=root.destroy,bg="black",fg="yellow",relief=SOLID,font=("verdana",20,"bold"))
b.grid(columnspan=5,row=7,sticky='nswe',column=0)
con()

label3=Label(root,bg="black",fg="yellow",justify=LEFT,font=("verdana",20,"bold"),relief=SOLID,
            height=1)
label3.grid(columnspan=3,row=7,sticky='nswe',column=5)
label3['text']="temp: "+str(jaipurtemp.temp())

list1=Listbox(root,fg="yellow",bg="black",font=("verdana",20,"bold"),relief=RAISED)
list1.grid(row=2,column=8,rowspan=8,columnspan=3)

for x in range(7):
    root.grid_rowconfigure(x,weight=2)
for x in range(5):
    root.grid_columnconfigure(x,weight=2)

root.mainloop()
