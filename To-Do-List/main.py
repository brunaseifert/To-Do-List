import tkinter as tk
from tkinter import messagebox
import json
import os

ARQUIVO_TAREFAS = 'tasks.json'

def carregar_tarefas():
    if os.path.exists(ARQUIVO_TAREFAS):
        with open(ARQUIVO_TAREFAS, 'r') as f:
            return json.load(f)
    return []

def salvar_tarefas(tarefas):
    with open(ARQUIVO_TAREFAS, 'w') as f:
        json.dump(tarefas, f, indent=2)

def atualizar_lista():
    lista.delete(0, tk.END)
    for i, tarefa in enumerate(tarefas):
        status = "✔" if tarefa["concluida"] else "❌"
        lista.insert(tk.END, f"{status} {tarefa['titulo']}")

def adicionar_tarefa():
    titulo = entrada.get()
    if titulo.strip() == "":
        messagebox.showwarning("Aviso", "Digite uma tarefa.")
        return
    tarefas.append({"titulo": titulo, "concluida": False})
    salvar_tarefas(tarefas)
    entrada.delete(0, tk.END)
    atualizar_lista()

def remover_tarefa():
    selecao = lista.curselection()
    if selecao:
        tarefas.pop(selecao[0])
        salvar_tarefas(tarefas)
        atualizar_lista()

def marcar_concluida():
    selecao = lista.curselection()
    if selecao:
        tarefas[selecao[0]]["concluida"] = not tarefas[selecao[0]]["concluida"]
        salvar_tarefas(tarefas)
        atualizar_lista()

# GUI
janela = tk.Tk()
janela.title("Lista de Tarefas")
janela.geometry("500x500")
janela.resizable(False, False)

# Cores e fontes
cor_fundo = "#2d033b"
cor_primaria = "#810ca8"
cor_secundaria = "#c147e9"
cor_texto = "#f3f0f6"
cor_lista = "#4f2d6b"
fonte_titulo = ("Courier New", 20, "bold")
fonte_padrao = ("Courier New", 13)
fonte_botao = ("Courier New", 12, "bold")

janela.configure(bg=cor_fundo)

label_titulo = tk.Label(janela, text="Lista de Tarefas", bg=cor_fundo, fg=cor_secundaria, font=fonte_titulo)
label_titulo.pack(pady=(18, 8))

tarefas = carregar_tarefas()

entrada_frame = tk.Frame(janela, bg=cor_fundo)
entrada_frame.pack(pady=(0, 10))

entrada = tk.Entry(entrada_frame, width=28, font=fonte_padrao, bg=cor_lista, fg=cor_texto, insertbackground=cor_texto, borderwidth=0, relief=tk.FLAT)
entrada.pack(side=tk.LEFT, padx=(0, 8), ipady=6)

botao_adicionar = tk.Button(entrada_frame, text="Adicionar", command=adicionar_tarefa, bg=cor_primaria, fg=cor_texto, font=fonte_botao, activebackground=cor_secundaria, activeforeground=cor_texto, borderwidth=0, padx=12, pady=4, cursor="hand2")
botao_adicionar.pack(side=tk.LEFT)

lista_frame = tk.Frame(janela, bg=cor_fundo)
lista_frame.pack(pady=(0, 10))

lista = tk.Listbox(lista_frame, width=40, height=13, font=fonte_padrao, bg=cor_lista, fg=cor_texto, selectbackground=cor_secundaria, selectforeground=cor_fundo, borderwidth=0, relief=tk.FLAT, highlightthickness=0)
lista.pack(side=tk.LEFT, padx=(0, 0))

scrollbar = tk.Scrollbar(lista_frame, orient=tk.VERTICAL, command=lista.yview, bg=cor_fundo)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
lista.config(yscrollcommand=scrollbar.set)

botao_frame = tk.Frame(janela, bg=cor_fundo)
botao_frame.pack(pady=(0, 10))

botao_concluir = tk.Button(botao_frame, text="Marcar como Concluída", command=marcar_concluida, bg=cor_primaria, fg=cor_texto, font=fonte_botao, activebackground=cor_secundaria, activeforeground=cor_texto, borderwidth=0, padx=16, pady=6, cursor="hand2")
botao_concluir.pack(side=tk.LEFT, padx=8)

botao_remover = tk.Button(botao_frame, text="Remover Tarefa", command=remover_tarefa, bg=cor_primaria, fg=cor_texto, font=fonte_botao, activebackground=cor_secundaria, activeforeground=cor_texto, borderwidth=0, padx=16, pady=6, cursor="hand2")
botao_remover.pack(side=tk.LEFT, padx=8)

atualizar_lista()
janela.mainloop()
