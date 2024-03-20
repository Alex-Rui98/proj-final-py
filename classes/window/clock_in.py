from tkinter import *
from tkinter import Toplevel
from datetime import datetime
import sqlite3
import os

class SuperAdmin:
    def __init__(self, admin):
        self.admin = admin

class RegisterWindowClock(SuperAdmin):

    def __init__(self, attendance):

        def __init__(self):

         super().__init__(None)  # No admin provided for now
        
         # Create the main window
         self.register_window_clock = Toplevel()
         self.register_window_clock.title("User Registration")
         self.register_window_clock.configure(bg="#f0f0f0")  # Change background color  

         # Configuration of the register button
         self.register_clock_btn = Button(self.register_window_clock, text="Register Clock", font="Arial 14", command=self.register_clock) 
         self.register_clock_btn.grid(row=4, column=0, columnspan=2, padx=20, pady=10, sticky="NSEW")

         conn = sqlite3.connect('clock.db')
         cursor = conn.cursor()

         cursor.execute(
                "INSERT INTO clock (worker, clock_in) VALUES (?,?)", (worker, clock_in)
        )
         conn.commit()
         conn.close()


    def register_clock(self):
        current_time = clock_in()  # Get current time
        print(f"Clock registered at: {current_time}")  # For demonstration, print the registered time

class Funcionario(SuperAdmin):
    def __init__(self, admin, funcionario):
        super().__init__(admin)
        self.funcionario = funcionario

def clock_in():
    current_time = datetime.now()
    return current_time.strftime("%Y-%m-%d %H:%M:%S")



