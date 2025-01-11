
import tkinter as tk
from tkinter import messagebox


def validate_login():
    userid = username_entry.get()
    password = password_entry.get()

    if userid == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome, Admin!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


parent = tk.Tk()
parent.title("Login Form")


username_label = tk.Label(parent, text="Userid:")
username_label.pack()

username_entry = tk.Entry(parent)
username_entry.pack()


password_label = tk.Label(parent, text="Password:")
password_label.pack()

password_entry = tk.Entry(parent, show="*") 
password_entry.pack()

login_button = tk.Button(parent, text="Login", command=validate_login)
login_button.pack()

parent.mainloop()
