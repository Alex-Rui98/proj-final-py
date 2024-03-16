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

        # Configuration of the ID field 
        self.ID_lbl = Label(self.login_window, text="ID", font="Arial 20 bold",bg="#f0f0f0")
        self.ID_lbl.grid(row=1, column=0, sticky="e", pady=20)
        self.ID_entry = Entry(self.login_window, font="Arial 14 bold", bg="#f0f0f0")
        self.ID_entry.grid(row=1, column=1, pady=10)

        # Configuration of the password field 
        self.password_lbl = Label(self.login_window, text="ID", font="Arial 20 bold",bg="#f0f0f0")
        self.password_lbl.grid(row=2, column=0, sticky="e", pady=20)
        self.password_entry = Entry(self.login_window, font="Arial 14 bold", bg="#f0f0f0")
        self.password_entry.grid(row=2, column=1, pady=10)

        # Configuration of the register button
        self.login_btn = Button(self.login_window, text="Register", font="Arial 14", command=self.user_login) 
        self.login_btn.grid(row=6, column=0, columnspan=2, padx=20, pady=10, sticky="SEW")

        # Exit button
        self.exit_btn = Button(self.login_window, text="Exit", font="Arial 14",
        command=self.login_window.destroy)
        self.exit_btn.grid(row=6, column=1, columnspan=2, padx=20, pady=10, sticky="SEW")

    def user_login(self):
        id_input = self.ID_entry.get()
        pass_input = self.password_entry.get()

    conn= sqlite3.connect("func.db")

    cur = conn.cursor()

    id_check = cur.execute("SELECT ID FROM funcionario")
    id_check.fetchone("ID", user_login.id_input) #need help with these arguments
    pass_check = cur.execute("SELECT password FROM funcionario")
    pass_check.fetchone()#need help with these arguments