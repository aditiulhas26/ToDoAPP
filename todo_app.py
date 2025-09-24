# todo_app.py - Final Upgraded Version
from tkinter import *
import os

# ------------------------------
# Main window
# ------------------------------
root = Tk()
root.title("To-Do App")
root.geometry("500x500")
root.config(bg="#f0f0f0")  # Light grey background

# ------------------------------
# File to store tasks
# ------------------------------
tasks_file = os.path.join(os.path.dirname(__file__), "tasks.txt")

# ------------------------------
# Task list
# ------------------------------
tasks = []

# ------------------------------
# Load tasks from file
# ------------------------------
def load_tasks():
    if os.path.exists(tasks_file):
        with open(tasks_file, "r") as f:
            for line in f:
                tasks.append(line.strip())

# ------------------------------
# Save tasks to file
# ------------------------------
def save_tasks():
    with open(tasks_file, "w") as f:
        for task in tasks:
            f.write(task + "\n")

# ------------------------------
# Add task
# ------------------------------
def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append(task)
        update_listbox()
        save_tasks()
        task_entry.delete(0, END)

# ------------------------------
# Delete task
# ------------------------------
def delete_task():
    try:
        selected_index = listbox.curselection()[0]
        tasks.pop(selected_index)
        update_listbox()
        save_tasks()
    except IndexError:
        pass

# ------------------------------
# Edit task
# ------------------------------
def edit_task():
    try:
        selected_index = listbox.curselection()[0]
        new_task = task_entry.get()
        if new_task != "":
            tasks[selected_index] = new_task
            update_listbox()
            save_tasks()
            task_entry.delete(0, END)
    except IndexError:
        pass

# ------------------------------
# Update listbox
# ------------------------------
def update_listbox():
    listbox.delete(0, END)
    for task in tasks:
        listbox.insert(END, task)

# ------------------------------
# GUI Elements
# ------------------------------
font_style = ("Arial", 12)

task_entry = Entry(root, width=35, font=font_style)
task_entry.pack(pady=15)

button_frame = Frame(root, bg="#f0f0f0")
button_frame.pack(pady=5)

add_button = Button(button_frame, text="Add Task", width=15, bg="#4CAF50", fg="white", font=font_style, command=add_task)
add_button.grid(row=0, column=0, padx=5)

edit_button = Button(button_frame, text="Edit Task", width=15, bg="#FFC107", fg="black", font=font_style, command=edit_task)
edit_button.grid(row=0, column=1, padx=5)

delete_button = Button(button_frame, text="Delete Task", width=15, bg="#f44336", fg="white", font=font_style, command=delete_task)
delete_button.grid(row=0, column=2, padx=5)

# ------------------------------
# Listbox with Scrollbar
# ------------------------------
listbox_frame = Frame(root)
listbox_frame.pack(pady=15)

scrollbar = Scrollbar(listbox_frame)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(listbox_frame, width=50, height=15, font=font_style, bg="#ffffff", fg="#000000", selectbackground="#2196F3", yscrollcommand=scrollbar.set)
listbox.pack(side=LEFT, fill=BOTH)

scrollbar.config(command=listbox.yview)

# ------------------------------
# Load tasks at startup
# ------------------------------
load_tasks()
update_listbox()

# ------------------------------
# Run GUI loop
# ------------------------------
root.mainloop()