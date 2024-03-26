import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from classes.window.window_search import MySearch
from classes.window.window_attendance import Attendance
import datetime
import sqlite3
from newspaper import Article


class Admin():

    def __init__(self, id, primeiro_nome, ultimo_nome, cargo):
        # Create the main window
        self.logged_window = ctk.CTk()
        self.logged_window.title("Employee Management")
        self.logged_window.configure(fg_color="#EDF6F9")
        
        #font
        self.logged_window.after(201, lambda :self.logged_window.iconbitmap('assets\\clock_icon.ico'))

        #guardar ID numa variável
        self.id_entry = id

        # Guardar a font
        self.font_normal_bold = ctk.CTkFont(family="Arial", size=14, weight="bold")
        self.font_normal = ctk.CTkFont(family="Arial", size=14, weight="normal")
        self.font_grande = ctk.CTkFont(family="Arial", size=20, weight="bold")

        # Frames
        self.top_frame = ctk.CTkFrame(self.logged_window)
        self.top_frame.configure(fg_color="#EDF6F9")
        self.top_frame.pack(pady=20, padx=10)

        self.clock_frame = ctk.CTkFrame(self.logged_window)
        self.clock_frame.configure(fg_color="#EDF6F9")
        self.clock_frame.pack(pady=20, padx=10)

        self.input_frame = ctk.CTkFrame(self.logged_window, fg_color="#EDF6F9")
        self.input_frame.pack(pady=20, padx=10)

        self.button_frame = ctk.CTkFrame(self.logged_window, fg_color="#EDF6F9")
        self.button_frame.pack(pady=20, padx=10)
        

        self.welcome_lbl = ctk.CTkLabel(self.top_frame, text=f"{primeiro_nome} {ultimo_nome}", font=self.font_grande, text_color="#006D77", bg_color="#EDF6F9")
        self.welcome_lbl.grid(row=0, column=0,padx=20, pady=0)

        self.welcome_lbl = ctk.CTkLabel(self.top_frame, text=cargo.capitalize(), font=self.font_normal, text_color="#006D77", bg_color="#EDF6F9")
        self.welcome_lbl.grid(row=1, column=0,padx=20, pady=0)


       # self.logged_window.mainloop()
        self.clock_state = "clockin"
        if cargo == "administrador":
            self.search = ctk.CTkButton(self.button_frame, text='Pesquisa', font=self.font_normal_bold,text_color="#EDF6F9", command=lambda: self.open_search(), fg_color='#006D77')
            self.search.grid(row=0, column=0, padx=20, pady=10)
            self.attendance = ctk.CTkButton(self.button_frame, text='Faltas', font=self.font_normal_bold,text_color="#EDF6F9", command=lambda: self.open_absence(), fg_color='#006D77')
            self.attendance.grid(row=2, column=0, padx=20, pady=10)
        
        self.clock_btn_in = ctk.CTkButton(self.button_frame, text='CLOCK IN', font=self.font_normal_bold,text_color="#EDF6F9", command=self.toggle_button, fg_color='#8ac926')
        self.clock_btn_in.grid(row=3, column=0, padx=20, pady=10)

        self.clock_btn_out = ctk.CTkButton(self.button_frame, text='CLOCK OUT', font=self.font_normal_bold,text_color="#EDF6F9", command=self.toggle_button, fg_color='#ff595e')
        self.clock_btn_out.grid(row=3, column=0, padx=20, pady=10)
        self.clock_btn_out.grid_remove()

        self.time_lbl = ctk.CTkLabel(self.clock_frame,text="Hora atual: ", font=self.font_normal, text_color="#006D77", bg_color="#EDF6F9")
        self.time_lbl.grid(row=9, column=0,padx=0, pady=0)
        self.clock_lbl = ctk.CTkLabel(self.clock_frame, font=self.font_grande, text_color="#006D77", bg_color="#EDF6F9")
        self.clock_lbl.grid(row=10, column=0,padx=20, pady=0)


        self.news_url= ('https://www.nytimes.com/interactive/2024/science/total-solar-eclipse-maps-path.html')
        self.news_article = Article(self.news_url, language= 'en')
        self.news_article.download()
        self.news_article.parse()
        self.news_text = self.news_article.text
        print(self.news_text)
        
        self.news_text_box = ctk.CTkTextbox(self.clock_frame, font=self.font_normal, text_color="#006D77", bg_color="#EDF6F9")
        self.news_text_box.grid(row=8, column=0, padx=0, pady=0)
        self.news_text_box.insert(1.0 , self.news_text)



        self.update_clock()

    def update_clock(self):
        RTC = datetime.datetime.now()
        self.clock_lbl.configure(text=f"{str(RTC.hour)} : {str(RTC.minute)} : {str(RTC.second)}")
        self.logged_window.after(1000, self.update_clock)
    def open_search(self):
        MySearch()
    def open_absence(self):
        Attendance()
    def toggle_button(self):
        if self.clock_state == 'clockin':
            self.register_clock()
            self.clock_btn_in.grid_remove()
            self.clock_btn_out.grid(row=3, column=0, padx=20, pady=10)
            self.clock_state = 'clockout'
            self.registration_success_message = CTkMessagebox(message="Clock in efetuado com sucesso!",
                  icon="check", option_1="Thanks")
            
        else:
            self.register_clock_out()
            self.clock_btn_out.grid_remove()
            self.clock_btn_in.grid(row=3, column=0, padx=20, pady=10)
            self.clock_state = 'clockin'
            self.registration_success_message = CTkMessagebox(message="Clock out efetuado com sucesso!",
                  icon="check", option_1="Thanks")

    

    def format_current_day(self):
        current_day = datetime.datetime.now().strftime("%Y-%m-%d") 
        return current_day
        
    def format_current_hour(self):
        current_hour = datetime.datetime.now().strftime("%H:%M")
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

