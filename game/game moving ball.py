from tkinter import *
import time
from tkinter import messagebox
import tkinter.ttk
root= Tk()
root.geometry("500x500")
root.title("GAME")
x=1
y=1
def up(event):
    if c.coords(r1)[1]>=0:
        c.move(r1,0,-6)
        
def down(event):
    if c.coords(r1)[1]<=440:
        c.move(r1,0,6)

def left(event):
    if c.coords(r2)[1]>=0:
        c.move(r2,0,-6)
        
def right(event):
    if c.coords(r2)[1]<=440:
        c.move(r2,0,6)
t=2999
i=0
r=5
A=0
def move():
    global t
    global x
    global r
    global y
    global i
    global u
    global label
    global o
    global B
    B.destroy()
    if c.coords(o)[0]== 20 and int(c.coords(o)[1]) in range(int(c.coords(r1)[1]),int(c.coords(r1)[3])):
        x=1
    if c.coords(o)[2]==480 and int(c.coords(o)[1]) in range(int(c.coords(r2)[1]),int(c.coords(r2)[3])):
        x=-1
    if c.coords(o)[1]<=10:
        y=1
    if c.coords(o)[1]>=490:
        y=-1
    if c.coords(o)[0]==0 or c.coords(o)[2]==500:
        messagebox.showinfo("RESULT", "You Lost")
        B=Button(root,text="start",bg="yellow",font=("verdana",20,"bold"),command=move)
        B.place(x=200,y=230)
        A=5
        c.delete(o)
        o=c.create_oval( 150,380,180,410, outline='blue',fill="red")
        t=2999
        i=0
        r=5
        return
    
    t=t+1
    if t==3000:
        r=r-2
        t=0
        i=i+1
        u=0
        label=Label(root,text="label {}".format(i),bg="yellow",font=("verdana",20,"bold"))
        label.place(x=200,y=230)
        
    u=u+1
    if u==30:
        label.destroy()
        u=0
    c.move(o,x,y)
    root.after(r,move)


c=Canvas(root,width=500,height=500,bg='blue')
c.grid()
o=c.create_oval( 150,380,180,410, outline='blue',fill="red")
r1=c.create_rectangle( 0,180,20,280, outline='blue',fill="yellow")
r2=c.create_rectangle( 480,180,500,280, outline='blue',fill="yellow")
c.bind("<Up>",up)
c.bind("<Down>",down)
c.bind("<Left>",left)
c.bind("<Right>",right)
c.focus_set()
B=Button(root,text="start",bg="yellow",font=("verdana",20,"bold"),command=move)
B.place(x=200,y=230)

root.mainloop()
