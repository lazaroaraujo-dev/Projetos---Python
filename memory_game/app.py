import tkinter as tk
from tkinter import PhotoImage

# Função do jogo
def play_game():
    for widget in janela.winfo_children():
        widget.destroy()
        # Agora cria o conteúdo do "jogo"
    janela.configure(bg='lightblue')
    label_jogo = tk.Label(janela, text="Jogo iniciado!", font=("Arial", 24),bg="lightblue")
    label_jogo.pack(pady=100)

# # Fonte e cores
cor_fundo = "#000000"
cor_letra = "#ffffff"
cor_fonte = ('Arial', 26, 'bold italic')
fonte_helvica = ("Helvetica", 16, "bold italic")

# Criando a janela / instanciando uma janela na memória da máquina
janela = tk.Tk()
janela.title("Memory Game")
janela.geometry("640x480+200+400")
janela.configure(bg="black")

janela.minsize(640,480)
# Ícone da janela
icon = PhotoImage(file="icone_da_janela.png")
janela.iconphoto(True, icon)

# Imagem de fundo (usando apenas Tkinter)
imagem_fundo = PhotoImage(file="imagem.png")

# Coloca a imagem como fundo
label_fundo = tk.Label(janela, image=imagem_fundo)
label_fundo.place(x=0, y=0, relwidth=1, relheight=1)

# Label do título (por cima da imagem)
title_label = tk.Label(janela, text="Memory Game", font=cor_fonte,
                        fg=cor_letra, bg=cor_fundo)
title_label.place(relx=0.5, rely=0.2, anchor="center")

# Botão Play
botao_play = tk.Button(janela, text="Play", command=play_game,
                       bg='green', fg='white', padx=40,
                       font=fonte_helvica)
botao_play.place(relx=0.5, rely=0.5, anchor="center")

# Botão Quit
botao_quit = tk.Button(janela, text="Quit", command=janela.quit,
                       bg='red', fg='white', padx=40,
                       font=fonte_helvica)
botao_quit.place(relx=0.5, rely=0.65, anchor="center")

# Exibir a janela
janela.mainloop()
