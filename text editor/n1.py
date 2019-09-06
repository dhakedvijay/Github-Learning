from tkinter import *
from tkinter import messagebox
import time
import webbrowser
from tkinter import filedialog
import os


def title(t):
    global root
    root.title(t)

def hello():
    print("hello")
    
def SAVE():
    global inut,fname,t,entry,ok,check,check_save,filepath
    if check_save==False:
        filepath=filedialog.asksaveasfilename(initialfile='Untitled.txt',
                                              defaultextension=".txt",
                                              filetypes=[("All Files","*.*")
                                                , ("Text Documents","*.txt")])
        check_save=True
        title(os.path.basename(filepath)[:len(os.path.basename(filepath))-4]+' - Notepad')
        if filepath != None:
            file=open(filepath,'w')
            data = text.get("1.0",END)
            file.write(data)
            file.close()
    else:
        file=open(filepath,'w')
        data = text.get("1.0",END)
        file.write(data)
        file.close()

def SAVEAS():
    global inut,fname,t,entry,ok,check,filepath
    filepath=filedialog.asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt"
                                          , filetypes=[("All Files","*.*")
                                                , ("Text Documents","*.txt")])
    title(os.path.basename(filepath)[:len(os.path.basename(filepath))-4]+' - Notepad')
    if filepath != None:
        file=open(filepath,'w')
        data = text.get("1.0",END)
        file.write(data)
        file.close()    

def OPEN():
    global text,name
    filename=filedialog.askopenfilename()
    print(filename)
    if '.txt' == filename[(len(filename)-4):]:
        name=os.path.basename(filename)
        try:
            file=open(name,"r")
            lines=file.readlines()
            print(lines)
            text.delete(1.0, END)
            for line in lines:
                text.insert(END, line)
        except EOFError as e:
            pass
        finally:
            file.close()
            title(name[:(len(name)-4)]+" - Notepad")
    else:
        messagebox.showerror("Error","Invalid Type Of File")
        OPEN()
    
def NEW():
    global root
    root.destroy()
    create()

def PRINT():
    messagebox.showerror("Error","Your System Does Not Support Printing")

def PAGESETUP():
    root.geometry("400x400")

def UNDO():
    global data,edata
    data = text.get("1.0",END)
    text.delete(1.0, END)
    text.insert(END, edata[:(len(edata)-1)])
    edata=data
    
def GOOGLE():
    webbrowser.open('https://www.google.co.in/')

def CUT():
    text.event_generate("<<Cut>>")

def COPY():
    text.event_generate("<<Copy>>")

def PASTE():
    text.event_generate("<<Paste>>")

def DELETE():
    text.event_generate("<<Delete>>")

def find():
    global text,s
    inpt=text.get('1.0',END)
    search=s.get()
    l=[]
    if search in inpt:
        l=list(inpt.split('\n'))
        for j,i in enumerate(l,1):
            if search in i:
                m=0
                for k in range(len(search),len(i)+1):
                    if search==i[m:k]:
                        starting=f"{j}.{m}"
                        ending=f"{j}.{k}"
                        text.tag_add("Write Here", starting, ending)
                        text.tag_config("Write Here", background="blue", foreground="white")
                    m+=1
    else:
        messagebox.showerror("Error","Not founnd")
        
def FIND():
    global root,s
    top=Toplevel(root)
    top.title("FIND")
    top.geometry("300x100+400+350")
    Label(top,text="Find what:").place(x=10,y=30)
    s=StringVar()
    e=Entry(top,text=s,width=20)
    e.place(x=80,y=30)
    ok=Button(top,text="Ok",width=7,command=find)
    ok.place(x=220,y=15)

def replace():
    global text,st,rep
    inpt=text.get('1.0',END)
    search=st.get()
    l=[]
    if search in inpt:
        l=list(inpt.split('\n'))
        for j,i in enumerate(l,1):
            if search in i:
                m=0
                for k in range(len(search),len(i)+1):
                    if search==i[m:k]:
                        starting=f"{j}.{m}"
                        ending=f"{j}.{k}"
                        text.replace(starting,ending,rep.get())
                        return
                    m+=1
    else:
        messagebox.showerror("Error","Not founnd")
    

def REPLACE():
    global root,st,rep
    top=Toplevel(root)
    top.title("REPLACE")
    top.geometry("300x100+400+350")
    Label(top,text="Find what:").place(x=10,y=30)
    Label(top,text="Replace with:").place(x=10,y=50)
    st=StringVar()
    rep=StringVar()
    e=Entry(top,text=st,width=20)
    e.place(x=80,y=30)
    e=Entry(top,text=rep,width=20)
    e.place(x=80,y=50)
    ok=Button(top,text="Ok",width=7,command=replace)
    ok.place(x=220,y=15)

def find_next():
    global findcount,text,stf,find_list
    find_list=[]
    inpt=text.get('1.0',END)
    search=stf.get()
    l=[]
    if search in inpt :
        l=list(inpt.split('\n'))
        for j,i in enumerate(l,1):
            if search in i:
                m=0
                for k in range(len(search),len(i)+1):
                    if search==i[m:k]:
                        starting=f"{j}.{m}"
                        ending=f"{j}.{k}"
                        find_list.append((starting,ending))
                    m+=1
        print(findcount,len(find_list))
    if findcount>len(find_list):
        findcount=1
    if len(find_list)!=0:
        text.tag_add("Write Here", find_list[findcount-1][0], find_list[findcount-1][1])
        text.tag_config("Write Here", background="blue", foreground="white")
    else:
        messagebox.showerror("Error","Not founnd")
        return                    
        
def FIND_NEXT():
    global text,stf,findcount
    findcount+=1
    top=Toplevel(root)
    top.title("FIND_NEXT")
    top.geometry("300x100+400+350")
    Label(top,text="Find what:").place(x=10,y=30)
    stf=StringVar()
    e=Entry(top,text=stf,width=20)
    e.place(x=80,y=30)
    ok=Button(top,text="Ok",width=7,command=find_next)
    ok.place(x=220,y=15)
    
def SELECTALL():
    global text
    l=[]
    inut=text.get('1.0',END)
    l=inut.split('\n')
    text.tag_add("Write Here", '1.0',f'{len(l)}.0')
    text.tag_config("Write Here", background="blue", foreground="white")
    return

def goto():
    global text,sf,top
    inut=text.get("1.0",END)
    length=len(inut.split('\n'))
    if int(sf.get())<=length:
        text.insert(f"{sf.get()}.0",'')
        top.destroy()
        return
    else:
        messagebox.showerror("Error","Invalid Lenght")
    

def GOTO():
    global sf,top
    top=Toplevel(root)
    top.title("FIND_NEXT")
    top.geometry("300x100+400+350")
    Label(top,text="enter line no:").place(x=10,y=30)
    sf=StringVar()
    e=Entry(top,text=sf,width=5)
    e.place(x=100,y=30)
    ok=Button(top,text="Ok",width=7,command=goto)
    ok.place(x=220,y=15)

def TIME():
    global text
    text.insert(END,time.ctime())

def DONE():
    global text,var
    f=int(var.get())
    text['font']=f'italian {f} bold'

def FONT():
    global var
    top=Toplevel(root)
    top.title("FONT")
    top.geometry("300x100+400+350")
    Label(top,text="enter font").place(x=10,y=30)
    var=StringVar()
    Entry(top,text=var).place(x=100,y=30)
    Button(top,text="Ok",width=10,command=DONE).place(x=80,y=60)
    
def ZOOMIN():
    global text,font
    font+=3
    text['font']=f'italian {font} bold'

def ZOOMOUT():
    global text,font
    font-=3
    text['font']=f'italian {font} bold'

def DEFAULTZOOM():
    global text,font
    font=15
    text['font']=f'italian {font} bold'

def VIEWHELP():
    webbrowser.open('https://www.python-course.eu/')

def ABOUT():
    top=Toplevel(root)
    top.title("FONT")
    top.geometry("80x80+400+350")
    m=Message(top,text="This Is Python Text Editor",font=('Bradley Hand ITC',15,'bold'),
              bg='light green')
    m.place(x=0,y=0) 
    
def create():
    global check,text,name,root,edata,findcount,find_list,font,check_save
    check_save=False
    font=15
    find_list=[]
    findcount=0
    edata=''
    name=None
    root=Tk()
    root.geometry('1000x515+200+150')
    title("Untitled - Notepad")
    root.configure(background='white')
    menubar=Menu(root)
    check=0
    #FILE
    filemenu=Menu(menubar,tearoff=0)
    filemenu.add_command(label="New",command=NEW)
    filemenu.add_command(label="Open...",command=OPEN)
    filemenu.add_command(label="Save",command=SAVE)
    filemenu.add_command(label="Save As...",command=SAVEAS)
    filemenu.add_separator()
    filemenu.add_command(label="Page Setup...",command=PAGESETUP)
    filemenu.add_command(label="Print...",command=PRINT)
    filemenu.add_separator()
    filemenu.add_command(label="Exit",command=root.destroy)
    menubar.add_cascade(label="File",menu=filemenu)
    
    #EDIT
    editmenu=Menu(menubar,tearoff=0)
    editmenu.add_command(label="Undo",command=UNDO)
    editmenu.add_separator()
    editmenu.add_command(label="Cut",command=CUT)
    editmenu.add_command(label="Copy",command=COPY)
    editmenu.add_command(label="Paste",command=PASTE)
    editmenu.add_command(label="Delete",command=DELETE)
    editmenu.add_separator()
    editmenu.add_command(label="Search with Google...",command=GOOGLE)
    editmenu.add_command(label="Find...",command=FIND)
    editmenu.add_command(label="Find Next",command=FIND_NEXT)
    editmenu.add_command(label="Replace...",command=REPLACE)
    editmenu.add_command(label="Go To...",command=GOTO)
    editmenu.add_separator()
    editmenu.add_command(label="Select All",command=SELECTALL)
    editmenu.add_command(label="Time/Date",command=TIME)
    menubar.add_cascade(label="Edit",menu=editmenu)

    #FORMAT
    formatmenu=Menu(menubar,tearoff=0)
    formatmenu.add_command(label="Word Wrap",command=hello)
    formatmenu.add_command(label="Font...",command=FONT)
    menubar.add_cascade(label="Format",menu=formatmenu)

    #VIEW
    viewmenu=Menu(menubar,tearoff=0)
    zvmenu=Menu(viewmenu,tearoff=0)
    zvmenu.add_command(label="Zoom In",command=ZOOMIN)
    zvmenu.add_command(label="Zoom Out",command=ZOOMOUT)
    zvmenu.add_command(label="Restore Default Zoom",command=DEFAULTZOOM)
    viewmenu.add_cascade(label="Zoom",menu=zvmenu)
    viewmenu.add_command(label="Status Bar",command=hello)
    menubar.add_cascade(label="View",menu=viewmenu)

    #HELP
    helpmenu=Menu(menubar,tearoff=0)
    helpmenu.add_command(label="View Help",command=VIEWHELP)
    helpmenu.add_separator()
    helpmenu.add_command(label="About Notepad",command=ABOUT)
    menubar.add_cascade(label="Help",menu=helpmenu)                                  
    root.config(menu=menubar)

    text=Text(root,font=f'italian {font} bold',width=66,height=16)
    text.grid()
    root.mainloop()

create()
