from tkinter import *
import sqlite3
from datetime import datetime

class SuperAdmin:
    def __init__(self, admin):
        self.admin = admin
        # It's not clear what you're trying to accomplish here
        # You may need to revise this part
    
class RegisterWindowClock(SuperAdmin):
    def __init__(self):
        # Create the main window
        self.register_window_clock = Toplevel()
        self.register_window_clock.title("User Registration")
        # self.register_window_clock.iconbitmap('assets/icon/icon.ico')  # Change favicon
        self.register_window_clock.configure(bg="#f0f0f0")  # Change background color  

        # Configuration of the register button
        self.register_clock_btn = Button(self.register_window_clock, text="Regist Clock", font="Arial 14", command=self.register_clock) 
        self.register_clock_btn.grid(row=4, column=0, columnspan=2, padx=20, pady=10, sticky="NSEW")

    def register_clock(self):
        # You need to implement the registration logic here
        pass

class Funcionario(SuperAdmin):
    def __init__(self, admin, funcionario):
        super().__init__(admin)
        self.funcionario = funcionario
        # It's not clear what you're trying to accomplish here
        # You may need to revise this part

def clock_in():
    current_time = datetime.now()
    return current_time.strftime("%Y-%m-%d %H:%M:%S")

# Example of usage:
print("You clocked in at:", clock_in())
