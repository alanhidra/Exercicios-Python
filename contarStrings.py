import tkinter as tk

def contar_string():
    texto = entrada.get()
    quantidade_caracteres = len(texto)
    resultado_label.config(text=f"Total de caracteres: {quantidade_caracteres}")

contador = tk.Tk()
contador.title("Contador de Strings")

label = tk.Label(contador, text="Digite sua string:")
label.pack()

entrada = tk.Entry(contador)
entrada.pack()

botao_contar = tk.Button(contador, text="Contar", command=contar_string)
botao_contar.pack()

resultado_label = tk.Label(contador, text="Total de caracteres: 0")
resultado_label.pack()

contador.mainloop()
