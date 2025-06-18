# TASK 1 - TO-DO LIST
import tkinter as tk
from tkinter import messagebox
import os

TASKS_FILE = "To-do_Tasks.txt"

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📝 My To-Do List")
        self.root.geometry("500x520")
        self.root.configure(bg="#e3f2fd")

        self.tasks = []

        tk.Label(root, text="✨ To-Do Task Manager ✨", font=("Helvetica", 18, "bold"), bg="#e3f2fd", fg="#0d47a1").pack(pady=10)

        self.entry = tk.Entry(root, font=("Helvetica", 14), width=30)
        self.entry.pack(pady=10)

        tk.Button(root, text="➕ Add Task", width=20, bg="#64dd17", fg="white", font=("Helvetica", 12), command=self.add_task).pack()

        self.listbox = tk.Listbox(root, font=("Helvetica", 12), width=45, height=12, bg="#ffffff", fg="#000000", selectmode=tk.SINGLE)
        self.listbox.pack(pady=10)

        button_frame = tk.Frame(root, bg="#e3f2fd")
        button_frame.pack(pady=5)

        tk.Button(button_frame, text="✔ Mark Done", bg="#039be5", fg="white", width=15, command=self.mark_done).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="🗑 Delete Task", bg="#e53935", fg="white", width=15, command=self.delete_task).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="💾 Save & Exit", bg="#6a1b9a", fg="white", width=15, command=self.save_and_exit).grid(row=0, column=2, padx=5)

        self.load_tasks()

    def add_task(self):
        task = self.entry.get().strip()
        if task:
            self.tasks.append({"task": task, "done": False})
            self.entry.delete(0, tk.END)
            self.update_listbox()
        else:
            messagebox.showwarning("Input Error", "Task cannot be empty!")

    def mark_done(self):
        selected = self.listbox.curselection()
        if selected:
            idx = selected[0]
            self.tasks[idx]["done"] = not self.tasks[idx]["done"]
            self.update_listbox()
        else:
            messagebox.showinfo("No Task Selected", "Select a task to mark as done.")

    def delete_task(self):
        selected = self.listbox.curselection()
        if selected:
            idx = selected[0]
            confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this task?")
            if confirm:
                self.tasks.pop(idx)
                self.update_listbox()
        else:
            messagebox.showinfo("No Task Selected", "Select a task to delete.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✅" if task["done"] else "⬜"
            self.listbox.insert(tk.END, f"{status} {task['task']}")

    def save_and_exit(self):
        with open(TASKS_FILE, "w") as f:
            for task in self.tasks:
                status = "1" if task["done"] else "0"
                f.write(f"{task['task']}|{status}\n")
        self.root.destroy()

    def load_tasks(self):
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, "r") as f:
                for line in f:
                    if "|" in line:
                        task_text, done_flag = line.strip().split("|")
                        self.tasks.append({"task": task_text, "done": done_flag == "1"})
        self.update_listbox()


# ---------------- RUN APP ----------------
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()