import tkinter
from tkinter import *

root =Tk()
root.title("TO-DO-List")
root.geometry("400x650+400+100")
root.resizable(False,False)

#crate task
task_list= []

def addTask():
    task = taskEntry.get()
    taskEntry.delete(0, END)

    if task:
        with open("tasklist.txt",'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        tasks.insert(END,task)

def deleteTask():
    global task_list
    task = str(tasks.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt","w") as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")
        tasks.delete(ANCHOR)

def openTaskFile():

    try:
        global task_list

        with open("tasklist.txt","r") as taskfile:
            taskss = taskfile.readlines()

        for task in taskss:
            if task != '\n':
                task_list.append(task)
                tasks.insert(END, task)
    except:
        file = open('tasklist.txt','w')
        file.close()


#icons
imgIcon = PhotoImage(file="task.png")
root.iconphoto(False,imgIcon)

#top
#TopImg = PhotoImage(file="b.png")
#Label(root,image=TopImg).pack()

heading = Label(root, text="All Tasks", font=('Times', 20), fg="black")
heading.place(x=130,y=20)

frame = Frame(root,width=400,height=50,bg="white")
frame.place(x=0,y=100)

task=StringVar()
taskEntry = Entry(frame, width=18,font="arial 20", bd=0)
taskEntry.place(x=10,y=7)
taskEntry.focus()

btn = Button(frame, text="Create", font="Times 20 ", width=6, bg="sandybrown", fg="black", bd=0, command=addTask )
btn.place(x=310, y=0)

#tasks
frame1 = Frame(root,bd=3, width=700, height=280, bg="#32405b")
frame1.pack(pady=(180,0))

tasks = Listbox(frame1,font=('Times', 12),width=40, height=16, fg="white", bg="#32405b", cursor="hand2", selectbackground="#5a95ff")
tasks.pack(side=LEFT, fill=BOTH, padx=2)

scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

tasks.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=tasks.yview)

openTaskFile()
#delete
#DeleteIcon = PhotoImage(file="delete.jpg")
#Button(root, image=DeleteIcon, bd=0).pack(side=BOTTOM, pady=13)
deletebtn = Button(text="Delete", font="Times 20 ", width=6, bg="sandybrown", fg="black", bd=0, command=deleteTask )
deletebtn.pack(side=BOTTOM, pady=13)



root.mainloop()

