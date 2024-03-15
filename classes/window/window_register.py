from tkinter import *
from tkinter import Tk
import sqlite3
import hashlib
import os

# Create class for the registration window
class RegisterWindow:
    def __init__(self):

        # Create the main window
        self.register_window = Toplevel()
        self.register_window.title("User Registration")
        self.register_window.iconbitmap('assets/icon/icon.ico') # Change favicon
        self.register_window.configure(bg="#f0f0f0") # Change background color  

        # Create registration label 
        self.register_lbl = Label(self.register_window, text="Registration", font="Arial 20", fg="#333333", bg="#f0f0f0")
        self.register_lbl.grid(row=0, column=0, columnspan=2, pady=20, sticky="NSEW") 

        # Configuration of the username field    
        self.username_lbl = Label(self.register_window, text="Username", font="Arial 20 bold",bg="#f0f0f0")
        self.username_lbl.grid(row=1, column=0, sticky="e", pady=20)
        self.username_entry = Entry(self.register_window, font="Arial 14 bold", bg="#f0f0f0")
        self.username_entry.grid(row=1, column=1, pady=10)        

        # Configuration of the password field 
        self.password_lbl = Label(self.register_window, text="Password", font="Arial 20 bold",bg="#f0f0f0")
        self.password_lbl.grid(row=2, column=0, sticky="e", pady=20)
        self.password_entry = Entry(self.register_window, font="Arial 14 bold", bg="#f0f0f0", show="*")
        self.password_entry.grid(row=2, column=1, pady=10)     

        # Configuration of the register button
        self.register_btn = Button(self.register_window, text="Register", font="Arial 14", command=self.register_user) 
        self.register_btn.grid(row=4, column=0, columnspan=2, padx=20, pady=10, sticky="NSEW")

        # Exit button
        self.exit_btn = Button(self.register_window, text="Exit", font="Arial 14",
         command=self.register_window.destroy)
        self.exit_btn.grid(row=5, column=0, columnspan=2, padx=20, pady=10, sticky="NSEW")
        
    def register_user(self):
        # Get user input data
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Generate salt value
        salt = os.urandom(16)

        # Generate sha-256 hash
        password_hash = hashlib.pbkdf2_hmac('sha256', password.encode('UTF-8'), salt, 100000)

        # Convert salt and password hash to hexadecimal
        salt_hex = salt.hex()
        password_hash_hex = password_hash.hex()

        # Value to be stored
        password_to_store = f'{salt_hex}:{password_hash_hex}'

        # Connect to the database
        conn = sqlite3.connect('stock.db')
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)", (username, password_to_store)
        )

        conn.commit()
        conn.close()

        # Registration success message
        self.registration_success_message = Label(self.register_window, text="Registration successful", fg="green")
        self.registration_success_message.grid(row=3, column=0, columnspan=2)
        self.registration_success_message.after(3000, self.register_window.destroy)

# Example usage:
# root = Tk()
# app = RegisterWindow()
# root.mainloop()
