from tkinter import *
from tkinter import filedialog
import pygame
from pygame import mixer
from tkinter import ttk
from mutagen.mp3 import MP3
import threading
import time
import os

def automatic():
    global root,checkautomatic,scale_bar,checkm,paused
    checkm=1
    if pygame.mixer.music.get_busy():
        if not paused:
            scale_bar.set(scale_bar.get()+1)
    elif checkautomatic:
        next1()
    root.after(985,automatic)
    

def setlabel(label):
    global LABEL
    LABEL['text']=label

def add():
    global LISTBOX,songlist
    filename=filedialog.askopenfilename()
    songlist.append(filename)
    LISTBOX.insert(END,os.path.basename(filename))
    setlabel("Adding song to list")

def delete():
    global LISTBOX,songlist,checkautomatic
    checkautomatic=0
    index=LISTBOX.curselection()[0]
    setlabel(f"song:- {LISTBOX.get(index)} deleted")
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
    LISTBOX.delete(ANCHOR)
    print(index,'========',songlist)
    songlist.remove(songlist[index])
    
def setTL():
    global filename,TL,CL,length
    audio = MP3(filename)
    length=(audio.info.length)
    '''mi=int(length//60)
    sec=int(length-mi*60)
    _,ms=str(length-mi*60-sec).split('.')'''
    mi,sec=divmod(length,60)
    mi=round(mi)
    sec=round(sec)
    TL['text']=f"Total Length : {mi}.{sec}"
    CL['text']="Current Length : 0.0.0"
               
start=0
def playevent(event):
    global PLAY,LISTBOX,filename,songlist,scale_bar,length,checkm,start,checkautomatic
    checkautomatic=1
    index=LISTBOX.curselection()[0]
    filename=songlist[index]
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    setTL()
    setlabel(f"Playing:- {LISTBOX.get(index)}")
    scale.set(25)
    audio = MP3(filename)
    length=(audio.info.length)
    scale_bar['to']=length
    scale_bar['length']=length
    checkm=1
    scale_bar.set(0)
    if start==0:
        start=1
        automatic()
    
def play():
    global paused,LISTBOX,filename,songlist,length,scale_bar,checkautomatic
    checkautomatic=1
    if paused==True:
        paused=False
        pygame.mixer.music.unpause()
        index=LISTBOX.curselection()[0]
        return
    else:
        index=LISTBOX.curselection()[0]
        filename=songlist[index]
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(.05)
        setTL()
        setlabel(f"Playing:- {LISTBOX.get(index)}")
        audio = MP3(filename)
        length=(audio.info.length)
        scale_bar['to']=length
        scale_bar['length']=length
        scale_bar.set(0)
        
def previous():
    global LISTBOX,filename,songlist,scale_bar,checkautomatic
    checkautomatic=1
    index=LISTBOX.curselection()[0]
    file=LISTBOX.get(index)
    LISTBOX.delete(index)
    LISTBOX.insert(index,file)
    if index==0:
        index=len(songlist)-1
    else:
        index=index-1
    filename=songlist[index]
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    pygame.mixer.music.get_busy()
    LISTBOX.selection_set(index)
    setTL()
    setlabel(f"Playing:- {LISTBOX.get(index)}")
    audio = MP3(filename)
    length=(audio.info.length)
    scale_bar['to']=length
    scale_bar['length']=length
    scale_bar.set(0)

def next1():
    global LISTBOX,filename,songlist,scale_bar,checkautomatic
    checkautomatic=1
    index=LISTBOX.curselection()[0]
    file=LISTBOX.get(index)
    LISTBOX.delete(index)
    LISTBOX.insert(index,file)
    if index==(len(songlist)-1):
        index=0
    else:
        index=index+1
    filename=songlist[index]
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    pygame.mixer.music.get_busy()
    LISTBOX.selection_set(index)
    setTL()
    setlabel(f"Playing:- {LISTBOX.get(index)}")
    audio = MP3(filename)
    length=(audio.info.length)
    scale_bar['to']=length
    scale_bar['length']=length
    scale_bar.set(0)
    
def pause():
    global paused
    paused=True
    pygame.mixer.music.pause()
    setlabel("Music Paused")

def stop():
    global checkautomatic
    checkautomatic=0
    pygame.mixer.music.stop()
    setlabel("Music Stop")

def vol(x):
    global scale,filename,m,Iaudio
    x=scale.get()
    audio = MP3(filename)
    pygame.mixer.music.set_volume((x/100))
    m['image']=Iaudio
      
t=0.0
def m_length(x):
    global scale_bar,t,val,checkm,TL,CL
    val=float(x)-t
    t=float(x)
    if val>0 and checkm==0:
        pygame.mixer.music.set_pos(val)
    checkm=0
    mi,sec=divmod(float(x),60)
    mi=round(mi)
    sec=round(sec)
    CL['text']=f"Current length : {mi}.{sec}"
    
def mute():
    global MUTE,scale,m,Imute,Iaudio
    if MUTE==False:
        m['image']=Imute
        pygame.mixer.music.set_volume(0)
        MUTE=True
        return
    else:
        MUTE=False
        m['image']=Iaudio
        x=scale.get()
        pygame.mixer.music.set_volume((x/100))
        return
        
def restart():
    global scale_bar
    pygame.mixer.music.rewind()
    scale_bar.set(0)

def on_close():
    print("called")
    try:
        pygame.mixer.music.stop()
        root.destroy()
    except:
        pass    
        
def gui():
    global ADD,m,Iaudio,Imute,LISTBOX,DEL,PLAY,LABEL,scale_bar,paused,scale
    global TL,CL,mn,sec,ms,root,songlist,MUTE
    MUTE=False
    songlist=[]
    mn=0
    sec=0
    ms=0
    paused=False
    root=Tk()
    root.configure(bg='black')
    root.title("Music Player")
    style = ttk.Style()
    style.theme_use('clam')
    

    img=PhotoImage(file="background.png")
    aaa=Label(root,image=img,bg='black',fg='black')
    aaa.pack(fill=BOTH,expand=YES)
    frame1=Frame(aaa,bg='black')
    frame2=Frame(aaa,bg='black')
    f=Frame(frame1,bg='black')
    f.pack(side=TOP)
    style.configure("Horizontal.TScrollbar",
                background="Green", darkcolor="DarkGreen", lightcolor="LightGreen",
                troughcolor="#03f", bordercolor="black", arrowcolor="black")
    style.configure("Vertical.TScrollbar",
                background="Green", darkcolor="DarkGreen", lightcolor="LightGreen",
                troughcolor="#03f", bordercolor="black", arrowcolor="black")

    scrollbarx=ttk.Scrollbar(f,orient="horizontal")
    scrollbary=ttk.Scrollbar(f,orient="vertical")
    LISTBOX=Listbox(f,bg='black',fg='yellow',font='arial 12 bold',height=28,relief=RAISED
                    ,width=50,xscrollcommand=scrollbarx.set,yscrollcommand=scrollbary.set)
    scrollbarx.config(command=LISTBOX.xview)
    scrollbarx.pack(side="bottom", fill="x")
    scrollbary.config(command=LISTBOX.yview)
    scrollbary.pack(side="right", fill="y")
    LISTBOX.pack(side=TOP,pady=20)
    f2=Frame(frame1,bg='black')
    f2.pack(side=TOP)
    ADD=Button(f2,text='+ Add',command=add,bg='black',font='arial 15 bold',fg="yellow")
    ADD.pack(side=LEFT,padx=5)
    DEL=Button(f2,text='- Del',command=delete,bg='black',font='arial 15 bold',fg="yellow")
    DEL.pack(side=LEFT,padx=5)
    LABEL=ttk.Label(aaa,text="Music Player",font='italian 10 bold')
    LABEL.pack(side=BOTTOM,fill=X)


    f1=Frame(frame2,bg='black')
    f1.pack(side=TOP,pady=5)
    TL=Label(f1,text="Total Length : -:-",bg='black',fg='yellow',font='arial 11 bold')
    TL.pack(side=TOP,pady=15)
    CL=Label(f1,text="Current Length : -:-",bg='black',fg='yellow',font='arial 11 bold')
    CL.pack(side=TOP,pady=5)

    f1=Frame(frame2,bg='black')
    f1.pack(side=TOP,pady=25)

    Istart=PhotoImage(file="play.png")
    Ipause=PhotoImage(file="pause.png")
    Istop=PhotoImage(file="stop.png")
    Irestart=PhotoImage(file="restart.png")
    
    PLAY=ttk.Button(f1,image=Istart,command=play)
    PLAY.pack(side=LEFT)
    STOP=ttk.Button(f1,image=Istop,command=stop)
    STOP.pack(side=LEFT,padx=10)
    PAUSE=ttk.Button(f1,image=Ipause,command=pause)
    PAUSE.pack(side=LEFT,padx=10)
    RESTART=ttk.Button(f1,image=Irestart,command=restart)
    RESTART.pack(side=LEFT,padx=10)

    Iaudio=PhotoImage(file="audio.png")
    Imute=PhotoImage(file="mute.png")
    Inext111=PhotoImage(file="next.png")
    Iprev=PhotoImage(file="previous.png")
    
    f1=Frame(frame2,bg='black')
    f1.pack(side=TOP,pady=25)
    ttk.Button(f1,image=Iprev,command=previous).pack(side=LEFT,padx=10)
    m=Button(f1,image=Iaudio,command=mute)
    m.pack(side=LEFT,padx=10)
    ttk.Button(f1,image=Inext111,command=next1).pack(side=LEFT,padx=10)

    f1=Frame(frame2,bg='black')
    f1.pack(side=TOP,pady=25)
    scale=ttk.Scale(f1,from_=0,to=100,length=100,cursor='dot',command=vol,orient=HORIZONTAL)
    scale.pack(side=LEFT)

    f1=Frame(frame2,bg='black')
    f1.pack(side=TOP,pady=25)
    scale_bar=ttk.Scale(f1,from_=0,to=0,length=0,cursor='dot',command=m_length,
                    orient=HORIZONTAL)
    scale_bar.pack(side=LEFT)

    frame1.pack(side=LEFT)
    frame2.pack(side=RIGHT)
    LISTBOX.bind("<<ListboxSelect>>",playevent)
    s=Scrollbar(root)

    root.protocol("WM_DELETE_WINDOW",on_close)
    root.mainloop()
gui()
