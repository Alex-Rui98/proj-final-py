import customtkinter as ctk
from datetime import datetime
import sqlite3


class LoggedWindow:

    def __init__(self, id):

        # Create the main window
        self.logged_window = ctk.CTk()
        self.logged_window.title("Employee Management")
        self.logged_window.configure(fg_color="#EDF6F9")

        #guardar ID numa variável
        self.id_entry = id

        # Guardar a font
        font_normal_bold = ctk.CTkFont(family="Arial", size=14, weight="bold")
        font_normal = ctk.CTkFont(family="Arial", size=14, weight="normal")
        font_grande = ctk.CTkFont(family="Arial", size=20, weight="bold")

        # Create frames for better organization
        self.top_frame = ctk.CTkFrame(self.logged_window)
        self.top_frame.pack(pady=20, padx=10)

        self.input_frame = ctk.CTkFrame(self.logged_window, fg_color="#EDF6F9")
        self.input_frame.pack(pady=20, padx=10)

        self.button_frame = ctk.CTkFrame(self.logged_window, fg_color="#EDF6F9")
        self.button_frame.pack(pady=20, padx=10)

        # Welcome text configuration
        self.welcome_lbl = ctk.CTkLabel(self.top_frame, text='Employee Management', font=font_grande, text_color="#006D77", bg_color="#EDF6F9")

       # self.logged_window.mainloop()
        self.clock_state = "clockin"
        
        self.clock_btn_in = ctk.CTkButton(self.button_frame, text='CLOCK IN', font=font_normal, command=self.toggle_button, fg_color='#006D77')
        self.clock_btn_in.grid(row=0, column=0, padx=20, pady=10)

        self.clock_btn_out = ctk.CTkButton(self.button_frame, text='CLOCK OUT', font=font_normal, command=self.toggle_button, fg_color='#006D77')
        self.clock_btn_out.grid(row=0, column=2, padx=20, pady=10)
        self.clock_btn_out.grid_remove()

    def toggle_button(self):
        if self.clock_state == 'clockin':
            self.register_clock()
            self.clock_btn_in.grid_remove()
            self.clock_btn_out.grid(row=0, column=2, padx=20, pady=10)
            self.clock_state = 'clockout'
            
        else:
            self.register_clock_out()
            self.clock_btn_out.grid_remove()
            self.clock_btn_in.grid(row=0, column=0, padx=20, pady=10)
            self.clock_state = 'clockin'

    

    def format_current_day(self):
        current_day = datetime.now().strftime("%Y-%m-%d") 
        return current_day
        
    def format_current_hour(self):
        current_hour = datetime.now().strftime("%H:%M")
        return current_hour
    
    def register_clock(self):

        conn = sqlite3.connect('func.db')
            
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO clock (worker, clock_in_day, clock_in_hour) VALUES (?,?,?)", ( self.id_entry , self.format_current_day() , self.format_current_hour() )
            )

        conn.commit()

        conn.close()

    
    def register_clock_out(self):

        print(self.id_entry)

        conn = sqlite3.connect('func.db')
            
        cursor = conn.cursor()

        order_out = '''SELECT MAX(ID) from clock WHERE worker = ? LIMIT 1 '''

        clock_out_var = '''UPDATE clock SET clock_out_day = ?, clock_out_hour = ? WHERE ID = ?'''

        cursor.execute(order_out, (self.id_entry,))

        resultado = cursor.fetchone()

        if resultado:
            print(resultado)
            cursor.execute(clock_out_var, (self.format_current_day(), self.format_current_hour(), resultado[0]))

        conn.commit()

        conn.close()



