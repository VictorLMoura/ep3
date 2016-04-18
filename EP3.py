#Criando o tabuleiro
import tkinter as tk
class tabuleiro:
    def __init__(self):
#CRIANDO OS BOTOES    
        self.window = tk.Tk()
        #DANDO UM NOME A JANELA
        self.window.title("Jogo da Velha!")
        self.window.geometry("300x300")
        self.window.rowconfigure(0, minsize=100,weight=1)
        self.window.rowconfigure(1,minsize=100,weight=1)
        self.window.rowconfigure(2, minsize=100,weight=1)
        self.window.columnconfigure(0, minsize=100,weight=1)
        self.window.columnconfigure(1, minsize=100,weight=1)
        self.window.columnconfigure(2, minsize=100,weight=1)
        botao_00 = tk.Button (self.window) #00 é a localização do botao esse no caso é o superior esquerdo
        botao_00.grid(row=0,column=0,sticky="nswe")

        botao_01 = tk.Button (self.window)
        botao_01.grid(row=0,column=1,sticky="nswe")

        botao_02 =tk.Button (self.window)
        botao_02.grid (row=0,column=2,sticky="nswe")

        botao_10=tk.Button (self.window)
        botao_10.grid(row=1,column=0,sticky="nswe")

        botao_20=tk.Button (self.window)
        botao_20.grid(row=2,column=0,sticky="nswe")

        botao_11=tk.Button (self.window)
        botao_11.grid(row=1,column=1,sticky="nswe")

        botao_21=tk.Button (self.window)
        botao_21.grid(row=2,column=1,sticky="nswe")

        botao_12=tk.Button (self.window)
        botao_12.grid(row=1,column=2,sticky="nswe")

        botao_22 = tk.Button (self.window)
        botao_22.grid(row=2,column=2,sticky="nswe")



    def iniciar(self):
        self.window.mainloop()
app= tabuleiro()
app.iniciar()