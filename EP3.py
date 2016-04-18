#Criando o tabuleiro
import tkinter as tk
class tabuleiro:
    def __init__(self):
#CRIANDO OS BOTOES    
        self.window = tk.Tk()
        #DANDO UM NOME A JANELA
        self.window.title("Jogo da velha")
        self.window.geometry("300x300")
        self.window.rowconfigure(0, minisize=100,weight=1)
        self.window.rowconfigure(1,minisize=100,weight=1)
        self.window.rowconfigure(2, minisize=100,weight=1)
        self.window.columnconfigure(0, minisize=100,weight=1)
        self.window.columnconfigure(1, minisize=100,weight=1)
        self.window.columnconfigure(2, minisize=100,weight=1)
        botao_00 = tk.Button (window) #00 é a localização do botao esse no caso é o superior esquerdo
        botao_00.grid(row=0,column=0,sticky="nswe")

        botao_01 = tk.Button (window)
        botao_01.grid(row=0,column=1,sticky="nswe")

        botao_02 =tk.Button (window)
        botao_02.grid (row=0,column=2,sticky="nswe")

        botao_10=tk.Button (window)
        botao_10.grid(row=1,column=0,sticky="nswe")

        botao_20=tk.Button (window)
        botao_20.grid(row=2,column=0,sticky="nswe")

        botao_11=tk.Button (window)
        botao_11.grid(row=1,column=1,sticky="nswe")

        botao_21=tk.Button (window)
        botao_21.grid(row=2,column=1,sticky="nswe")

        botao_12=tk.Button (window)
        botao_12.grid(row=1,column=2,sticky="nswe")

        botao_22 = tk.Button (window)
        botao_22.grid(row=2,column=2,sticky="nswe")



        window.mainloop()