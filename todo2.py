from tkinter import *
from tkinter import messagebox
import sqlite3 as sqlite


count=0
def add():
    global count
    value=task.get()
    if value !="":
        con=sqlite.connect('todo.db')
        with con:
            cur=con.cursor()
            cur.execute("insert into task values(?,?)",(count,value))
            lb.insert(END,str(count)+") "+value)
            task.delete(0,"end")
            count+=1
    else:
        messagebox.showwarning("warning","Please enter some task!")

def delete_task():
    value=lb.get(lb.curselection())
    con=sqlite.connect('todo.db')
    with con:
        cur=con.cursor()
        cur.execute("delete from task where id=?",list(value)[0])
        lb.delete(ANCHOR)
  

def display():
    global count
    con=sqlite.connect('todo.db')
    with con:
        cur=con.cursor()
        cur.execute("select * from task")
        results=cur.fetchall()
        for result in results:
            lb.insert(END,str(result[0])+") "+str(result[1]))
            count=result[0]
        count+=1


window=Tk()
window.geometry("500x450")
window.title("TODO Schedule Planner")
window.config(bg='#223441')

frame=Frame(window)
frame.pack(pady=10)

lb=Listbox(frame,width=25,height=8,font=('Times',18),bd=0,fg='#464646')
lb.pack(side=LEFT,fill=BOTH)

sb=Scrollbar(frame)
sb.pack(side=RIGHT,fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

task=Entry(window,font=('times',18))
task.pack(pady=20)
display()

bframe=Frame(window)
bframe.pack(pady=5)

abutton=Button(bframe,text="Add",font=('times',14),command=add)
abutton.pack(fill=BOTH,side=LEFT)

bbutton=Button(bframe,text="Delete",font=('times',14),command=delete_task)
bbutton.pack(fill=BOTH,side=RIGHT)


window.mainloop()
