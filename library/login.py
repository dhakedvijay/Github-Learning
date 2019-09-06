from tkinter import *
import os
import backend
def clear():
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)
    entry4.delete(0,END)

def add_command():
    """Insert entry via button."""
    backend.insert(title_text.get(),
                    author_text.get(),
                    year_text.get(), 
                    isbn_text.get())
    listing.delete(0, END)
    listing.insert(END, 
                    (title_text.get(), 
                    author_text.get(), 
                    year_text.get(), 
                    isbn_text.get()))
    clear()

def view_command():
    """View entries via button."""
    listing.delete(0, END)
    for row in backend.view():
        listing.insert(END, row)

def update_command():
    """Update entry via button."""
    backend.update(selected_tuple[0], 
                    title_text.get(), 
                    author_text.get(), 
                    year_text.get(), 
                    isbn_text.get())

def delete_command():
    """Delete entry via button."""
    backend.delete(selected_tuple[0])
    clear()
    view_command()

def search_command():
    """Search entry via button."""
    listing.delete(0, END)
    for row in backend.search(title_text.get(), 
                                author_text.get(), 
                                year_text.get(), 
                                isbn_text.get()):
        listing.insert(END, row)

def get_selected_row(event):
    """Pre-fill fields for selected entry."""
    try:
        global selected_tuple
        index = listing.curselection()[0]
        clear()
        selected_tuple = listing.get(index)        
        entry1.insert(END, selected_tuple[1])
        entry2.insert(END, selected_tuple[2])
        entry3.insert(END, selected_tuple[3])
        entry4.insert(END, selected_tuple[4])
    except:
        pass
def f():
    window = Toplevel(login_screen)
    window.title("Library Management System")
    window.geometry("550x550+100+100")
    window.config(bg='black')
    label1 = Label(window, text = "Title",bg="powder blue",fg='green',font="Times 15 bold",
               relief=RAISED,bd=4)
    label1.grid(row = 0, column = 0,padx=5,pady=5,sticky='nswe')

    label2 = Label(window, text = "Author",bg="powder blue",fg='green',font="Times 15 bold",relief=RAISED,bd=4)
    label2.grid(row = 0, column = 2,padx=5,pady=5,sticky='nswe')

    label3 = Label(window, text = "Year",bg="powder blue",fg='green',font="Times 15 bold",relief=RAISED,bd=4)
    label3.grid(row = 1, column = 0,padx=5,pady=5,sticky='nswe')

    label4 = Label(window, text = "ISBN",bg="powder blue",fg='green',font="Times 15 bold",relief=RAISED,bd=4)
    label4.grid(row = 1, column = 2,padx=5,pady=5,sticky='nswe')

    # Entry Fields.
    global title_text
    title_text = StringVar()
    global entry1
    entry1 = Entry(window, textvariable = title_text,bg="powder blue",fg='green',font="Times 15 bold",relief=RAISED,bd=4)
    entry1.grid(row = 0, column = 1,padx=5,pady=5,sticky='nswe')
    global author_text
    author_text = StringVar()
    global entry2
    entry2 = Entry(window, textvariable = author_text,bg="powder blue",fg='green',font="Times 15 bold",relief=RAISED,bd=4)
    entry2.grid(row = 0, column = 3,padx=5,pady=5,sticky='nswe')
    global year_text
    year_text = StringVar()
    global entry3
    entry3 = Entry(window, textvariable = year_text,bg="powder blue",fg='green',font="Times 15 bold",relief=RAISED,bd=4)
    entry3.grid(row = 1, column = 1,padx=5,pady=5,sticky='nswe')
    global isbn_text
    isbn_text = StringVar()
    global entry4
    entry4 = Entry(window, textvariable = isbn_text,bg="powder blue",fg='green',font="Times 15 bold",relief=RAISED,bd=4)
    entry4.grid(row = 1, column = 3,padx=5,pady=5,sticky='nswe')
    global listing
    # List all data.
    listing = Listbox(window, height = 16, width = 35,bg='pink',fg='red',
                      font="Times 15 bold")
    listing.grid(row = 2, column = 0, rowspan = 6,padx=5,pady=5,columnspan = 3,sticky='nswe')
    listing.bind('<<ListboxSelect>>', get_selected_row)
    listing.bind('<Enter>',EListing)
    listing.bind('<Leave>',LListing)
    # Buttons for various operations on data.
    global button1
    global button2
    global button3
    global button4
    global button5
    global button6
    button1 = Button(window, 
                    text = "View All", 
                    width = 12, 
                    command = view_command,bg="powder blue",fg='green',font="Times 15 bold")
    button1.grid(row = 2, column = 3,pady=5,sticky='nswe')
    button1.bind("<Enter>",EButton1)
    button1.bind("<Leave>",LButton1)
    button2 = Button(window, 
                    text = "Search Entry", 
                    width = 12, 
                    command = search_command,bg="powder blue",fg='green',font="Times 15 bold")
    button2.grid(row = 3, column = 3,pady=5,sticky='nswe')
    button2.bind("<Enter>",EButton2)
    button2.bind("<Leave>",LButton2)
    
    button3 = Button(window, 
                    text = "Add Entry", 
                    width = 12, 
                    command = add_command,bg="powder blue",fg='green',font="Times 15 bold")
    button3.grid(row = 4, column = 3,pady=5,sticky='nswe')
    button3.bind("<Enter>",EButton3)
    button3.bind("<Leave>",LButton3)
    
    button4 = Button(window, 
                    text = "Update Selected", 
                    width = 12, 
                    command = update_command,bg="powder blue",fg='green',font="Times 15 bold")
    button4.grid(row = 5, column = 3,pady=5,sticky='nswe')
    button4.bind("<Enter>",EButton4)
    button4.bind("<Leave>",LButton4)
    
    button5 = Button(window, 
                    text = "Delete Selected", 
                    width = 12, 
                    command = delete_command,bg="powder blue",fg='green',font="Times 15 bold")
    button5.grid(row = 6, column = 3,pady=5,sticky='nswe')  
    button5.bind("<Enter>",EButton5)
    button5.bind("<Leave>",LButton5)
    button6 = Button(window, 
                    text = "Close", 
                    width = 12, 
                    command = window.destroy,bg="powder blue",fg='green',font="Times 15 bold")
    button6.grid(row = 7, column = 3,pady=5,sticky='nswe')
    button6.bind("<Enter>",EButton6)
    button6.bind("<Leave>",LButton6)
    for i in range(8):
        window.grid_rowconfigure(i,weight=1)
    for i in range(4):
        window.grid_columnconfigure(i,weight=1)
    # Keep window open until closed.
    window.mainloop()




def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("400x450+200+200")

    C = Canvas(register_screen)
    filename = PhotoImage(file ="lalit3.png")
    background_label = Label(C, image=filename,bg='black')
    background_label.pack(fill=BOTH,expand=YES)
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(background_label, text="Please enter details below",relief=RAISED,bd=4, font=("Calibri",23,'bold'),width="30",bg='powder blue').pack(padx=10,pady=10)
    username_lable = Label(background_label, text="Username * ",relief=RAISED,bd=4,font=("Calibri",23,'bold'),width="30",bg='powder blue')
    username_lable.pack(padx=10,pady=10)
    username_entry = Entry(background_label,relief=RAISED,bd=4, textvariable=username,font=("Calibri",23,'bold'),bg='pink',width="30")
    username_entry.pack(padx=10,pady=10)
    password_lable = Label(background_label, text="Password * ",relief=RAISED,bd=4,font=("Calibri",23,'bold'),width="30",bg='powder blue')
    password_lable.pack(padx=10,pady=10)
    password_entry = Entry(background_label, textvariable=password, show='*',relief=RAISED,bd=4,font=("Calibri",23,'bold'),bg='pink',width="30")
    password_entry.pack(padx=10,pady=10)
    global b4
    b4=Button(background_label, text="Register", bg='pink',height="2",relief=RAISED,bd=4, width="30", command = register_user,font=("Calibri",23,'bold'))
    b4.pack(padx=10,pady=10)
    b4.bind("<Enter>",Enter4)
    b4.bind("<Leave>",Leave4)
    C.pack(fill=BOTH,expand=YES)
    register_screen.mainloop()
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("400x450+200+200")

    C = Canvas(login_screen)
    filename = PhotoImage(file ="lalit3.png")
    background_label = Label(C, image=filename,bg='black')
    background_label.pack(fill=BOTH,expand=YES)
    
    Label(background_label,text="Please Enter Login Details",relief=RAISED,bd=4,bg='powder blue',font=("Calibri",23,'bold'),width="30").pack(padx=10,pady=10)
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(background_label, text="Username * ",relief=RAISED,bd=4,font=("Calibri",23,'bold'),width="30",bg='powder blue').pack(padx=10,pady=10)
    username_login_entry = Entry(background_label, width="30",relief=RAISED,bd=4,textvariable=username_verify,font=("Calibri",23,'bold'),bg='pink')
    username_login_entry.pack(padx=10,pady=10)
    Label(background_label, text="Password * ",font=("Calibri",23,'bold'),relief=RAISED,bd=4,bg='powder blue',width="30").pack(padx=10,pady=10)
    password_login_entry = Entry(background_label,bg='pink',relief=RAISED,bd=4,
                                 width="30", textvariable=password_verify,
                                 show= '*',font=("Calibri",23,'bold'))
    password_login_entry.pack(padx=10,pady=10)
    global b3
    b3=Button(background_label, text="Login", bg='pink',height="2", width="30",relief=RAISED,bd=4, command = login_verify,font=("Calibri",23,'bold'))
    b3.pack(padx=10,pady=10)
    b3.bind("<Enter>",Enter3)
    b3.bind("<Leave>",Leave3)
    C.pack(fill=BOTH,expand=YES)
    login_screen.mainloop()
# Implementing event on register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack(fill=BOTH,expand=YES)
 
# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            f()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 
# Designing popup for login success
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack(fill=BOTH,expand=YES)
    Button(login_success_screen, text="OK", command=delete_login_success).pack(fill=BOTH,expand=YES)
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ",relief=RAISED,bd=4,font=("Calibri",23,'bold'),width="30",bg='powder blue').pack(padx=10,pady=10)
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised,relief=RAISED,bd=4,font=("Calibri",23,'bold'),width="30",bg='pink').pack(padx=10,pady=10)
 

 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("250x250")
    Label(user_not_found_screen, text="User Not Found",relief=RAISED,bd=4,font=("Calibri",23,'bold'),width="30",bg='powder blue').pack(padx=10,pady=10)
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen,relief=RAISED,bd=4,font=("Calibri",23,'bold'),width="30",bg='pink').pack(padx=10,pady=10)
 
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 
# Designing Main(first) window
def Enter(event):
    b1['bg']='red'
    b1['fg']='white'
def Leave(event):
    b1['bg']='powder blue'
    b1['fg']='black'
def Enter1(event):
    b2['bg']='red'
    b2['fg']='white'
def Leave1(event):
    b2['bg']='powder blue'
    b2['fg']='black'
def Enter4(event):
    b4['bg']='red'
    b4['fg']='white'
def Leave4(event):
    b4['bg']='pink'
    b4['fg']='black'
def Enter3(event):
    b3['bg']='red'
    b3['fg']='white'
def Leave3(event):
    b3['bg']='pink'
    b3['fg']='black'

def EButton1(event):
    button1['bg']='red'
    button1['fg']='white'
def LButton1(event):
    button1['bg']='powder blue'
    button1['fg']='black'

def EButton2(event):
    button2['bg']='red'
    button2['fg']='white'
def LButton2(event):
    button2['bg']='powder blue'
    button2['fg']='black'

def EButton3(event):
    button3['bg']='red'
    button3['fg']='white'
def LButton3(event):
    button3['bg']='powder blue'
    button3['fg']='black'

def EButton4(event):
    button4['bg']='red'
    button4['fg']='white'
def LButton4(event):
    button4['bg']='powder blue'
    button4['fg']='black'

def EButton5(event):
    button5['bg']='red'
    button5['fg']='white'
def LButton5(event):
    button5['bg']='powder blue'
    button5['fg']='black'

def EButton6(event):
    button6['bg']='red'
    button6['fg']='white'
def LButton6(event):
    button6['bg']='powder blue'
    button6['fg']='black'

def EListing(event):
    listing['bg']='red'
    listing['fg']='white'
def LListing(event):
    listing['bg']='pink'
    listing['fg']='black'


def main_account_screen():
    global main_screen
    global b1
    global b2
    main_screen = Tk()
    main_screen.geometry("400x450+200+200")
    main_screen.title("Account Login")
    C = Canvas(main_screen,bg='black')
    filename = PhotoImage(file ="lalit3.png")
    background_label = Label(C, image=filename,bg='black')
    background_label.pack(fill=BOTH,expand=YES)
    
    Label(background_label,text="Select Your Choice",relief=RAISED,bd=4, bg="powder blue",width="30", height="2", font=("Calibri",23,'bold')).pack(padx=10,pady=10)
    b1=Button(background_label,text="Login", height="2",relief=RAISED,bd=4,
              width="30",bg='powder blue', command = login,font=("Calibri",23,'bold'))
    b1.bind("<Enter>",Enter)
    b1.bind("<Leave>",Leave)
    b1.pack(padx=10,pady=10)
    b2=Button(background_label,text="Register", height="2",relief=RAISED,bd=4, width="30",bg='powder blue',command=register,font=("Calibri",23,'bold'))
    b2.bind("<Enter>",Enter1)
    b2.bind("<Leave>",Leave1)
    b2.pack(padx=10,pady=10)
    C.pack(fill=BOTH,expand=YES)
    main_screen.mainloop()
 
 
main_account_screen()

