import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time

def insert(name):#copy data from enquire to joined
    conn=sqlite3.connect("teacher.db")
    rows=conn.execute(f"select * from allbatch where batchcode='{name}'").fetchall()
    start=rows[0][3]
    end=rows[0][4]
    sub=rows[0][2]
    branch=rows[0][5]
    conn.close()
    
    conn=sqlite3.connect("course.db")
    rows=conn.execute(f'''select * from {sub} where branch_prefer="{branch}" and stime="{start}"
                                            and etime="{end}"''').fetchall()
    conn.close()

    conn=sqlite3.connect("joined.db")
    for i in rows:
        conn.execute(f'''insert into {name} values("{i[0]}","{i[1]}",0,0)''')
    conn.commit()
    conn.close()

#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

def createtable(name):
    try:
        conn=sqlite3.connect("joined.db")
        conn.execute(f'''create table if not exists {name}(r_no text primary key not null,
                    name text not null,total_c text not null,present text not null)''')
    except:
        pass
    finally:
        conn.commit()
        conn.close()

#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

def tobatch(Tk1,nam):
    global root
    root=Tk1
    createtable(nam)
    insert(nam)
