from tkinter import *
from math import *
import time
root=Tk()
root.title("ANALOG CLOCK")
root.geometry("1000x1000")

c=Canvas(root,width=520,height=720,bg='black',border=10,relief='raised',bd=5)
c.pack(side=LEFT)


t=1
HZ=6
HH=1
def moves():
    global s
    global t
    global SZ
    global HH
    c.delete(s)
    
    s=c.create_line(275,275,275+185*sin(SZ*pi/180),275-185*cos(SZ*pi/180),width=1,fill='yellow')
    if SZ/360==t:
        t=t+1
        moveM()
    if (t-1)/2==HH:
        HH=HH+1
        moveH()
    SZ=SZ+6
    root.after(1000,moves)

def moveM():
    global m
    global MZ
    MZ=MZ+6
    c.delete(m)
    m=c.create_line(275,275,275+160*sin(MZ*pi/180),275-160*cos(MZ*pi/180),width=2,fill='red')


def moveH():
    global h
    global HZ
    HZ=HZ+1
    c.delete(h)
    h=c.create_line(275,275,275+130*sin(HZ*pi/180),275-130*cos(HZ*pi/180),width=5,fill='blue')
    

def con():
    button['text']=time.ctime()
    button.after(1000,con)
    
l=c.create_oval(500,500,50,50,width=5,fill='black')
l=c.create_oval(270,270,280,280,fill='yellow')

#Create Hour Line
for i in range(12):
    l=c.create_line(275+215*sin(i*30*pi/180),
                    275-215*cos(i*30*pi/180),275+195*sin(i*30*pi/180),
                    275-195*cos(i*30*pi/180),width=7,fill='yellow')

#Create Seconds Line
for i in range(60):
    l=c.create_line(275+215*sin(i*6*pi/180),
                    275-215*cos(i*6*pi/180),275+205*sin(i*6*pi/180),
                    275-205*cos(i*6*pi/180),width=2,fill='yellow')

HZ=time.localtime()[3]-12
HZ=HZ*30
SZ=time.localtime()[5]
SZ=SZ*6
MZ=time.localtime()[4]
MZ=MZ*6
HZ=HZ+(MZ/12)
button=Button(root,text='Click Me',command=con,fg='yellow',bg='black',
              font=('verdana',20,'bold'))
button.place(x=50,y=600)
s=c.create_line(275,275,275+185*sin(SZ*pi/180),275-185*cos(SZ*pi/180),width=1,fill='yellow')
m=c.create_line(275,275,275+160*sin(MZ*pi/180),275-160*cos(MZ*pi/180),width=2,fill='red')
h=c.create_line(275,275,275+130*sin(HZ*pi/180),275-130*cos(HZ*pi/180),width=5,fill='blue')
moves()

root.mainloop()
