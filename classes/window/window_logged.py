import customtkinter as ctk


class LoggedWindow:

    def __init__(self):

        # Create the main window
        self.logged_window = ctk.CTk()
        self.logged_window.title("Employee Management")
        self.logged_window.configure(fg_color="#EDF6F9")

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
