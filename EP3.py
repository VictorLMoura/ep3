#Criando o tabuleiro
import tkinter as tk
class tabuleiro:
    def __init__(self):
#CRIANDO OS BOTOES    
        self.window = tk.Tk()
        #DANDO UM NOME A JANELA
        self.window.title("Jogo da Velha!")
        #DANDO TAMANHO AO TABULEIRO
        self.window.geometry("300x325")
        #DANDO UM TAMANHO AOS BOTOES
        self.window.rowconfigure(0, minsize=100,weight=1)
        self.window.rowconfigure(1,minsize=100,weight=1)
        self.window.rowconfigure(2, minsize=100,weight=1)
        self.window.columnconfigure(0, minsize=100,weight=1)
        self.window.columnconfigure(1, minsize=100,weight=1)
        self.window.columnconfigure(2, minsize=100,weight=1)
        #DANDO TAMANHO A INDICAÇÃO DE JOGADOR USANDO LABEL
    
           
        #self.Label_status = tk.Label()#NÃO SEI O QUE DEU ERRADO AQUI
        
        
        self.botao_00 = tk.Button (self.window) #00 é a localização do botao esse no caso é o superior esquerdo
        #REALIZAR AÇÃO QUANDO CLICADO
        self.botao_00.grid(row=0,column=0,sticky="nsew")
        self.botao_00.configure(command= self.botao_00clicado)

        self.botao_01 = tk.Button (self.window)
        self.botao_01.grid(row=0,column=1,sticky="nsew")
        self.botao_01.configure(command= self.botao_01clicado)
        
        self.botao_02 =tk.Button (self.window)
        self.botao_02.grid (row=0,column=2,sticky="nsew")
        self.botao_02.configure(command= self.botao_02clicado)
        
        self.botao_10=tk.Button (self.window)
        self.botao_10.grid(row=1,column=0,sticky="nsew")
        self.botao_10.configure(command= self.botao_10clicado)
        
        self.botao_20=tk.Button (self.window)
        self.botao_20.grid(row=2,column=0,sticky="nsew")
        self.botao_20.configure(command= self.botao_20clicado)
        
        self.botao_11=tk.Button (self.window)
        self.botao_11.grid(row=1,column=1,sticky="nsew")
        self.botao_11.configure(command= self.botao_11clicado)
        
        self.botao_21=tk.Button (self.window)
        self.botao_21.grid(row=2,column=1,sticky="nsew")
        self.botao_21.configure(command= self.botao_21clicado)

        self.botao_12=tk.Button (self.window)
        self.botao_12.grid(row=1,column=2,sticky="nsew")
        self.botao_12.configure(command= self.botao_12clicado)

        self.botao_22 = tk.Button (self.window)
        self.botao_22.grid(row=2,column=2,sticky="nsew")
        self.botao_22.configure(command= self.botao_22clicado)
        
        self.Label_vez = tk.Label(self.window)
        self.Label_vez.configure(font="Courier 14 bold")
        self.Label_vez.grid(row = 3, column = 0, columnspan=2)
        self.Label_vez.configure(text='Vez do: Jogador 1')
        

  #AÇÕES DOS BOTÕES , SÓ UM EXEMPLO
    def clique (self, i, j):
        print ("botao {0} x {1} clicado".format(i,j))
    def botao_00clicado(self):
        self.clique(0,0)
        self.botao_00.configure(text = "X")
       # recebe_jogada(0,0)
    def botao_01clicado(self):
        self.clique(0,1)
        self.botao_01.configure(text = "X")
      #  recebe_jogada(0,1)
    def botao_10clicado(self):
        self.clique(1,0)
        self.botao_10.configure(text = "X")
     #   recebe_jogada(1,0)
    def botao_20clicado(self):
        self.clique(2,0)
        self.botao_20.configure(text = "X")
      #  recebe_jogada(2,0)
    def botao_11clicado(self):
        self.clique(1,1)
        self.botao_11.configure(text = "X")
      #  recebe_jogada(1,1)
    def botao_12clicado(self):
        self.clique(1,2)
        self.botao_12.configure(text = "X")
      #  recebe_jogada(1,2)
    def botao_21clicado(self):
        self.clique(2,1)
        self.botao_21.configure(text = "X")
      #  recebe_jogada(2,1)
    def botao_22clicado(self):
        self.clique(2,2)
        self.botao_22.configure(text = "X")
     #   recebe_jogada(2,2)
    def botao_02clicado(self):
        self.clique(0,2)
        self.botao_02.configure(text = "X")
      #  recebe_jogada(0,2)

    def iniciar(self):
        self.window.mainloop()
app= tabuleiro()
app.iniciar()

class Jogo:
    def __init_(self):
       self.jogador= 1

    def recebe_jogada(i,j):
        muda_jogador(self)      
        
    def muda_jogador(self):
        if (self.jogador==1):
            self.label.configure(text='Jogador 2')
            self.jogador=2
            
        if (self.jogador==2):
            self.label.configure(text='Jogador 1')
            self.jogador=1