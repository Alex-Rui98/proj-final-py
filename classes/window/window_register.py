from tkinter import *
from tkinter import Tk, messagebox
import sqlite3
import hashlib
import os
from classes.window.window_logged import LoggedWindow
# Create class for the registration window
class RegisterWindow:
    def __init__(self):

        # Create the main window
        self.register_window = Toplevel()
        self.register_window.title("User Registration")
        # self.register_window.iconbitmap('assets/icon/icon.ico') # Change favicon
        self.register_window.configure(bg="#f0f0f0") # Change background color  

        # Create registration label 
        self.register_lbl = Label(self.register_window, text="Registration", font="Arial 20", fg="#333333", bg="#f0f0f0")
        self.register_lbl.grid(row=0, column=0, columnspan=2, pady=20, sticky="NSEW") 

        # Configuration of the first and last name field 
        self.first_name_lbl = Label(self.register_window, text="Primeiro nome", font="Arial 20 bold",bg="#f0f0f0")
        self.first_name_lbl.grid(row=1, column=0, sticky="e", pady=20)
        self.first_name_entry = Entry(self.register_window, font="Arial 14 bold", bg="#f0f0f0")
        self.first_name_entry.grid(row=1, column=1, pady=10)

        # Configuration of the first and last name field 
        self.last_name_lbl = Label(self.register_window, text="Ultimo nome", font="Arial 20 bold",bg="#f0f0f0")
        self.last_name_lbl.grid(row=2, column=0, sticky="e", pady=20)
        self.last_name_entry = Entry(self.register_window, font="Arial 14 bold", bg="#f0f0f0")
        self.last_name_entry.grid(row=2, column=1, pady=10)          

        # Configuration of the password field 
        self.password_lbl = Label(self.register_window, text="Password", font="Arial 20 bold",bg="#f0f0f0")
        self.password_lbl.grid(row=3, column=0, sticky="e", pady=20)
        self.password_entry = Entry(self.register_window, font="Arial 14 bold", bg="#f0f0f0", show="*")
        self.password_entry.grid(row=3, column=1, pady=10)

        

        # Configuration of the card id name field 
        self.card_id_lbl = Label(self.register_window, text="CC", font="Arial 20 bold",bg="#f0f0f0")
        self.card_id_lbl.grid(row=4, column=0, sticky="e", pady=20)
        self.card_id_entry = Entry(self.register_window, font="Arial 14 bold", bg="#f0f0f0")
        self.card_id_entry.grid(row=4, column=1, pady=10)

        # Configuration of nib field 
        self.nib_lbl = Label(self.register_window, text="NIB", font="Arial 20 bold",bg="#f0f0f0")
        self.nib_lbl.grid(row=5, column=0, sticky="e", pady=20)
        self.nib_entry = Entry(self.register_window, font="Arial 14 bold", bg="#f0f0f0")
        self.nib_entry.grid(row=5, column=1, pady=10)

        # Configuration of academics field 
        self.academics_lbl = Label(self.register_window, text="Nivel Escolaridade", font="Arial 20 bold",bg="#f0f0f0")
        self.academics_lbl.grid(row=6, column=0, sticky="e", pady=20)
        self.academics_entry = Entry(self.register_window, font="Arial 14 bold", bg="#f0f0f0")
        self.academics_entry.grid(row=6, column=1, pady=10)                  

        # Configuration of the register button
        self.register_btn = Button(self.register_window, text="Register", font="Arial 14", command=self.register_user) 
        self.register_btn.grid(row=7, column=0, columnspan=2, padx=20, pady=10, sticky="SEW")

        # Exit button
        self.exit_btn = Button(self.register_window, text="Exit", font="Arial 14",
         command=self.register_window.destroy)
        self.exit_btn.grid(row=8, column=0, columnspan=2, padx=20, pady=10, sticky="SEW")
        
    def register_user(self):
        # Get user input data
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        nib = self.nib_entry.get()
        academics = self.academics_entry.get()
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
        conn = sqlite3.connect('func.db')
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO funcionario (primeiro_nome, ultimo_nome,nib,nivel_escolaridade, password) VALUES (?, ?,?,?,?)", (first_name, last_name,nib,academics, password_to_store)
        )
        conn.commit()
        conn.close()

        # Registration success message
        self.registration_success_message = Label(self.register_window, text="Registration successful", fg="green")
        self.registration_success_message.grid(row=3, column=0, columnspan=2)
        self.registration_success_message.after(3000, self.register_window.destroy)


class CheckLogin:
    def __init__(self, id_entry, password_entry):
        self.id_entry = id_entry
        self.password_entry = password_entry
        self.check_credentials(id_entry.get(), password_entry.get())

    def check_credentials(self, id_entry, password_entry):
        # efetua conexão com a db
        conn = sqlite3.connect('func.db')
        cursor = conn.cursor()

        # pedir a tabela da db o id que seja identico ao introduzido
        cursor.execute("SELECT password FROM funcionario WHERE id = ?", (id_entry,))
        result = cursor.fetchone()

        if result:
            stored_password_hash = result[0]
            # dividir a password entre salt e hash visto que já se encontram divididos por ":"
            stored_salt_hex, stored_password_hash_hex = stored_password_hash.split(':')
            # Converter o salt para bytes
            stored_salt = bytes.fromhex(stored_salt_hex)

            # hash a senha inserida com o sal armazenado
            hashed_password = hashlib.pbkdf2_hmac('sha256', password_entry.encode('utf-8'), stored_salt, 100000).hex()

            # Comparação da password introduzida com a da db
            if hashed_password == stored_password_hash_hex:
                messagebox.showinfo("Login status", "Login was Succesful")
                return LoggedWindow(self.id_entry)
                
            else:
                messagebox.showerror("Login status", "Login wasn't Succesful")
                return False
        else:
            messagebox.showerror("User not found.")
            return False

# Example usage:
# root = Tk()
# app = RegisterWindow()
# root.mainloop()
