import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# Função para excluir todos os arquivos .txt em um diretório
def excluir_arquivos_txt():
    # Abrir a caixa de diálogo para selecionar o diretório
    diretorio = filedialog.askdirectory()

    if diretorio:
        try:
            # Percorrer todos os arquivos no diretório
            for arquivo in os.listdir(diretorio):
                # Verificar se o arquivo é um arquivo .txt
                if arquivo.endswith(".txt"):
                    # Construir o caminho completo do arquivo
                    caminho_arquivo = os.path.join(diretorio, arquivo)
                    # Excluir o arquivo
                    os.remove(caminho_arquivo)

            # Exibir mensagem de sucesso após excluir os arquivos
            messagebox.showinfo("Sucesso", "Todos os arquivos .txt foram excluídos com sucesso.")
        except Exception as e:
            # Exibir mensagem de erro se ocorrer um problema
            messagebox.showerror("Erro", f"Ocorreu um erro ao excluir os arquivos: {e}")
# Criando a janela principal
janela = tk.Tk()
janela.title("Excluir Arquivos .txt")

# Criando um rótulo na janela
rotulo = ttk.Label(janela, text="Clique no botão para excluir todos os arquivos .txt de um diretório.")
rotulo.pack(padx=10, pady=10)

# Criando um botão na janela
botao_excluir = ttk.Button(janela, text="Excluir Arquivos .txt", command=excluir_arquivos_txt)
botao_excluir.pack(padx=10, pady=10)

# Iniciando o loop principal da janela
janela.mainloop()