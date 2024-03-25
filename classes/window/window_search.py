import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
import sqlite3
from difflib import SequenceMatcher

class CustomSearchButton(ttk.Frame):
    def __init__(self, master, table_frame, data, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.table_frame = table_frame
        self.data = data
        
        self.search_var = tk.StringVar()
    
        self.search_entry = ttk.Entry(self, textvariable=self.search_var)
        self.search_entry.pack(side=tk.LEFT, padx=5, pady=5)

        self.search_button = ttk.Button(self, text="Procurar",command=self.search_table)
        self.search_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.reset_button = ttk.Button(self, text="Reset",command=self.reset_table)
        self.reset_button.pack(side=tk.LEFT, padx=5, pady=5)

    def reset_table(self):
        self.table_frame.refresh_table(self.data)
    def search_table(self):
        filtered_data = []

        if self.search_entry.get() == "":
            self.reset_table()
            return

        for person in self.data:
            id = person.get('ID')
            firstname = person.get('primeiro_nome')
            lastname = person.get('ultimo_nome')

            s = SequenceMatcher(None, str(f"{firstname} {lastname}").lower(), self.search_entry.get().lower())

            if str(id) == self.search_entry.get():
                filtered_data.append({ "ratio": 1.0, "person": person })
                break
            elif s.ratio() > 0.5:
                filtered_data.append({ "ratio": s.ratio(), "person": person })

        filtered_data.sort(key=lambda x:x['ratio'], reverse=True)

        # Update the table with the filtered data
        self.table_frame.refresh_table([filtered['person'] for filtered in filtered_data])

 
class EditableTable(ttk.Frame):
    def __init__(self, master, data, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.data = data
        
        self.table = ttk.Treeview(self, columns=("ID", "Primeiro Nome", "Último Nome", "Cargo"), show="headings")
        self.table.heading("ID", text="ID")
        self.table.heading("Primeiro Nome", text="Primeiro Nome")
        self.table.heading("Último Nome", text="Último Nome")
        self.table.heading("Cargo", text="Cargo")
        self.table.pack(expand=True, fill="both", padx=5, pady=5)
 
        self.table.bind("<Double-1>", self.edit_cell)
 
        self.display_data()
        
 
    def display_data(self, data=None):
        if data is None:
            data = self.data

        for idx, person in enumerate(data):
            self.table.insert("", "end", text=str(idx), values=(person["ID"], person["primeiro_nome"], person["ultimo_nome"], person["cargo"]))
    
    def refresh_table(self, new_data):
        # Clear the existing items in the table
        for item in self.table.get_children():
            self.table.delete(item)

        # Update the table with the new data
        self.data = new_data
        self.display_data()

 
    def edit_cell(self, event):
        item = self.table.selection()[0]
        column = self.table.identify_column(event.x)
        if column != "#0":  # Não permitir edição da coluna ID
            cell_value = self.table.item(item, "values")[int(column[1:]) - 1]
            new_value = self.ask_for_input("Edit value", f"New value for {column}:", initial_value=cell_value)
            if new_value is not None:
                self.table.set(item, column, new_value)
 
    def ask_for_input(self, title, prompt, initial_value=""):
        return simpledialog.askstring(title, prompt, initialvalue=initial_value)
 
class MyApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Pesquisar Funcionários")
        
        self.data = self.db_get()

        self.table_frame = EditableTable(self, self.data)
        self.search_button = CustomSearchButton(self, self.table_frame, self.data)

        self.search_button.pack(padx=10, pady=10)
        self.table_frame.pack(expand=True, fill="both", padx=10, pady=10)


    def db_get(self):
        conn = sqlite3.connect('func.db')
        cursor = conn.cursor()

        cursor.execute("SELECT ID, primeiro_nome, ultimo_nome, cargo FROM funcionario")

        rows = cursor.fetchall()

        result_list = [{"ID": row[0], "primeiro_nome": row[1],"ultimo_nome": row[2], "cargo": row[3]} for row in rows]

        conn.close()

        return result_list
