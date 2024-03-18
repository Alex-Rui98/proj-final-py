import sqlite3
from tkinter import messagebox
import hashlib

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

            # Hash the entered password with the stored salt using PBKDF2 with SHA-256
            hashed_password = hashlib.pbkdf2_hmac('sha256', password_entry.encode('utf-8'), stored_salt, 100000).hex()

            # Comparação da password introduzida com a da db
            if hashed_password == stored_password_hash_hex:
                messagebox.showinfo("Login was Successful")
                return True
            else:
                messagebox.showerror("Login Failed", "Credentials are invalid.")
                return False
        else:
            messagebox.showerror("Login Failed", "User not found.")
            return False
