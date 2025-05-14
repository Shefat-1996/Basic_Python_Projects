import tkinter as tk
from tkinter import messagebox

# File to store tasks
TASK_FILE = "tasks.txt"

# Load existing tasks from file
def load_tasks():
    try:
        with open(TASK_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks():
    with open(TASK_FILE, "w") as file:
        for task in task_listbox.get(0, tk.END):
            file.write(task + "\n")

# Add a task
def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

# Delete the selected task
def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Setup the GUI window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

# Entry box to type new task
task_entry = tk.Entry(root, width=30, font=("Arial", 14))
task_entry.pack(pady=10)

# Button to add task
add_button = tk.Button(root, text="Add Task", width=20, command=add_task)
add_button.pack(pady=5)

# Listbox to display tasks
task_listbox = tk.Listbox(root, width=40, height=10, font=("Arial", 12))
task_listbox.pack(pady=10)

# Button to delete task
delete_button = tk.Button(root, text="Delete Selected Task", width=20, command=delete_task)
delete_button.pack(pady=5)

# Load tasks on start
for task in load_tasks():
    task_listbox.insert(tk.END, task)

# Save tasks on window close
def on_closing():
    save_tasks()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

# Run the app
root.mainloop()