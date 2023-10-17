import tkinter as tk
import subprocess

def exibir_home():
    home = tk.Tk()
    home.title("Tela Home")

    def abrir_contador_strings():
        # Abre o arquivo contarStrings.py usando o comando 'python'
        subprocess.Popen(['python', 'contarStrings.py'])

    def abrir_notas():
        # Abre o arquivo notas.py usando o comando 'python'
        subprocess.Popen(['python', 'notas.py'])

    botao_contador_strings = tk.Button(home, text="Contador de Strings", command=abrir_contador_strings)
    botao_contador_strings.pack()

    botao_notas = tk.Button(home, text="Notas", command=abrir_notas)
    botao_notas.pack()

    home.mainloop()
