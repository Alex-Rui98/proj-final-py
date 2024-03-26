from tkinter import *
from tkinter import Tk, messagebox
import sqlite3
import hashlib
import os
from classes.window.window_logged import Admin
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import tkcalendar as tkc

class RegisterWindow:
    def __init__(self):

        # create main window
        self.register_window = ctk.CTkToplevel()
        self.register_window.title("User Registration")
        self.register_window.configure(fg_color="#EDF6F9")
        self.register_window.frame
        # change registry window focus
        self.register_window.attributes('-topmost', True)
        self.register_window.focus_force()
    

        #Icon
        self.register_window.after(201, lambda :self.register_window.iconbitmap('assets\\clock_icon.ico'))

        # store font
        font_normal_bold = ctk.CTkFont(family="Arial", size=14, weight="bold")

        # create label for registry
        self.register_lbl = ctk.CTkLabel(self.register_window, text="Registration", font=font_normal_bold, text_color="#006D77", bg_color="#EDF6F9")
        self.register_lbl.grid(row=0, column=0, columnspan=2, pady=20, sticky="N")
        

        # field config
        
        self.first_name_lbl = ctk.CTkLabel(self.register_window, text="First Name", font=font_normal_bold, text_color="#006D77", bg_color="#EDF6F9")
        self.first_name_lbl.grid(row=1, column=0, sticky="E", pady=10)
        self.first_name_entry = ctk.CTkEntry(self.register_window, font=font_normal_bold, text_color="#006D77", bg_color="#EDF6F9")
        self.first_name_entry.grid(row=1, column=1, pady=10, sticky="EW")

        
        self.last_name_lbl = ctk.CTkLabel(self.register_window, text="Last Name", font=font_normal_bold, text_color="#006D77", bg_color="#EDF6F9")
        self.last_name_lbl.grid(row=2, column=0, sticky="E", pady=10)
        self.last_name_entry = ctk.CTkEntry(self.register_window, font=font_normal_bold, text_color="#006D77", bg_color="#EDF6F9")
        self.last_name_entry.grid(row=2, column=1, pady=10, sticky="EW")

        
        self.nationality_lbl = ctk.CTkLabel(self.register_window, text="Nationality", font=font_normal_bold, text_color="#006D77", bg_color="#EDF6F9")
        self.nationality_lbl.grid(row=3, column=0, sticky="E", pady=10)
        self.nationality_entry = ctk.CTkEntry(self.register_window, font=font_normal_bold, text_color="#006D77", bg_color="#EDF6F9")
        self.nationality_entry.grid(row=3, column=1, pady=10, sticky="EW")

        
        self.password_lbl = ctk.CTkLabel(self.register_window, text="Password", font=font_normal_bold, text_color="#006D77", bg_color="#EDF6F9")
        self.password_lbl.grid(row=4, column=0, sticky="E", pady=10)
        self.password_entry = ctk.CTkEntry(self.register_window, font=font_normal_bold, text_color="#006D77", bg_color="#EDF6F9", show="*")
        self.password_entry.grid(row=4, column=1, pady=10, sticky="EW")

        
        self.card_id_lbl = ctk.CTkLabel(self.register_window, text="Doc. Num.", font=font_normal_bold, text_color="#006D77", bg_color="#EDF6F9")
        self.card_id_lbl.grid(row=5, column=0, sticky="E", pady=10)
        self.card_id_entry = ctk.CTkEntry(self.register_window, font=font_normal_bold, text_color="#006D77", bg_color="#EDF6F9")
        self.card_id_entry.grid(row=5, column=1, pady=10, sticky="EW")

        
        self.nib_lbl = ctk.CTkLabel(self.register_window, text="NIB", font=font_normal_bold, text_color="#006D77", bg_color="#EDF6F9")
        self.nib_lbl.grid(row=6, column=0, sticky="E", pady=10)
        self.nib_entry = ctk.CTkEntry(self.register_window, font=font_normal_bold, text_color="#006D77", bg_color="#EDF6F9")
        self.nib_entry.grid(row=6, column=1, pady=10, sticky="EW")

        
        self.academics_lbl = ctk.CTkLabel(self.register_window, text="Level of Education", font=font_normal_bold, text_color="#006D77", bg_color="#EDF6F9")
        self.academics_lbl.grid(row=7, column=0, sticky="E", pady=10)
        self.academics_entry = ctk.CTkOptionMenu(self.register_window, fg_color="White", dynamic_resizing=False, font=font_normal_bold, text_color="#006D77", values=["Illiterate", "Incomplete Basic Education", "Basic Education", "Middle School", "High School", "Bachelor", "Master", "Doctorate"])
        self.academics_entry.grid(row=7, column=1, pady=10, sticky="EW")

        
        self.data_nascm_label = ctk.CTkLabel(self.register_window, text="Date of Birth", font=font_normal_bold, text_color="#006D77", bg_color="#EDF6F9")
        self.data_nascm_label.grid(row=8, column=0, sticky="E", pady=10)
        self.data_nascm_entry = tkc.DateEntry(self.register_window, font=font_normal_bold, text_color="#006D77", bg_color="#EDF6F9", max_width=50, date_pattern='dd-mm-yyyy')
        self.data_nascm_entry.grid(row=8, column=1, pady=10, sticky="EW")

        #confirm registry button
        self.register_btn = ctk.CTkButton(self.register_window, text="Register", font=font_normal_bold, command=self.register_user, fg_color="#006D77")
        self.register_btn.grid(row=9, column=0, columnspan=2, padx=20, pady=10, sticky="SEW")

        # exit button
        self.exit_btn = ctk.CTkButton(self.register_window, text="Exit", font=font_normal_bold, command=self.register_window.destroy, fg_color="#006D77")
        self.exit_btn.grid(row=10, column=0, columnspan=2, padx=20, pady=10, sticky="SEW")

        self.register_window.resizable(False,False)
    def register_user(self):
        # obtain user's entries
        first_name = self.first_name_entry.get().capitalize()
        last_name = self.last_name_entry.get().capitalize()
        cc = self.card_id_entry.get()
        nib = self.nib_entry.get()
        academics = self.academics_entry.get()
        password = self.password_entry.get()
        data_nasc = self.data_nascm_entry.get()
        nacionalidade = self.nationality_entry.get().capitalize()

        # validate entries
        if not first_name or not last_name or not nib or not academics or not password:
            messagebox.showerror("Error", "Not enough credentials")
            return

        # generate salt
        salt = os.urandom(16)

        # generate hash sha-256
        password_hash = hashlib.pbkdf2_hmac('sha256', password.encode('UTF-8'), salt, 100000)

        # convert salt and hash to hex
        salt_hex = salt.hex()
        password_hash_hex = password_hash.hex()

        # value to be stored
        password_to_store = f'{salt_hex}:{password_hash_hex}'

        # connect to data base
        conn = sqlite3.connect('func.db')
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO employee (first_name, last_name, nib, level_education, password, date_birth, nationality, document_number, perms) VALUES (?, ?,?,?,?,?,?,?,?)", (first_name, last_name,nib,academics, password_to_store,data_nasc,nacionalidade,cc, "employee"))
        
        conn.commit()
        conn.close()

        # sucessful registration message
        self.registration_success_message = CTkMessagebox(message="Registration was succesful!",
                  icon="check", option_1="Thanks")
        self.registration_success_message.grid()
        self.registration_success_message.after(3000, self.register_window.destroy)


