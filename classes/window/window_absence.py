import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import tkcalendar as tkc
import sqlite3

class Absence:
    def __init__(self):
        self.register_window = ctk.CTkToplevel()
        self.register_window.title("Absence")
        self.register_window.configure(fg_color="#EDF6F9")

        # store font
        font_normal_bold = ctk.CTkFont(family="Arial", size=14, weight="bold")

        # config entry ID
        self.id_lbl = ctk.CTkLabel(self.register_window, text="ID", font=font_normal_bold, text_color="#006D77", bg_color="#EDF6F9")
        self.id_lbl.grid(row=0, column=0, sticky="e", pady=10)
        self.id_entry = ctk.CTkEntry(self.register_window, font=font_normal_bold, text_color="#006D77", bg_color="#EDF6F9")
        self.id_entry.grid(row=0, column=1, pady=10, sticky="ew")

        # config entry date
        self.absence_date_label = ctk.CTkLabel(self.register_window, text="worker", font=font_normal_bold, text_color="#006D77", bg_color="#EDF6F9")
        self.absence_date_label.grid(row=1, column=0, sticky="e", pady=10)
        self.absence_date_entry = tkc.DateEntry(self.register_window, font=font_normal_bold, text_color="#006D77", bg_color="#EDF6F9", max_width=50, date_pattern='dd-mm-yyyy')
        self.absence_date_entry.grid(row=1, column=1, pady=10, sticky="ew")

        # config entry first name
        self.desc_lbl = ctk.CTkLabel(self.register_window, text="worker", font=font_normal_bold, text_color="#006D77", bg_color="#EDF6F9")
        self.desc_lbl.grid(row=2, column=0, sticky="e", pady=10)
        self.desc_entry = ctk.CTkEntry(self.register_window, font=font_normal_bold, text_color="#006D77", bg_color="#EDF6F9", height=150, width=150)
        self.desc_entry.grid(row=2, column=1, sticky="e", pady=10)

        # config command button
        self.mark_btn = ctk.CTkButton(self.register_window, text="Mark Absence",command=lambda: self.mark_absence())
        self.mark_btn.grid(row=4, column=0, padx=20, pady=10, sticky="SEW")


    def mark_absence(self):
        # obtaint entry data user
        ID = self.id_entry.get()
        absence_date = self.absence_date_entry.get()
        description = self.desc_entry.get()

        #connect to database+create cursor
        conn = sqlite3.connect('func.db')
        cursor = conn.cursor()

        #execute requested order
        cursor.execute(
            "INSERT INTO attendance (worker, day,description) VALUES (?,?,?)", (ID,absence_date,description) )
        
        conn.commit()

        conn.close()

        # sucessful entry message
        self.registration_success_message = CTkMessagebox(title="",message="Absence marked sucessfully!",
                  icon="check", option_1="Thanks")
        self.registration_success_message.grid()
        self.registration_success_message.after(3000, self.register_window.destroy)

    
