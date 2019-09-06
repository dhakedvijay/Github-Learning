from tkinter import *
from tkinter import messagebox
import itertools

root=Tk()
root.title("Tic Tac")
l=[]
count=True
pl1=[]
pl2=[]
w=0
u=None
v=None

def reset():
    global pl1
    global count
    global w
    global l
    global pl2
    global u
    global v
    global restart
    restart['state']='disable'
    u.destroy()
    v.destroy()
    u=None
    v=None
    l=[]
    pl1=[]
    pl2=[]
    w=0
    count=True
    for i in range(3):
        for j in range(3):
            l.append(Button(root,command=lambda t=(i,j): p1(t) if count==True else p2(t),state="disable",font=("verdana",20,"bold"),width=12,height=5))
            l[-1].grid(row=i,column=j,sticky='nswe')

def p1(t):
    global pl1
    global count
    global w
    global l
    global pl2
    global v
    global u
    u.destroy()
    l[t[0]*3+t[1]]['bg']='red'
    l[t[0]*3+t[1]]['state']='disable'
    restart['state']='active'
    count=False
    v=Label(root,text='player 2',bg='blue',font=("verdana",20,"bold"))
    v.grid(row=3,column=2,rowspan=2,sticky='nswe')
    w=w+1
    pl1.append(t[0]*3+1+t[1])
    
    win=[(1,4,7),(2,5,8),(3,6,9),(1,2,3),(4,5,6),(7,8,9),(1,5,9),(7,5,3)]
    if w>=5:
        for i in list(itertools.permutations(pl1,3)):
            if i in win:
                messagebox.showinfo("RESULT", "Player 1 win")
                reset()
                return
            
            if w==9:
                messagebox.showinfo("RESULT", "DRAW")
                reset()
                 
def p2(t):
    global w
    global pl2                  
    global l
    w=w+1
    global u
    global v
    global count
    restart['state']='active'
    l[t[0]*3+t[1]]['state']='disable'
    l[t[0]*3+t[1]]['bg']='blue'
    v.destroy()
    u=Label(root,text='player 1',bg='red',font=("verdana",20,"bold"))
    u.grid(row=3,column=0,rowspan=2,sticky='nswe')
    count=True
    pl2.append(t[0]*3+1+t[1])
    win=[(1,4,7),(2,5,8),(3,6,9),(1,2,3),(4,5,6),(7,8,9),(1,5,9),(7,5,3)]
    if w>=5:
        for i in list(itertools.permutations(pl2,3)):
            if i in win:
                messagebox.showinfo("RESULT", "Player 2 win")
                reset()     
                
def enable():
    global u
    global l
    for i in range(9):
        l[i]['state']='active'
    u=Label(root,text='player 1',bg='red',font=("verdana",20,"bold"))
    u.grid(row=3,column=0,rowspan=2,sticky='nswe')
        

for i in range(3):
    for j in range(3):
        l.append(Button(root,bg='white',command=lambda t=(i,j):p1(t) if count==True else p2(t),
                        state="disable",font=("verdana",20,"bold"),width=12,height=5))
        l[-1].grid(row=i,column=j,sticky='nswe')


start=Button(root,text='Start',command=enable,bg='powder blue',font=('verdana',20,'bold')).grid(row=3,column=1,sticky='nswe')
restart=Button(root,state='disable',text='ReStart',command=reset,bg='yellow',font=('verdana',20,'bold'))
restart.grid(row=4,column=1,sticky='nswe',padx=5,pady=5)
for x in range(5):
    root.grid_rowconfigure(x,weight=2)
        
for x in range(3):
    root.grid_columnconfigure(x,weight=2)



root.mainloop()
