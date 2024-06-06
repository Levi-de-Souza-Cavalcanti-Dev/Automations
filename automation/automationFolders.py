import os
import tkinter as tk
from tkinter import filedialog, messagebox
import pyautogui
import time

def abrir_nova_janela():
    # Importa a função da nova janela
    from cleanFolders import excluir_arquivos_txt
    excluir_arquivos_txt()
    # Destroi a janela atual
    root.destroy()

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
            
            # Abre a subpasta no explorador de arquivos
            os.startfile(caminho_subpasta)
            
            # Espera a subpasta abrir
            time.sleep(1)
            
            # Move o cursor para a subpasta e clica com o botão direito
            first_link_position = (848, 300)  # Substitua (x, y) pelas coordenadas

            pyautogui.moveTo(first_link_position[0], first_link_position[1], duration=0.1)
            pyautogui.rightClick()
            
            time.sleep(1)
            pos_propriedades = (936, 616)
            pyautogui.moveTo(pos_propriedades[0], pos_propriedades[1], duration=0.1)
            pyautogui.click()
            
            alter_name = (329, 325)
            pyautogui.moveTo(alter_name[0], alter_name[1], duration=0.1)
            pyautogui.click()
            # Aguarda um curto período de tempo para garantir que a caixa de texto esteja pronta para receber entrada
            time.sleep(0.5)

            # Escreve "teste" na caixa de texto
            pyautogui.typewrite("teste")
            time.sleep(2)
            # Seleciona todo o texto na caixa de texto e apaga
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.press('backspace')

        else:
            messagebox.showerror("Erro", f"Índice fora do intervalo. Selecione um número entre 1 e {len(subpastas)}.")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")
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
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(padx=10, pady=10)

# Cria um campo de entrada para receber o índice da subpasta a ser aberta
entry_indice = tk.Entry(root)
entry_indice.pack(pady=10)

# Cria um botão para abrir a subpasta com base no índice fornecido
botao_abrir_pasta = tk.Button(root, text="Abrir Subpasta", command=abrir_pasta_selecionada)
botao_abrir_pasta.pack(pady=10)

# Cria um botão para abrir a nova janela
botao_nova_janela = tk.Button(root, text="Abrir Nova Janela", command=abrir_nova_janela)
botao_nova_janela.pack(pady=10)

# Inicia o loop principal do Tkinter
root.mainloop()