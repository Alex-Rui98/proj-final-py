from tkinter import Tk, Label, Entry, Button, Frame




class LoggedWindow:
    def __init__(self, id):
        # Create the main window
        self.id_entry = id
        self.main_window = Tk()
        self.main_window.title(f"id: {self.id_entry}")
        self.main_window.configure(bg="#1F2CA5")

        # Create frames for better organization
        self.top_frame = Frame(self.main_window, bg="#1F2CA5")
        self.top_frame.pack(pady=20, padx=10)

        self.input_frame = Frame(self.main_window, bg="#1F2CA5")
        self.input_frame.pack(pady=20, padx=10)

        self.button_frame = Frame(self.main_window, bg="#1F2CA5")
        self.button_frame.pack(pady=20, padx=10)

        # Welcome text configuration
        self.welcome_lbl = Label(self.top_frame, text="id:"+ self.id, font="Arial 20", bg="#1F2CA5")
        self.welcome_lbl.pack()

           # Configuration of the register button
        self.register_clock_btn = Button(self.register_window_clock, text="Register Clock", font="Arial 14", command=self.register_clock)
        self.register_clock_btn.grid(row=4, column=0, columnspan=2, padx=20, pady=10, sticky="NSEW")
       
        # Exit button configuration
        self.exit_btn = Button(self.button_frame, text='Exit', font="Arial 14", command=self.main_window.destroy, bg="#0F172A", fg='white')
        self.exit_btn.grid(row=0, column=2, padx=20, pady=10)




 
     
 