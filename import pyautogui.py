import os
import tkinter as tk
from tkinter import filedialog, messagebox

def listar_subpastas(diretorio):
    try:
        # Lista todos os arquivos e diretórios no caminho especificado
        itens = os.listdir(diretorio)

        # Filtra apenas os diretórios e arquivos .txt
        subpastas_e_txt = [item for item in itens if os.path.isdir(os.path.join(diretorio, item)) or item.endswith(".txt")]

        # Limpa a listbox antes de adicionar novos itens
        listbox.delete(0, tk.END)

        # Adiciona as subpastas e arquivos .txt na listbox
        for item in subpastas_e_txt:
            listbox.insert(tk.END, item)
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

def selecionar_diretorio():
    diretorio = filedialog.askdirectory()
    if diretorio:
        listar_subpastas(diretorio)
        # Armazena o diretório selecionado globalmente para usar na renomeação
        global diretorio_selecionado
        diretorio_selecionado = diretorio

def abrir_subpasta(diretorio, indice):
    try:
        # Lista todos os arquivos e diretórios no caminho especificado
        itens = os.listdir(diretorio)

        # Filtra apenas os diretórios
        subpastas = sorted([item for item in itens if os.path.isdir(os.path.join(diretorio, item))])

        if 1 <= indice <= len(subpastas):
            subpasta_selecionada = subpastas[indice - 1]
            caminho_subpasta = os.path.join(diretorio, subpasta_selecionada)
            os.startfile(caminho_subpasta)
        else:
            messagebox.showerror("Erro", f"Índice fora do intervalo. Selecione um número entre 1 e {len(subpastas)}.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

def abrir_pasta_selecionada():
    try:
        indice = int(entry_indice.get())
        abrir_subpasta(diretorio_selecionado, indice)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")

# Inicializa a variável global do diretório
diretorio_selecionado = ""

# Cria a janela principal
root = tk.Tk()
root.title("Gerenciamento de Diretórios")

# Cria um botão para selecionar o diretório
botao_selecionar = tk.Button(root, text="Selecionar Diretório", command=selecionar_diretorio)
botao_selecionar.pack(pady=10)

# Cria uma Listbox para exibir as subpastas
listbox = tk.Listbox(root, width=50, height=20)
listbox.pack(padx=10, pady=10)

# Cria um campo de entrada para receber o índice da subpasta a ser aberta
entry_indice = tk.Entry(root)
entry_indice.pack(pady=10)

# Cria um botão para abrir a subpasta com base no índice fornecido
botao_abrir_pasta = tk.Button(root, text="Abrir Subpasta", command=abrir_pasta_selecionada)
botao_abrir_pasta.pack(pady=10)

# Inicia o loop principal do Tkinter
root.mainloop()
