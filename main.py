import tkinter as tk
from tkinter import messagebox

class ToDoListManager:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Manager")
        self.root.geometry("500x450+750+250")
        self.root.resizable(0, 0)
        self.root.configure(bg="#FAEBD7")

        # Create a frame for the header
        self.header_frame = tk.Frame(self.root, bg="#FAEBD7")
        self.header_frame.pack(fill="both")

        # Create a label for the header
        self.header_label = tk.Label(
            self.header_frame,
            text="The To-Do List",
            font=("Arial", 24, "bold"),  # Change font to Arial, size 24, bold
            fg="#008000",  # Change text color to green
            bg="#FAEBD7",  # Change background color to light gray
            justify="center"  # Center the text
        )
        self.header_label.pack(padx=20, pady=20)

        # Create a frame for the task entry
        self.task_frame = tk.Frame(self.root, bg="#FAEBD7")
        self.task_frame.pack(fill="both")

        # Create a label for the task entry
        self.task_label = tk.Label(
            self.task_frame,
            text="Enter the Task:",
            font=("Helvetica", 14),  # Change font to Helvetica, size 14
            fg="#0000FF",  # Change text color to blue
            bg="#FAEBD7",  # Change background color to light gray
            anchor="w"  # Left-align the text
        )
        self.task_label.pack(padx=10, pady=10)

        # Create an entry field for the task
        self.task_field = tk.Entry(
            self.task_frame,
            font=("Courier", 12),  # Change font to Courier, size 12
            fg="#FF0000",  # Change text color to red
            bg="#FFFFFF",  # Change background color to white
            width=30
        )
        self.task_field.pack(padx=10, pady=10)

        # Create a list box for the tasks
        self.task_listbox = tk.Listbox(
            self.root,
            font=("Times New Roman", 12),  # Change font to Times New Roman, size 12
            fg="#000000",  # Change text color to black
            bg="#FFFFFF",  # Change background color to white
            width=30,
            height=10
        )
        self.task_listbox.pack(padx=10, pady=10)

        # Create a frame for the buttons
        self.button_frame = tk.Frame(self.root, bg="#FAEBD7")
        self.button_frame.pack(fill="both")

        # Create a button for adding the task
        self.add_button = tk.Button(
            self.button_frame,
            text="Add Task",
            font=("Arial", 12),  # Change font to Arial, size 12
            fg="#008000",  # Change text color to green
            bg="#FAEBD7",  # Change background color to light gray
            command=self.add_task
        )
        self.add_button.pack(side="left", padx=10, pady=10)

        # Create a button for deleting the task
        self.delete_button = tk.Button(
            self.button_frame,
            text="Delete Task",
            font=("Arial", 12),  # Change font to Arial, size 12
            fg="#FF0000",  # Change text color to red
            bg="#FAEBD7",  # Change background color to light gray
            command=self.delete_task
        )
        self.delete_button.pack(side="left", padx=10, pady=10)

        # Create a button for updating the task
        self.update_button = tk.Button(
            self.button_frame,
            text="Update Task",
            font=("Arial", 12),  # Change font to Arial, size 12
            fg="#0000FF",  # Change text color to blue
            bg="#FAEBD7",  # Change background color to light gray
            command=self.update_task
        )
        self.update_button.pack(side="left", padx=10, pady=10)

        # Create a button for deleting all tasks
        self.delete_all_button = tk.Button(
            self.button_frame,
            text="Delete All",
            font=("Arial", 12),  # Change font to Arial, size 12
            fg="#FF0000",  # Change text color to red
            bg="#FAEBD7",  # Change background color to light gray
            command=self.delete_all_tasks
        )
        self.delete_all_button.pack(side="left", padx=10, pady=10)

        # Initialize the tasks list
        self.tasks = []

    def add_task(self):
        task_string = self.task_field.get()
        if len(task_string) == 0:
            messagebox.showinfo('Error', 'Field is Empty.')
        else:
            self.tasks.append(task_string)
            self.list_update()
            self.task_field.delete(0, 'end')

    def delete_task(self):
        try:
            task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(task_index)
            self.tasks.pop(task_index)
        except:
            messagebox.showinfo('Error', 'Select a task to delete.')

    def update_task(self):
        try:
            task_index = self.task_listbox.curselection()[0]
            task_string = self.task_field.get()
            if len(task_string) == 0:
                messagebox.showinfo('Error', 'Field is Empty.')
            else:
                self.tasks[task_index] = task_string
                self.list_update()
                self.task_field.delete(0, 'end')
        except:
            messagebox.showinfo('Error', 'Select a task to update.')

    def delete_all_tasks(self):
        self.task_listbox.delete(0, 'end')
        self.tasks = []

    def list_update(self):
        self.task_listbox.delete(0, 'end')
        for task in self.tasks:
            self.task_listbox.insert('end', task)


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListManager(root)
    root.mainloop()