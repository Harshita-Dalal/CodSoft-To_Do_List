# # importing the required modules
# import tkinter as tk  # importing the tkinter module as tk
# from tkinter import ttk  # importing the ttk module from the tkinter library
# from tkinter import messagebox  # importing the messagebox module from the tkinter library
# import sqlite3 as sql  # importing the sqlite3 module as sql
#
#
# # defining the function to add tasks to the list
# def add_task():
#     # getting the string from the entry field
#     task_string = task_field.get()
#     # checking whether the string is empty or not
#     if len(task_string) == 0:
#         # displaying a message box with 'Empty Field' message
#         messagebox.showinfo('Error', 'Field is Empty.')
#     else:
#         # adding the string to the tasks list
#         tasks.append(task_string)
#         # using the execute() method to execute a SQL statement
#         the_cursor.execute('insert into tasks values (?)', (task_string,))
#         # calling the function to update the list
#         list_update()
#         # deleting the entry in the entry field
#         task_field.delete(0, 'end')
#
#     # defining the function to update the list
#
#
# def list_update():
#     # calling the function to clear the list
#     clear_list()
#     # iterating through the strings in the list
#     for task in tasks:
#         # using the insert() method to insert the tasks in the list box
#         task_listbox.insert('end', task)
#
#     # defining the function to delete a task from the list
#
#
# def delete_task():
#     # using the try-except method
#     try:
#         # getting the selected entry from the list box
#         the_value = task_listbox.get(task_listbox.curselection())
#         # checking if the stored value is present in the tasks list
#         if the_value in tasks:
#             # removing the task from the list
#             tasks.remove(the_value)
#             # calling the function to update the list
#             list_update()
#             # using the execute() method to execute a SQL statement
#             the_cursor.execute('delete from tasks where title = ?', (the_value,))
#     except:
#         # displaying the message box with 'No Item Selected' message for an exception
#         messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')
#
#     # function to delete all tasks from the list
#
#
# def delete_all_tasks():
#     # displaying a message box to ask user for confirmation
#     message_box = messagebox.askyesno('Delete All', 'Are you sure?')
#     # if the value turns to be True
#     if message_box == True:
#         # using while loop to iterate through the tasks list until it's empty
#         while (len(tasks) != 0):
#             # using the pop() method to pop out the elements from the list
#             tasks.pop()
#             # using the execute() method to execute a SQL statement
#         the_cursor.execute('delete from tasks')
#         # calling the function to update the list
#         list_update()
#
#     # function to clear the list
#
#
# def clear_list():
#     # using the delete method to delete all entries from the list box
#     task_listbox.delete(0, 'end')
#
#
# # function to close the application
# def close():
#     # printing the elements from the tasks list
#     print(tasks)
#     # using the destroy() method to close the application
#     guiWindow.destroy()
#
#
# # function to retrieve data from the database
# def retrieve_database():
#     # using the while loop to iterate through the elements in the tasks list
#     while (len(tasks) != 0):
#         # using the pop() method to pop out the elements from the list
#         tasks.pop()
#         # iterating through the rows in the database table
#     for row in the_cursor.execute('select title from tasks'):
#         # using the append() method to insert the titles from the table in the list
#         tasks.append(row[0])
#
#     # main function
#
#
# if __name__ == "__main__":
#     # creating an object of the Tk() class
#     guiWindow = tk.Tk()
#     # setting the title of the window
#     guiWindow.title("To-Do List Manager - JAVATPOINT")
#     # setting the geometry of the window
#     guiWindow.geometry("500x450+750+250")
#     # disabling the resizable option
#     guiWindow.resizable(0, 0)
#     # setting the background color to #FAEBD7
#     guiWindow.configure(bg="#FAEBD7")
#
#     # using the connect() method to connect to the database
#     the_connection = sql.connect('listOfTasks.db')
#     # creating the cursor object of the cursor class
#     the_cursor = the_connection.cursor()
#     # using the execute() method to execute a SQL statement
#     the_cursor.execute('create table if not exists tasks (title text)')
#
#     # defining an empty list
#     tasks = []
#
#     # defining frames using the tk.Frame() widget
#     header_frame = tk.Frame(guiWindow, bg="#FAEBD7")
#     functions_frame = tk.Frame(guiWindow, bg="#FAEBD7")
#     listbox_frame = tk.Frame(guiWindow, bg="#FAEBD7")
#
#     # using the pack() method to place the frames in the application
#     header_frame.pack(fill="both")
#     functions_frame.pack(side="left", expand=True, fill="both")
#     listbox_frame.pack(side="right", expand=True, fill="both")
#
#     # defining a label using the ttk.Label() widget
#     header_label = ttk.Label(
#         header_frame,
#         text="The To-Do List",
#         font=("Brush Script MT", "30"),
#         background="#FAEBD7",
#         foreground="#8B4513"
#     )
#     # using the pack() method to place the label in the application
#     header_label.pack(padx=20, pady=20)
#
#     # defining another label using the ttk.Label() widget
#     task_label = ttk.Label(
#         functions_frame,
#         text="Enter the Task:",
#         font=("Consolas", "11", "bold"),
#         background="#FAEBD7",
#         foreground="#000000"
#     )
#     # using the place() method to place the label in the application
#     task_label.place(x=30, y=40)
#
#     # defining an entry field using the ttk.Entry() widget
#     task_field = ttk.Entry(
#         functions_frame,
#         font=("Consolas", "12"),
#         width=18,
#         background="#FFF8DC",
#         foreground="#A52A2A"
#     )
#     # using the place() method to place the entry field in the application
#     task_field.place(x=30, y=80)
#
#     # adding buttons to the application using the ttk.Button() widget
#     add_button = ttk.Button(
#         functions_frame,
#         text="Add Task",
#         width=24,
#         command=add_task
#     )
#     del_button = ttk.Button(
#         functions_frame,
#         text="Delete Task",
#         width=24,
#         command=delete_task
#     )
#     del_all_button = ttk.Button(
#         functions_frame,
#         text="Delete All Tasks",
#         width=24,
#         command=delete_all_tasks
#     )
#     exit_button = ttk.Button(
#         functions_frame,
#         text="Exit",
#         width=24,
#         command=close
#     )
#     # using the place() method to set the position of the buttons in the application
#     add_button.place(x=30, y=120)
#     del_button.place(x=30, y=160)
#     del_all_button.place(x=30, y=200)
#     exit_button.place(x=30, y=240)
#
#     # defining a list box using the tk.Listbox() widget
#     task_listbox = tk.Listbox(
#         listbox_frame,
#         width=26,
#         height=13,
#         selectmode='SINGLE',
#         background="#FFFFFF",
#         foreground="#000000",
#         selectbackground="#CD853F",
#         selectforeground="#FFFFFF"
#     )
#     # using the place() method to place the list box in the application
#     task_listbox.place(x=10, y=20)
#
#     # calling some functions
#     retrieve_database()
#     list_update()
#     # using the mainloop() method to run the application
#     guiWindow.mainloop()
#     # establishing the connection with database
#     the_connection.commit()
#     the_cursor.close()

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