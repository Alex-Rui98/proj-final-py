import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import tkcalendar as tkc
import sqlite3

class Absence:
    def __init__(self):
        self.absence_window = ctk.CTkToplevel()
        self.absence_window.title("Absence")
        self.absence_window.configure(fg_color="#EDF6F9")

        # store font
        font_normal_bold = ctk.CTkFont(family="Arial", size=14, weight="bold")

        # frame labels and entrys  
        self.absence_window_frame = ctk.CTkFrame(self.absence_window, fg_color="#EDF6F9")
        self.absence_window_frame.pack(pady=20, padx=20, fill="both", expand=True)


        # config entry ID
        self.id_lbl = ctk.CTkLabel(self.absence_window_frame, text="Worker ID: ", font=font_normal_bold, text_color="#006D77", bg_color="#EDF6F9")
        self.id_lbl.grid(row=0, column=0, sticky="nw", pady=10, padx=10)
        self.id_entry = ctk.CTkEntry(self.absence_window_frame, font=font_normal_bold, text_color="#006D77", bg_color="#EDF6F9")
        self.id_entry.grid(row=0, column=1, pady=10, padx=10, sticky="e")

        # config entry date
        self.absence_date_label = ctk.CTkLabel(self.absence_window_frame, text="Date of absence: ", font=font_normal_bold, text_color="#006D77", bg_color="#EDF6F9")
        self.absence_date_label.grid(row=1, column=0, sticky="nw", pady=10, padx=10)
        self.absence_date_entry = tkc.DateEntry(self.absence_window_frame, font=font_normal_bold, text_color="#006D77", bg_color="#EDF6F9", max_width=50, date_pattern='dd-mm-yyyy')
        self.absence_date_entry.grid(row=1, column=1, pady=10,padx=10, sticky="e")

        # config entry first name
        self.desc_lbl = ctk.CTkLabel(self.absence_window_frame, text="Description: ", font=font_normal_bold, text_color="#006D77", bg_color="#EDF6F9")
        self.desc_lbl.grid(row=2, column=0, sticky="nw", pady=10, padx=10)
        self.desc_entry = ctk.CTkEntry(self.absence_window_frame, font=font_normal_bold, text_color="#006D77", bg_color="#EDF6F9", height=150, width=150)
        self.desc_entry.grid(row=2, column=1, padx=10, sticky="e", pady=10)

        # config command button
        self.mark_btn = ctk.CTkButton(self.absence_window_frame, text="Mark Absence",command=lambda: self.mark_absence(), font=font_normal_bold, fg_color='#006D77', text_color="#EDF6F9")
        self.mark_btn.grid(row=3, column=0,columnspan=2, padx=20, pady=10, sticky="SEW")


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

    
