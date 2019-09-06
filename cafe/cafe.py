from tkinter import *
root=Tk()
root.title("CAFE")
label=Label(root,text="Unique Caterers",bg='powder blue',font=("italian",20,"bold"),height=1,width=35)
label.pack(side='top',fill=BOTH)

B=[]

#panipuri  I1
N1=0
def F1():
    global N1
    N1=N1+1
    B1['text']='Add {}'.format(N1)
    
I1 = PhotoImage(file = "I1.gif")
m = Label(root, image=I1)
m.place(x=10,y=50)
L1=Label(root,text="PaniPuri  Rs.50",font=("italian",20,"bold"))
L1.place(x=10,y=200)
B1=Button(root,text="Add",command=F1,font=("italian",20,"bold"))
B1.place(x=220,y=100)
B.append(B1)

#Veg_Biryani I2
N2=0
def F2():
    global N2
    N2=N2+1
    B2['text']='Add {}'.format(N2)
    
I2 = PhotoImage(file = "I2.gif")
m = Label(root, image=I2)
m.place(x=10,y=260)
L2=Label(root,text="Veg_Biryani  Rs.90",font=("italian",18,"bold"))
L2.place(x=10,y=430)
B2=Button(root,text="Add",command=F2,font=("italian",20,"bold"))
B2.place(x=235,y=310)
B.append(B2)

#Samosa I3
N3=0
def F3():
    global N3
    N3=N3+1
    B3['text']='Add {}'.format(N3)
    
I3 = PhotoImage(file = "I3.gif")
m = Label(root, image=I3)
m.place(x=10,y=470)
L3=Label(root,text="Samosa  Rs.20",font=("italian",18,"bold"))
L3.place(x=10,y=640)
B3=Button(root,text="Add",command=F3,font=("italian",20,"bold"))
B3.place(x=220,y=510)
B.append(B3)

#Chola-Bhatoora I4
N4=0
def F4():
    global N4
    N4=N4+1
    B4['text']='Add {}'.format(N4)
    
I4 = PhotoImage(file = "I4.gif")
m = Label(root, image=I4)
m.place(x=340,y=50)
L4=Label(root,text="Chola-Bhatoora  Rs.100",font=("italian",18,"bold"))
L4.place(x=340,y=195)
B4=Button(root,text="Add",command=F4,font=("italian",20,"bold"))
B4.place(x=545,y=100)
B.append(B4)

#Special-Thali  I5
N5=0
def F5():
    global N5
    N5=N5+1
    B5['text']='Add {}'.format(N5)
    
I5 = PhotoImage(file = "I5.gif")
m = Label(root, image=I5)
m.place(x=340,y=260)
L5=Label(root,text="Special-Thali  Rs.140",font=("italian",18,"bold"))
L5.place(x=340,y=430)
B5=Button(root,text="Add",command=F5,font=("italian",20,"bold"))
B5.place(x=575,y=310)
B.append(B5)

#Rasmalai I6
N6=0
def F6():
    global N6
    N6=N6+1
    B6['text']='Add {}'.format(N6)
    
I6 = PhotoImage(file = "I6.gif")
m = Label(root, image=I6)
m.place(x=340,y=465)
L6=Label(root,text="Rasmalai  Rs.80",font=("italian",18,"bold"))
L6.place(x=340,y=665)
B6=Button(root,text="Add",command=F6,font=("italian",20,"bold"))
B6.place(x=545,y=510)
B.append(B6)

#Paratha I7
N7=0
def F7():
    global N7
    N7=N7+1
    B7['text']='Add {}'.format(N7)
    
I7 = PhotoImage(file = "I7.gif")
m = Label(root, image=I7)
m.place(x=660,y=50)
L7=Label(root,text="Paratha  Rs.25",font=("italian",18,"bold"))
L7.place(x=660,y=200)
B7=Button(root,text="Add",command=F7,font=("italian",20,"bold"))
B7.place(x=915,y=100)
B.append(B7)



L=[]
#OK
def create_label():
    global l
    NAME=Label(root,text="NAME",font=("italian",12,"bold"))
    NAME.place(x=1050,y=100)
    QUANTITY=Label(root,text="QUANTITY",font=("italian",12,"bold"))
    QUANTITY.place(x=1200,y=100)
    PRICE=Label(root,text="PRICE",font=("italian",12,"bold"))
    PRICE.place(x=1300,y=100)

    #I1
    global N1
    if N1!=0:
        print(N1)
        LB=Label(root,text="pani puri",font=("italian",12,"bold"))
        LB.place(x=1050,y=150)
        L.append(LB)
        LB=Label(root,text=N1,font=("italian",12,"bold"))
        LB.place(x=1200,y=150)
        L.append(LB)
        LB=Label(root,text=50*N1,font=("italian",12,"bold"))
        LB.place(x=1300,y=150)
        L.append(LB)

    #I2
    global N2
    if N2!=0:
        print(N2)
        LB=Label(root,text="Veg-Biryani",font=("italian",12,"bold"))
        LB.place(x=1050,y=170)
        L.append(LB)
        LB=Label(root,text=N2,font=("italian",12,"bold"))
        LB.place(x=1200,y=170)
        L.append(LB)
        LB=Label(root,text=90*N2,font=("italian",12,"bold"))
        LB.place(x=1300,y=170)
        L.append(LB)

    #I3
    global N3
    if N3!=0:
        print(N3)
        LB=Label(root,text="Samosa",font=("italian",12,"bold"))
        LB.place(x=1050,y=190)
        L.append(LB)
        LB=Label(root,text=N3,font=("italian",12,"bold"))
        LB.place(x=1200,y=190)
        L.append(LB)
        LB=Label(root,text=120*N3,font=("italian",12,"bold"))
        LB.place(x=1300,y=190)
        L.append(LB)

    #I4
    global N4
    if N4!=0:
        print(N4)
        LB=Label(root,text="Chola-Bhatoora",font=("italian",12,"bold"))
        LB.place(x=1050,y=210)
        L.append(LB)
        LB=Label(root,text=N4,font=("italian",12,"bold"))
        LB.place(x=1200,y=210)
        L.append(LB)
        LB=Label(root,text=100*N4,font=("italian",12,"bold"))
        LB.place(x=1300,y=210)
        L.append(LB)

    #I5
    global N5
    if N5!=0:
        print(N5)
        LB=Label(root,text="Special-Thali",font=("italian",12,"bold"))
        LB.place(x=1050,y=230)
        L.append(LB)
        LB=Label(root,text=N5,font=("italian",12,"bold"))
        LB.place(x=1200,y=230)
        L.append(LB)
        LB=Label(root,text=140*N5,font=("italian",12,"bold"))
        LB.place(x=1300,y=230)
        L.append(LB)

    #I6
    global N6
    if N6!=0:
        print(N6)
        LB=Label(root,text="Rasmalai",font=("italian",12,"bold"))
        LB.place(x=1050,y=250)
        L.append(LB)
        LB=Label(root,text=N6,font=("italian",12,"bold"))
        LB.place(x=1200,y=250)
        L.append(LB)
        LB=Label(root,text=80*N6,font=("italian",12,"bold"))
        LB.place(x=1300,y=250)
        L.append(LB)

    #I7
    global N7
    if N7!=0:
        print(N7)
        LB=Label(root,text="Paratha",font=("italian",12,"bold"))
        LB.place(x=1050,y=270)
        L.append(LB)
        LB=Label(root,text=N7,font=("italian",12,"bold"))
        LB.place(x=1200,y=270)
        L.append(LB)
        LB=Label(root,text=25*N7,font=("italian",12,"bold"))
        LB.place(x=1300,y=270)
        L.append(LB)

    
    P=50*N1+90*N2+20*N3+100*N4+140*N5+80*N6+25*N7
    LB=Label(root,text="Total Bill                                    Rs.{}".format(P),font=("italian",12,"bold"))
    LB.place(x=1050,y=610)
    L.append(LB)



#RESET
def reset():
    global L
    global B
    global N1
    global N2
    global N3
    global N4
    global N5
    global N6
    global N7
    N1=0
    N2=0
    N3=0
    N4=0
    N5=0
    N6=0
    N7=0
    for i in L:
        i.destroy()
    for i in B:
        i['text']='Add'
    
    

#BILL
LB=Label(root,text="BILL",font=("italian",20,"bold"),bg='pink',height=1,width=25)
LB.place(x=1000,y=50)

OK=Button(root,text="OK",command=create_label,font=("italian",20,"bold"),height=1,width=5)
OK.place(x=1000,y=660)

RESET=Button(root,text="RESET",command=reset,font=("italian",20,"bold"),height=1,width=5)
RESET.place(x=1200,y=660)


root.mainloop()
