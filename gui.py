from cProfile import label
import tkinter as tk
from tkinter import messagebox
import webbrowser
import random

root = tk.Tk()
root.title("Interactive CPU Scheduler")
size = "1000x500"
size_out = "1000x400"
root.geometry(size)


def goto_user_queue():
    second = tk.Toplevel()
    second.geometry(size)
    root.withdraw()
    e1 = tk.Entry(second)
    e2 = tk.Entry(second)
    e3 = tk.Entry(second)
    lab1 = tk.Label(second, text="Process ID:", font=("New Times Roman", 20, "normal"))
    lab2 = tk.Label(second, text="Burst Time:", font=("New Times Roman", 20, "normal"))
    lab3 = tk.Label(second, text="Arrival Time:", font=("New Times Roman", 20, "normal"))

    e1.grid(row=1, column=0, padx=115, pady=10, ipady=4, ipadx=2)
    e2.grid(row=1, column=1, padx=115, pady=10, ipady=4, ipadx=2)
    e3.grid(row=1, column=2, padx=115, pady=10, ipady=4, ipadx=2)
    lab1.grid(row=0, column=0, padx=30, pady=30)
    lab2.grid(row=0, column=1, padx=20, pady=30)
    lab3.grid(row=0, column=2, padx=30, pady=30)

    global row
    row = 30
    global count
    count = 0
    queue = []
    def give_row():
        global row
        row += 1
        return row
    def add_process():
        global count
        count += 1
        try:
            pid = int(e1.get())
            burst_time = int(e2.get())
            arr_time = int(e3.get())
        except:
            messagebox.showerror("Invalid Input!", "One or more than one inputs aren't integers. Retry.")
            return
        user_process = (pid, burst_time, arr_time)
        for pr in queue:
            if user_process[0] == pr[0]:
                messagebox.showerror("Process IDs should be unique!", "You entered a Process ID which isn't unique.")
                e1.delete(0, tk.END)
                return
        if len(queue) > 6:
            messagebox.showwarning("Max Inputs Reached!", "User can input maximum of 7 processes.")
            return
        row1 = give_row()
        if count == 1:
            lab4 = tk.Label(second, text="Process ID", font=("New Times Roman", 10, "normal"))
            lab5 = tk.Label(second, text="Burst Time", font=("New Times Roman", 10, "normal"))
            lab6 = tk.Label(second, text="Arrival Time", font=("New Times Roman", 10, "normal"))
            lab4.grid(row=3, column=0, padx=30, pady=10)
            lab5.grid(row=3, column=1, padx=20, pady=10)
            lab6.grid(row=3, column=2, padx=30, pady=10)
        value1 = tk.Label(second, text = pid, font=("Times New Roman", 15, "normal")).grid(row=row1, column=0,)
        value2 = tk.Label(second, text=burst_time, font=("Times New Roman", 15, "normal")).grid(row=row1, column=1)
        value3 = tk.Label(second, text=arr_time, font=("Times New Roman", 15, "normal")).grid(row=row1, column=2)
        queue.append(user_process)
        e1.delete(0, tk.END)
        e2.delete(0, tk.END)
        e3.delete(0, tk.END)
    count=0
    b1 = tk.Button(second, text="Go to Main", height=2, command=lambda:goto_main(second))
    b2 = tk.Button(second, text="Add Process", height=2,  command=add_process)
    #b3 = tk.Button(second, text="Submit", height=2, command=lambda:goto_submission(second, queue))
    b1.grid(row=2, column=0, padx=50, pady=50, sticky=tk.NSEW)
    b2.grid(row=2, column=1, padx=50, pady=50, sticky=tk.NSEW)
    b3.grid(row=2, column=2, padx=50, pady=50, sticky=tk.NSEW)

def goto_main(second):
    root.deiconify()
    second.withdraw()

def goto_about():
    about = tk.Toplevel()
    about.geometry(size_out)
    root.withdraw()
    def callback(event):
        webbrowser.open_new(event.widget.cget("text"))
    contact0 ="Keshav Garg"
    

    collab = tk.Label(about, text="Collaborators", font=("Times New Roman", 15, "normal"))
    cnt0 = tk.Label(about, text=contact0, justify=tk.LEFT, font=("Times New Roman", 10, "normal"))

    email = tk.Label(about, text="Email", font=("Times New Roman", 15,"normal"))
    lbl0 = tk.Label(about, text=r"keshav.garg2410@gmail.com ", fg="blue", cursor="hand2", anchor="e")
    
    
    lbl0.bind("<Button-1>", callback)
    
    tk.Label(about, text=" ").grid(row=0, column=0, padx=20)
    tk.Label(about, text=" ").grid(row=0, column=1, pady=30)
    collab.grid(row=1, column=1, padx=80, pady=10, sticky=tk.W)
    cnt0.grid(row=2, column=1, padx=80, sticky=tk.W)
    
    email.grid(row=1, column=3, padx=80, pady=10, sticky=tk.W)
    lbl0.grid(row=2, column=3, padx=80, sticky=tk.W)
    
    
    b1 = tk.Button(about, text="Go to Main", height=2, command=lambda:goto_main(about)).grid(row=8, column=2, pady=60)


bg = tk.PhotoImage(file = "cpu.png")
label1 = tk.Label( root, image = bg)
label1.place(x = 0,y = 0)
w = tk.Label(root, text = "Welcome to CPU Scheduling Algorithms project.\nChoose:", font=('Times New Roman', 18 ,'normal'),bg = "#88cffa")
b2 = tk.Button(root, text="User-Created Queue Generation", height=3, command=goto_user_queue)
b3 = tk.Button(root, text="Quit", height=3, command=root.quit)
b4 = tk.Button(root, text="Contact Us", height=3, command=goto_about)
w.grid(row=0, column=0, padx=400, pady=70, columnspan=3, sticky=tk.EW)
b2.grid(row=1, column=1, sticky=tk.NSEW, padx=10, pady=10)
b3.grid(row=2, column=1, sticky=tk.NSEW, padx=20, pady=10)
b4.grid(row=3, column=1, sticky=tk.NSEW, padx=20, pady=10)
root.mainloop()
