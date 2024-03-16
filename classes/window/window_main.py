#imports
from tkinter import *
from tkinter import Tk
from classes.window.window_register import RegisterWindow
from classes.window.window_login import LoginWindow
 
#Main window class:
class MainWindow:
    def __init__(self):
 
        #Create the main window
        self.main_window = Tk()
        self.main_window.title("Employee Management") #change title
        #self.main_window.iconbitmap('assets/icon/icon.ico') #change favicon
        self.main_window.configure(bg="#f0f0f0")
 
        #Welcome text configuration
        self.welcome_lbl = Label(self.main_window, text='Employee Management',
        font="Arial 20", bg = "#f0f0f0")
        self.welcome_lbl.grid(row=0, column=1, columnspan=1, pady=20)
 
        #Register button configuration
        self.register_btn = Button(self.main_window, text='Register', font="Arial 14", command=self.open_register_window)
        self.register_btn.grid(row=1, column=1, columnspan=2, padx=20, pady=10, sticky="NSEW")
 
        #Login button configuration
        self.login_btn = Button(self.main_window, text='Login', font="Arial 14", command=self.open_login_window)
        self.login_btn.grid(row=2, column=1, columnspan=2, padx=20, pady=10, sticky="NSEW")
 
        #Exit button configuration
        self.exit_btn = Button(self.main_window, text='Exit', font="Arial 14", command=self.main_window.destroy)
        self.exit_btn.grid(row=3, column=1, columnspan=2, padx=20, pady=10, sticky="NSEW")
 
    def open_register_window(self):
        RegisterWindow()
 
    def open_login_window(self):
        LoginWindow()
