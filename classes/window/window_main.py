#imports 
import customtkinter as ctk
from classes.window.window_register import RegisterWindow
from classes.window.window_logged import Admin
import hashlib
import sqlite3
from CTkMessagebox import CTkMessagebox
 
 
#Main window class:
class MainWindow:
    def __init__(self):

        # Create the main window
        self.main_window = ctk.CTk()
        self.main_window.title("Employee Management")
        self.main_window.configure(fg_color="#EDF6F9")

        self.main_window.after(201, lambda :self.main_window.iconbitmap('assets\\clock_icon.ico'))

        # Store font
        font_normal_bold = ctk.CTkFont(family="Arial", size=14, weight="bold")
        font_normal = ctk.CTkFont(family="Arial", size=14, weight="normal")
        font_grande = ctk.CTkFont(family="Arial", size=20, weight="bold")

        # Create frames for better organization
        self.top_frame = ctk.CTkFrame(self.main_window)
        self.top_frame.pack(pady=20, padx=10)

        self.input_frame = ctk.CTkFrame(self.main_window, fg_color="#EDF6F9")
        self.input_frame.pack(pady=20, padx=10)

        self.button_frame = ctk.CTkFrame(self.main_window, fg_color="#EDF6F9")
        self.button_frame.pack(pady=20, padx=10)

        # Welcome text configuration
        self.welcome_lbl = ctk.CTkLabel(self.top_frame, text='Employee Management', font=font_grande,text_color="#006D77", bg_color="#EDF6F9")
        self.welcome_lbl.pack()

        # Configuration of ID input field
        self.login_lbl = ctk.CTkLabel(self.input_frame, text="ID:", font=font_normal_bold, text_color="#006D77", bg_color="#EDF6F9")
        self.login_lbl.grid(row=0, column=0, sticky="e")
        self.login_entry = ctk.CTkEntry(self.input_frame, font=font_normal,text_color="#006D77", bg_color="#EDF6F9")
        self.login_entry.grid(row=0, column=1, pady=10, padx=20)

        # Configuration of the password field
        self.password_lbl = ctk.CTkLabel(self.input_frame, text="Password:", font=font_normal_bold,text_color="#006D77", bg_color="#EDF6F9")
        self.password_lbl.grid(row=1, column=0, sticky="e")
        self.password_entry = ctk.CTkEntry(self.input_frame, font=font_normal,text_color="#006D77", bg_color="#EDF6F9", show="*")
        self.password_entry.grid(row=1, column=1, pady=10)

        # Login button configuration
        self.login_btn = ctk.CTkButton(self.button_frame, text='Login', font=font_normal, command=self.open_login_window, fg_color='#006D77')
        self.login_btn.grid(row=0, column=0, padx=20, pady=10)

        # Register button configuration
        self.register_btn = ctk.CTkButton(self.button_frame, text='Register', font=font_normal, command=self.open_register_window, fg_color='#006D77')
        self.register_btn.grid(row=0, column=1, padx=20, pady=10)

        # Exit button configuration
        self.exit_btn = ctk.CTkButton(self.button_frame, text='Exit', font=font_normal, command=self.main_window.destroy, fg_color='#006D77')
        self.exit_btn.grid(row=0, column=2, padx=20, pady=10)
        
        self.main_window.update()
        self.main_window.deiconify()

    #retrive ID for other files
    def id_exp(id_entry):
        return id_entry

    #classes to execute files
    def open_register_window(self):
        RegisterWindow()
 
    def open_login_window(self):
        CheckLogin(self.main_window, self.login_entry, self.password_entry)
    
    def close_window(self):
        self.main_window.withdraw()

        
class CheckLogin:
    def __init__(self, main_window, id_entry, password_entry):
        self.main_window = main_window
        self.id_entry = id_entry
        self.password_entry = password_entry
        self.check_credentials(id_entry.get(), password_entry.get())
    
    #cross-check login details
    def check_credentials(self, id_entry, password_entry):
        # connect to database
        conn = sqlite3.connect('func.db')
        cursor = conn.cursor() 

        # ask database to fetch corresponding ID
        cursor.execute("SELECT * FROM employee WHERE id = ?", (id_entry,))
        user = cursor.fetchone()

        if user:
            # divide password and salt by ":"
            stored_salt_hex, stored_password_hash_hex = user[10].split(':')
            # convert salt to bytes
            stored_salt = bytes.fromhex(stored_salt_hex)

            # hash password and salt
            hashed_password = hashlib.pbkdf2_hmac('sha256', password_entry.encode('utf-8'), stored_salt, 100000).hex()

            # verify password from database and entry

            if hashed_password == stored_password_hash_hex:
                print(f"Logging in as {user[9]}")
                
                CTkMessagebox(title="", message="Login was succesful!",
                  icon="check", option_1="Thanks")
                self.main_window.withdraw()
                nova_janela = Admin(user[0], user[1], user[2], user[9])
                nova_janela.logged_window.mainloop()
            else:
                CTkMessagebox(title="", message="Login wasn't successful", icon="cancel")
                return False
                
        else:
          
            CTkMessagebox(title="", message="User not found", icon="cancel")
            return False
