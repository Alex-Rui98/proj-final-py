import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from classes.window.window_search import MySearch
from classes.window.window_attendance import Attendance
import datetime
import sqlite3
from newspaper import Article


class Admin():

    def __init__(self, id, first_name, last_name, perms):
        # Create the main window
        self.logged_window = ctk.CTk()
        self.logged_window.title("Employee Management")
        self.logged_window.configure(fg_color="#EDF6F9")
        
        
        #font
        self.logged_window.after(201, lambda :self.logged_window.iconbitmap('assets\\clock_icon.ico'))

        #save ID in variable
        self.id_entry = id

        # store font
        self.font_small = ctk.CTkFont(family="Arial", size=10, weight="normal")
        self.font_normal_bold = ctk.CTkFont(family="Arial", size=14, weight="bold")
        self.font_normal = ctk.CTkFont(family="Arial", size=14, weight="normal")
        self.font_grande = ctk.CTkFont(family="Arial", size=20, weight="bold")


        # Frames

        
        self.top_frame = ctk.CTkFrame(self.logged_window)
        self.top_frame.configure(fg_color="#EDF6F9")
        self.top_frame.pack(pady=20, padx=10, fill="both")
        self.top_frame.columnconfigure(0, weight=1)
        self.top_frame.columnconfigure(1, weight=1)
        self.top_frame.columnconfigure(2, weight=1)
        self.top_frame.columnconfigure(3, weight=1)

        self.clock_frame = ctk.CTkFrame(self.logged_window)
        self.clock_frame.configure(fg_color="#EDF6F9")
        self.clock_frame.pack(pady=20, padx=10)
        self.clock_frame.rowconfigure(0, weight=1)
        self.clock_frame.columnconfigure(0, weight=1)

        self.news_frame = ctk.CTkFrame(self.logged_window)
        self.news_frame.configure(fg_color="#EDF6F9")
        self.news_frame.pack(pady=20, padx=10)
        self.news_frame.rowconfigure(0, weight=1)
        self.news_frame.columnconfigure(0, weight=1)

        self.button_frame = ctk.CTkFrame(self.logged_window, fg_color="#EDF6F9")
        self.button_frame.pack(pady=20, padx=10)
        

        #labels and buttons

        self.id_display_lbl = ctk.CTkLabel(self.top_frame, text=f"ID: {id}", font=self.font_small, text_color="#006D77", bg_color="#EDF6F9")
        self.id_display_lbl.grid(row=0, column=0,padx=0, pady=0)
        
        
        self.log_out_btn = ctk.CTkButton(self.top_frame, text='Log out', font=self.font_small,text_color="#006D77", command=lambda: self.log_out(), fg_color="transparent", hover=False)
        self.log_out_btn.grid(row=0, column=2, padx=0, pady=10, sticky="e")


        self.welcome_name_lbl = ctk.CTkLabel(self.top_frame, text=f"{first_name} {last_name}", font=self.font_grande, text_color="#006D77", bg_color="#EDF6F9")
        self.welcome_name_lbl.grid(row=0, column=1,padx=10, pady=10, sticky="nsew")
        self.welcome_name_lbl.place(relx=0.5, rely=0.5, anchor="center")
        
    

        self.welcome_perms_lbl = ctk.CTkLabel(self.top_frame, text=perms.capitalize(), font=self.font_normal, text_color="#006D77", bg_color="#EDF6F9")
        self.welcome_perms_lbl.grid(row=1, column=1,padx=0, pady=0, sticky="s")

        
        
    

        

       # self.logged_window.mainloop()
        self.clock_state = "clockin"
        if perms == "administrator":
            self.search = ctk.CTkButton(self.button_frame, text='Search', font=self.font_normal_bold,text_color="#EDF6F9", command=lambda: self.open_search(), fg_color='#006D77')
            self.search.grid(row=0, column=0, padx=20, pady=10)
            self.attendance = ctk.CTkButton(self.button_frame, text='Absences', font=self.font_normal_bold,text_color="#EDF6F9", command=lambda: self.open_absence(), fg_color='#006D77')
            self.attendance.grid(row=0, column=1, padx=20, pady=10)
        
        self.clock_btn_in = ctk.CTkButton(self.button_frame, text='CLOCK IN', font=self.font_normal_bold,text_color="#EDF6F9", command=self.toggle_button, fg_color='#8ac926')
        self.clock_btn_in.grid(row=0, column=2, padx=20, pady=10)

        self.clock_btn_out = ctk.CTkButton(self.button_frame, text='CLOCK OUT', font=self.font_normal_bold,text_color="#EDF6F9", command=self.toggle_button, fg_color='#ff595e')
        self.clock_btn_out.grid(row=0, column=2, padx=20, pady=10)
        self.clock_btn_out.grid_remove()
        
        #clock function
        self.time_lbl = ctk.CTkLabel(self.clock_frame,text="Current time: ", font=self.font_normal, text_color="#006D77", bg_color="#EDF6F9")
        self.time_lbl.grid(row=0, column=0,padx=0, pady=0)
        self.clock_lbl = ctk.CTkLabel(self.clock_frame, font=self.font_grande, text_color="#006D77", bg_color="#EDF6F9")
        self.clock_lbl.grid(row=1, column=0,padx=20, pady=0)

        #news function
        self.news_url= ('https://www.nytimes.com/interactive/2024/science/total-solar-eclipse-maps-path.html')
        self.news_article = Article(self.news_url, language= 'en')
        self.news_article.download()
        self.news_article.parse()
        self.news_text = self.news_article.text
        print(self.news_text)
        
        self.news_text_box = ctk.CTkTextbox(self.news_frame, font=self.font_normal, text_color="#006D77", bg_color="#EDF6F9")
        self.news_text_box.configure(width=500, height=300)
        self.news_text_box.grid(row=0, column=0, padx=0, pady=0)
        self.news_text_box.insert(1.0 , self.news_text)


        #call for RTC
        self.update_clock()

    #logout call
    def log_out(self):
        self.logged_window.withdraw()

    #RTC refresh function
    def update_clock(self):
        RTC = datetime.datetime.now()
        self.clock_lbl.configure(text=f"{str(RTC.hour)} : {str(RTC.minute)} : {str(RTC.second)}")
        self.logged_window.after(1000, self.update_clock)
    
    #calls for classes from other files
    def open_search(self):
        MySearch()
    def open_absence(self):
        Attendance()
    
    #function to switch clock buttons
    def toggle_button(self):
        if self.clock_state == 'clockin':
            self.register_clock()
            self.clock_btn_in.grid_remove()
            self.clock_btn_out.grid(row=0, column=2, padx=20, pady=10)
            self.clock_state = 'clockout'
            self.registration_success_message = CTkMessagebox(title="",message="Sucessfully Clocked-in!",
                  icon="check", option_1="Thanks")
            
        else:
            self.register_clock_out()
            self.clock_btn_out.grid_remove()
            self.clock_btn_in.grid(row=0, column=2, padx=20, pady=10)
            self.clock_state = 'clockin'
            self.registration_success_message = CTkMessagebox(title="",message="Sucessfully Clocked-out!",
                  icon="check", option_1="Thanks")

    
    #formatting of day and hour for clock function
    def format_current_day(self):
        current_day = datetime.datetime.now().strftime("%Y-%m-%d") 
        return current_day
        
    def format_current_hour(self):
        current_hour = datetime.datetime.now().strftime("%H:%M")
        return current_hour
    
    #insert clock function entrys into data base
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

        result = cursor.fetchone()

        if result:
            print(result)
            cursor.execute(clock_out_var, (self.format_current_day(), self.format_current_hour(), result[0]))

        conn.commit()

        conn.close()

