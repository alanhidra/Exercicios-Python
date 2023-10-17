import tkinter as tk
from tkinter import messagebox
import config

# Resto do código de cadastro como mencionado anteriormente

def fazer_cadastro():
    global entry_nome, entry_usuario, entry_senha, entry_repetir_senha, entry_email, entry_cpf
    nome = entry_nome.get()
    usuario = entry_usuario.get()
    senha = entry_senha.get()
    repetir_senha = entry_repetir_senha.get()
    email = entry_email.get()
    cpf = entry_cpf.get()

    if senha == repetir_senha:
        # Adicione o usuário ao arquivo de configuração
        config.users[usuario] = senha

        with open("usuarios.txt", "a") as arquivo:
            arquivo.write(f"{nome},{usuario},{senha},{email},{cpf}\n")
        messagebox.showinfo("Cadastro", "Cadastro realizado com sucesso!")
        # Limpar os campos
        entry_nome.delete(0, 'end')
        entry_usuario.delete(0, 'end')
        entry_senha.delete(0, 'end')
        entry_repetir_senha.delete(0, 'end')
        entry_email.delete(0, 'end')
        entry_cpf.delete(0, 'end')

        # Atualize o arquivo config.py com o novo usuário
        with open("config.py", "w") as config_file:
            config_file.write("users = {\n")
            for u, p in config.users.items():
                config_file.write(f'    "{u}": "{p}",\n')
            config_file.write("}\n")
    else:
        messagebox.showerror("Erro", "As senhas não conferem. Tente novamente.")


# Função para realizar o login


    
    with open("usuarios.txt", "r") as arquivo:
        for linha in arquivo:
            partes = linha.strip().split(',')
            if len(partes) == 5 and partes[1] == usuario and partes[2] == senha:
                messagebox.showinfo("Login", "Login realizado com sucesso!")
                # Adicione aqui o código para ação após o login bem-sucedido
                return
        messagebox.showerror("Erro", "Usuário ou senha incorretos.")

cadastro = tk.Tk()
cadastro.title("Cadastro e Login")

# Nome Completo
label_nome = tk.Label(cadastro, text="Nome Completo:")
label_nome.pack()
entry_nome = tk.Entry(cadastro)
entry_nome.pack()

# Login
label_usuario = tk.Label(cadastro, text="Login:")
label_usuario.pack()
entry_usuario = tk.Entry(cadastro)
entry_usuario.pack()

# Senha
label_senha = tk.Label(cadastro, text="Senha:")
label_senha.pack()
entry_senha = tk.Entry(cadastro, show="*")
entry_senha.pack()

# Repetir Senha
label_repetir_senha = tk.Label(cadastro, text="Repetir Senha:")
label_repetir_senha.pack()
entry_repetir_senha = tk.Entry(cadastro, show="*")
entry_repetir_senha.pack()

# E-mail
label_email = tk.Label(cadastro, text="E-mail:")
label_email.pack()
entry_email = tk.Entry(cadastro)
entry_email.pack()

# CPF
label_cpf = tk.Label(cadastro, text="CPF:")
label_cpf.pack()
entry_cpf = tk.Entry(cadastro)
entry_cpf.pack()

# Botão para realizar o cadastro
botao_cadastrar = tk.Button(cadastro, text="Cadastrar", command=fazer_cadastro)
botao_cadastrar.pack()

cadastro.mainloop()
