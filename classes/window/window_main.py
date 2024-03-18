#imports
from tkinter import Tk, Label, Entry, Button, Frame
from classes.window.window_register import RegisterWindow
from classes.window.check_login import CheckLogin
 
#Main window class:
class MainWindow:
    def __init__(self):
        # Create the main window
        self.main_window = Tk()
        self.main_window.title("Employee Management")
        self.main_window.configure(bg="#1F2CA5")

        # Create frames for better organization
        self.top_frame = Frame(self.main_window, bg="#1F2CA5")
        self.top_frame.pack(pady=20, padx=10)

        self.input_frame = Frame(self.main_window, bg="#1F2CA5")
        self.input_frame.pack(pady=20, padx=10)

        self.button_frame = Frame(self.main_window, bg="#1F2CA5")
        self.button_frame.pack(pady=20, padx=10)

        # Welcome text configuration
        self.welcome_lbl = Label(self.top_frame, text='Employee Management', font="Arial 20", bg="#1F2CA5")
        self.welcome_lbl.pack()

        # Configuration of ID input field
        self.login_lbl = Label(self.input_frame, text="ID:", font="Arial 20 bold", fg='white', bg="#1F2CA5")
        self.login_lbl.grid(row=0, column=0, sticky="e")
        self.login_entry = Entry(self.input_frame, font="Arial 14 bold", bg="white")
        self.login_entry.grid(row=0, column=1, pady=10, padx=20)

        # Configuration of the password field
        self.password_lbl = Label(self.input_frame, text="Password:", font="Arial 20 bold",fg='white', bg="#1F2CA5")
        self.password_lbl.grid(row=1, column=0, sticky="e")
        self.password_entry = Entry(self.input_frame, font="Arial 14 bold", bg="white", show="*")
        self.password_entry.grid(row=1, column=1, pady=10)

        # Login button configuration
        self.login_btn = Button(self.button_frame, text='Login', font="Arial 14", command=self.open_login_window, bg="#0F172A", fg='white')
        self.login_btn.grid(row=0, column=0, padx=20, pady=10)

        # Register button configuration
        self.register_btn = Button(self.button_frame, text='Register', font="Arial 14", command=self.open_register_window, bg="#0F172A", fg='white')
        self.register_btn.grid(row=0, column=1, padx=20, pady=10)

        # Exit button configuration
        self.exit_btn = Button(self.button_frame, text='Exit', font="Arial 14", command=self.main_window.destroy, bg="#0F172A", fg='white')
        self.exit_btn.grid(row=0, column=2, padx=20, pady=10)

    def open_register_window(self):
        RegisterWindow()
 
    def open_login_window(self):
        CheckLogin(self.login_entry, self.password_entry)
