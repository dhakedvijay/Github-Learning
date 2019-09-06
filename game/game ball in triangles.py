from tkinter import *
root=Tk()
root.geometry("500x500")
root.title("GAME")
c=Canvas(root,width=500,height=500,bg='blue')
c.grid()


#for ball 1
def move11():
    global o1
    global t1
    global Z1
    t1=c.coords(o1)
    if int(t1[0]) in range(460-int(t1[1]),480-int(t1[1])) or t1[0]==0:
        Z1=0
    c.move(o1,-1,2)
    calling1()

def move12():
    global o1
    global t1
    global Z1
    t1=c.coords(o1)
    if t1[0]==0 or int(t1[0])in range(int(t1[1])-10,int(t1[1])+10):
        Z1=0
    c.move(o1,-1,-2)
    calling1()
    
Z1=0
def move1():
    global o1
    global Z1
    global t1
    t1=c.coords(o1)
    if int(t1[0])in range(int(t1[1])-10,int(t1[1])+10):
        Z1=1
    if int(t1[0]) in range(460-int(t1[1]),480-int(t1[1])):
        Z1=2
    else:
        c.move(o1,1,-1)
    calling1()
    
def calling1():
    global Z1
    if Z1==1:
        root.after(12,move11)
    elif Z1==2:
        root.after(12,move12)
    else:
        root.after(12,move1)

#for ball 2
def move21():
    global o2
    global t2
    global Z2
    t2=c.coords(o2)
    if int(t2[0]) in range(460-int(t2[1]),480-int(t2[1])) or t2[1]==0 or t2[1]==-1:
        Z2=0
    else:
        c.move(o2,2,-2)
    calling2()

def move22():
    global o2
    global t2
    global Z2
    t2=c.coords(o2)
    if int(t2[0])in range(460-int(t2[1]),480-int(t2[1])):
        Z2=0
    c.move(o2,2,1)
    calling2()
       
Z2=0
def move2():
    global o2
    global Z2
    global t2
    t2=c.coords(o2)
    if int(t2[0])in range(int(t2[1])-10,int(t2[1])+10):
        Z2=1
    if t2[1]==0 or t2[1]==-1:
        Z2=2
    else:
        c.move(o2,-2,1)
    calling2()
    
def calling2():
    global Z2
    if Z2==1:
        root.after(12,move21)
    elif Z2==2:
        root.after(12,move22)
    else:
        root.after(12,move2)

#for ball 3
def move31():
    global o3
    global t3
    global Z3
    t3=c.coords(o3)
    if int(t3[0]) in range(int(t3[1])-10,int(t3[1])+10) :
        Z3=0
    c.move(o3,-1,1)
    calling3()

def move32():
    global o3
    global t3
    global Z3
    t3=c.coords(o3)
    if int(t3[0])in range(460-int(t3[1]),480-int(t3[1])):
        Z3=0
    c.move(o3,-1,-1.5)
    calling3()
       
Z3=0
def move3():
    global o3
    global Z3
    global t3
    t3=c.coords(o3)
    if t3[2]==499.5 or t3[2]==501.5 or t3[2] in range(497,502):
        Z3=1
    if int(t3[0])in range(int(t3[1])-10,int(t3[1])+10):
        Z3=2
    else:
        c.move(o3,1.5,1)
    calling3()
    
def calling3():
    global Z3
    if Z3==1:
        root.after(12,move31)
    elif Z3==2:
        root.after(12,move32)
    else:
        root.after(12,move3)

#for ball 4
def move41():
    global o4
    global t4
    global Z4
    t4=c.coords(o4)
    if int(t4[3])in range(498,501):
        Z4=0
    else:
        c.move(o4,-.5,1)
    calling4()

def move42():
    global o4
    global t4
    global Z4
    t4=c.coords(o4)
    if int(t4[0])in range(470-int(t4[1]),490-int(t4[1])):
        Z4=0
    else:
        c.move(o4,-1,-1.5)
    calling4()
       
Z4=0
def move4():
    global o4
    global Z4
    global t4
    t4=c.coords(o4)
    if int(t4[3])in range(498,501):
        Z4=2
    if int(t4[0])in range(int(t4[1])-10,int(t4[1])+10):
        Z4=1
    else:
        c.move(o4,2,-1)
    calling4()
    
def calling4():
    global Z4
    if Z4==1:
        root.after(12,move41)
    elif Z4==2:
        root.after(12,move42)
    else:
        root.after(12,move4)


#Main
l1=c.create_line(0,0,500,500,width=5,fill='red')
l2=c.create_line(0,500,500,0,width=5,fill='red')
o1=c.create_oval( 125,250,145,270, outline='blue',fill="yellow")
o2=c.create_oval( 240,125,260,145, outline='blue',fill="yellow")
o3=c.create_oval( 375,250,395,270, outline='blue',fill="yellow")
o4=c.create_oval( 240,375,260,395, outline='blue',fill="yellow")
t1=c.coords(o1)

move1()
move2()
move3()
move4()

root.mainloop()
