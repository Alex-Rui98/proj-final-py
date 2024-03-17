from tkinter import *
from tkinter import Tk
import sqlite3
import hashlib
import os

class LoginWindow:
    def __init__(self):
        # Create the main window
        self.login_window = Toplevel()
        self.login_window.title("Login")
        # self.ID.iconbitmap('assets/icon/icon.ico') # Change favicon
        self.login_window.configure(bg="#f0f0f0") # Change background color  

        self.ID_lbl = Label(self.login_window, text="ID", font="Arial 20 bold",bg="#f0f0f0")
        self.ID_lbl.grid(row=1, column=0, sticky="e", pady=20)
        self.ID_entry = Entry(self.login_window, font="Arial 14 bold", bg="#f0f0f0")
        self.ID_entry.grid(row=1, column=1, pady=10)

        # Configuration of the password field 
        self.password_lbl = Label(self.login_window, text="ID", font="Arial 20 bold",bg="#f0f0f0")
        self.password_lbl.grid(row=2, column=0, sticky="e", pady=20)
        self.password_entry = Entry(self.login_window, font="Arial 14 bold", bg="#f0f0f0")
        self.password_entry.grid(row=2, column=1, pady=10)

        # Configuration of the login button
        self.login_btn = Button(self.login_window, text="Login", font="Arial 14", command=self.user_login) 
        self.login_btn.grid(row=6, column=0, columnspan=2, padx=20, pady=10, sticky="SEW")

        # Exit button
        self.exit_btn = Button(self.login_window, text="Exit", font="Arial 14",
        command=self.login_window.destroy)
        self.exit_btn.grid(row=6, column=1, columnspan=2, padx=20, pady=10, sticky="SEW")

    
    def login_user(self):    
        id_input = self.ID_entry.get()
        pass_input = self.password_entry.get()

        conn= sqlite3.connect("func.db")

        cur = conn.cursor()

        id_check = cur.execute("SELECT ID FROM funcionario VALUES (?)") (id_input)
        id_check.fetchone() #need help with these arguments
        pass_check = cur.execute("SELECT password FROM funcionario VALUES (?)") (pass_input)
        pass_check.fetchone()#need help with these arguments