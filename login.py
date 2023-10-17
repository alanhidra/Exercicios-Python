import tkinter as tk
from tkinter import messagebox
import config
import home  # Importe o módulo home.py

login = tk.Tk()
login.title("Login")

label_usuario = tk.Label(login, text="Usuário:")
label_usuario.pack()

entry_usuario = tk.Entry(login)
entry_usuario.pack()

label_senha = tk.Label(login, text="Senha:")
label_senha.pack()

entry_senha = tk.Entry(login, show="*")
entry_senha.pack()

def fazer_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    if usuario in config.users and config.users[usuario] == senha:
        messagebox.showinfo("Login", "Login realizado com sucesso!")
        # Adicione aqui o código para ação após o login bem-sucedido

        # Chame a função para exibir a tela "home"
        home.exibir_home()
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos.")

botao_login = tk.Button(login, text="Login", command=fazer_login)
botao_login.pack()

login.mainloop()
