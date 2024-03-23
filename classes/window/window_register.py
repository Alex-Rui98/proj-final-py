from tkinter import *
from tkinter import Tk, messagebox
import sqlite3
import hashlib
import os
from classes.window.window_logged import Admin, Func
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import tkcalendar as tkc

class RegisterWindow:
    def __init__(self):

        # criar a janela principal
        self.register_window = ctk.CTkToplevel()
        self.register_window.title("User Registration")
        self.register_window.configure(fg_color="#EDF6F9")
        # Change background color

        # mudar foco para a janela de registo
        self.register_window.attributes('-topmost', True)
        self.register_window.focus_force()

        # guardar a fonte
        font_normal_bold = ctk.CTkFont(family="Arial", size=14, weight="bold")

        # criar rótulo de registo
        self.register_lbl = ctk.CTkLabel(self.register_window, text="Registration", font=font_normal_bold, text_color="#006D77", bg_color="#EDF6F9")
        self.register_lbl.grid(row=0, column=0, columnspan=2, pady=20, sticky="NSEW")

        # configuração dos campos
        # configuração da entrada do primeiro nome
        self.first_name_lbl = ctk.CTkLabel(self.register_window, text="Primeiro nome", font=font_normal_bold, text_color="#006D77", bg_color="#EDF6F9")
        self.first_name_lbl.grid(row=1, column=0, sticky="e", pady=10)
        self.first_name_entry = ctk.CTkEntry(self.register_window, font=font_normal_bold, text_color="#006D77", bg_color="#EDF6F9")
        self.first_name_entry.grid(row=1, column=1, pady=10, sticky="ew")

        # configuração da entrada do último nome
        self.last_name_lbl = ctk.CTkLabel(self.register_window, text="Ultimo nome", font=font_normal_bold, text_color="#006D77", bg_color="#EDF6F9")
        self.last_name_lbl.grid(row=2, column=0, sticky="e", pady=10)
        self.last_name_entry = ctk.CTkEntry(self.register_window, font=font_normal_bold, text_color="#006D77", bg_color="#EDF6F9")
        self.last_name_entry.grid(row=2, column=1, pady=10, sticky="ew")

        # configuração da entrada de nacionalidade
        self.nationality_lbl = ctk.CTkLabel(self.register_window, text="Nacionalidade", font=font_normal_bold, text_color="#006D77", bg_color="#EDF6F9")
        self.nationality_lbl.grid(row=3, column=0, sticky="e", pady=10)
        self.nationality_entry = ctk.CTkEntry(self.register_window, font=font_normal_bold, text_color="#006D77", bg_color="#EDF6F9")
        self.nationality_entry.grid(row=3, column=1, pady=10, sticky="ew")

        # configuração da entrada de password
        self.password_lbl = ctk.CTkLabel(self.register_window, text="Password", font=font_normal_bold, text_color="#006D77", bg_color="#EDF6F9")
        self.password_lbl.grid(row=4, column=0, sticky="e", pady=10)
        self.password_entry = ctk.CTkEntry(self.register_window, font=font_normal_bold, text_color="#006D77", bg_color="#EDF6F9", show="*")
        self.password_entry.grid(row=4, column=1, pady=10, sticky="ew")

        # configuração da entrada de CC
        self.card_id_lbl = ctk.CTkLabel(self.register_window, text="CC", font=font_normal_bold, text_color="#006D77", bg_color="#EDF6F9")
        self.card_id_lbl.grid(row=5, column=0, sticky="e", pady=10)
        self.card_id_entry = ctk.CTkEntry(self.register_window, font=font_normal_bold, text_color="#006D77", bg_color="#EDF6F9")
        self.card_id_entry.grid(row=5, column=1, pady=10, sticky="ew")

        # configuração da entrada de NIB
        self.nib_lbl = ctk.CTkLabel(self.register_window, text="NIB", font=font_normal_bold, text_color="#006D77", bg_color="#EDF6F9")
        self.nib_lbl.grid(row=6, column=0, sticky="e", pady=10)
        self.nib_entry = ctk.CTkEntry(self.register_window, font=font_normal_bold, text_color="#006D77", bg_color="#EDF6F9")
        self.nib_entry.grid(row=6, column=1, pady=10, sticky="ew")

        # configuração da entrada de escolaridade
        self.academics_lbl = ctk.CTkLabel(self.register_window, text="Nivel Escolaridade", font=font_normal_bold, text_color="#006D77", bg_color="#EDF6F9")
        self.academics_lbl.grid(row=7, column=0, sticky="e", pady=10)
        self.academics_entry = ctk.CTkOptionMenu(self.register_window, fg_color="White", dynamic_resizing=False, font=font_normal_bold, text_color="#006D77", values=["Analfabeto", "Fundamental Incompleto", "Fundamental Completo", "Ensino Medio Incompleto", "Ensino Medio Completo", "Superior Incompleto", "Superior Completo", "Pos Graduado"])
        self.academics_entry.grid(row=7, column=1, pady=10, sticky="ew")

        # configuração da entrada de data
        self.data_nascm_label = ctk.CTkLabel(self.register_window, text="Data de Nascimento", font=font_normal_bold, text_color="#006D77", bg_color="#EDF6F9")
        self.data_nascm_label.grid(row=8, column=0, sticky="e", pady=10)
        self.data_nascm_entry = tkc.DateEntry(self.register_window, font=font_normal_bold, text_color="#006D77", bg_color="#EDF6F9", max_width=50, date_pattern='dd-mm-yyyy')
        self.data_nascm_entry.grid(row=8, column=1, pady=10, sticky="ew")

        # configuração do botão de registo
        self.register_btn = ctk.CTkButton(self.register_window, text="Register", font=font_normal_bold, command=self.register_user, fg_color="#006D77")
        self.register_btn.grid(row=9, column=0, columnspan=2, padx=20, pady=10, sticky="SEW")

        # botão de saída
        self.exit_btn = ctk.CTkButton(self.register_window, text="Exit", font=font_normal_bold, command=self.register_window.destroy, fg_color="#006D77")
        self.exit_btn.grid(row=10, column=0, columnspan=2, padx=20, pady=10, sticky="SEW")

       # FALTA OTIMIZAR ESTA JANELA
       # Fix temporario
        self.register_window.resizable(False,False)
    def register_user(self):
        # obter dados de entrada do utilizador
        first_name = self.first_name_entry.get().capitalize()
        last_name = self.last_name_entry.get().capitalize()
        cc = self.card_id_entry.get()
        nib = self.nib_entry.get()
        academics = self.academics_entry.get()
        password = self.password_entry.get()
        data_nasc = self.data_nascm_entry.get()
        nacionalidade = self.nationality_entry.get().capitalize()

        # validar entradas
        if not first_name or not last_name or not nib or not academics or not password:
            messagebox.showerror("Error", "Not enough credentials")
            return

        # gerar salt
        salt = os.urandom(16)

        # gerar hash sha-256
        password_hash = hashlib.pbkdf2_hmac('sha256', password.encode('UTF-8'), salt, 100000)

        # converter sal e hash da palavra-passe para hexadecimal
        salt_hex = salt.hex()
        password_hash_hex = password_hash.hex()

        # valor a ser armazenado
        password_to_store = f'{salt_hex}:{password_hash_hex}'

        # conectar à base de dados
        conn = sqlite3.connect('func.db')
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO funcionario (primeiro_nome, ultimo_nome,nib,nivel_escolaridade, password, data_nascimento, nacionalidade, numero_cartao_cidadao, cargo) VALUES (?, ?,?,?,?,?,?,?,?)", (first_name, last_name,nib,academics, password_to_store,data_nasc,nacionalidade,cc, "funcionario"))
        
        conn.commit()
        conn.close()

        # mensagem de sucesso registro
        self.registration_success_message = CTkMessagebox(message="Registration was succesful!",
                  icon="check", option_1="Thanks")
        self.registration_success_message.grid()
        self.registration_success_message.after(3000, self.register_window.destroy)


