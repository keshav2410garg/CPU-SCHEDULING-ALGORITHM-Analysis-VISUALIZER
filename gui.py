from cProfile import label
import tkinter as tk
from tkinter import messagebox
import webbrowser
import random
import fcfs
import sjf_non_pre
import round_robin

root = tk.Tk()
root.title("Interactive CPU Scheduler")
size = "1000x500"
size_out = "1000x400"
root.geometry(size)

def algo(algorithm, queue):
    def show_output(algorithm, output):
        def ret():
            top_out.grid_forget()
            label.grid_forget()
            button.grid_forget()
            output_win.destroy()
            
        output_win = tk.Toplevel()
        output_win.geometry(size)
        button = tk.Button(output_win, text="Go Back", command=ret, height=2, width=14)

        wait_time = output[0]
        response_time = output[1]
        turnaround_time = output[2]
        throughput = output[3]
        out = f"Average Waiting Time: {round(wait_time,2)}\n\nAverage Response Time: {round(response_time,2)}\n\nAverage Turnaround Time: {round(turnaround_time,2)}\n\nThroughput: {round(throughput,2)}"
        label = tk.Label(output_win, text=out, justify="left", font=("Times New Roman", 12, "normal"))
        top_out = tk.Label(output_win, text=f"Selected Algorithm\n({algorithm})", font=("Times New Roman", 15, "normal"))
        t1 = tk.Label(output_win, text="Process ID", font=("Times New Roman", 15, "normal"))
        t2 = tk.Label(output_win, text="Burst Time", font=("Times New Roman", 15, "normal"))
        t3 = tk.Label(output_win, text="Arrival Time", font=("Times New Roman", 15, "normal"))
        tk.Label(output_win, text="  ").grid(row=0, column=0, padx=60)
        t1.grid(row=0, column=1, padx=60, pady=20)
        t2.grid(row=0, column=2, pady=20)
        t3.grid(row=0, column=3, padx=60, pady=20)
        pri = [process[0] for process in queue]
        burst = [process[1] for process in queue]
        arriv = [process[2] for process in queue]
        for i in range(len(pri)):
            tk.Label(output_win, text=pri[i], font=("Times New Roman", 12, "normal")).grid(row=1+i, column=1)
            tk.Label(output_win, text=burst[i], font=("Times New Roman", 12, "normal")).grid(row=1+i, column=2)
            tk.Label(output_win, text=arriv[i], font=("Times New Roman", 12, "normal")).grid(row=1+i, column=3)
        top_out.grid(row=10, column=1, padx=60, pady=10)
        label.grid(row=11, column=1, padx=60)
        button.grid(row=12, column=2, sticky=tk.NSEW)
    if algorithm == "First Come First Serve":
        output = fcfs.fcfs(queue)
    elif algorithm == "Shortest Job First":
        output = sjf_non_pre.sjf_non_pre(queue)
    elif algorithm == "Round Robin":
        value = extra.get()
        output = round_robin.round_robin(queue, value)
    elif algorithm == "Multi Level Queue":
        pass
    else:
        messagebox.showerror("Select Algorithm First!", "Click on Select Algorithm button before submitting.")
        return
    show_output(algorithm, output)
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
    b3 = tk.Button(second, text="Submit", height=2, command=lambda:goto_submission(second, queue))
    b1.grid(row=2, column=0, padx=50, pady=50, sticky=tk.NSEW)
    b2.grid(row=2, column=1, padx=50, pady=50, sticky=tk.NSEW)
    b3.grid(row=2, column=2, padx=50, pady=50, sticky=tk.NSEW)

def goto_main(second):
    root.deiconify()
    second.withdraw()

def goto_submission(second, queue):
    global submit
    global extra
    submit = None
    extra = None
    third = tk.Toplevel()
    second.withdraw()
    third.geometry(size)
    ids = [pri[0] for pri in queue]
    ids_stat = tk.Label(third, text=f"Process IDs: {ids}", relief=tk.SUNKEN, bd=2)
    sl = tk.Scale(third, from_=1, to=7, orient=tk.HORIZONTAL)
    pr = [process[0] for process in queue]
    pr_pris = [0 for i in pr]
    pr_idx = [0 for i in pr]    
    pr_title = tk.Label(third, text="Process ID:")
    pris_title = tk.Label(third, text="Priorities:")
    time_quantum = tk.Label(third, text="Time Quantum")
    feedback_label = tk.Label(third, text="Threshold (integer in range 1-5):")
    feedback_threshold = tk.Entry(third)
    for i in range(len(pr)):
        pr_idx[i] = tk.Label(third, text=pr[i])
        pr_pris[i] = tk.Entry(third)

    
        

    def select_algo(algorithm):
        global submit
        global extra
        extra = None
        lab.config(text=op.get())
        submit = algorithm
    lab = tk.Label(third)
    modes = [
        ("First Come First Serve"),
        ("Shortest Job First"),
        ("Round Robin"),
        ("Multi Level Queue"),
    ]
    op = tk.StringVar()
    option = tk.OptionMenu(third, op, *modes)
    b = tk.Button(third, text="Select Algorithm", height=2, width=30, command=lambda: select_algo(op.get()))
    b1 = tk.Button(third, text="Go to Main", height=2, width=30, command=lambda:goto_main(third))
    b2 = tk.Button(third, text="Submit for Processing", height=2, width=30, command=lambda:algo(submit, queue))
    option.config(height=1, width=40)
    option.grid(row=1, column=1, padx=60, pady=40)
    b.grid(row=2, column=1, padx=60, pady=30, sticky=tk.NSEW)
    b1.grid(row=2, column=0, padx=60, pady=30, sticky=tk.NSEW)
    b2.grid(row=2, column=2, padx=60, pady=30, sticky=tk.NSEW)
    lab.grid(row=3, column=1)
    ids_stat.grid(row=0, column=0, columnspan=3, padx=90, sticky=tk.W+tk.E)

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
