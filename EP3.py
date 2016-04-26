#Criando o tabuleiro
import tkinter as tk
class tabuleiro:
    def __init__(self):
        #import Jogo #, precisamos importar a classe Jogo para usar o atributo jogador
#CRIANDO OS BOTOES    
        self.jogador=1
        self.venceu = False
        self.window = tk.Tk()
        #DANDO UM NOME A JANELA
        self.window.title("Jogo da Velha!")
        #DANDO TAMANHO AO TABULEIRO
        self.window.geometry("400x400")
        #DANDO UM TAMANHO AOS BOTOES
        self.window.rowconfigure(0, minsize=100,weight=1)
        self.window.rowconfigure(1,minsize=100,weight=1)
        self.window.rowconfigure(2, minsize=100,weight=1)
        self.window.rowconfigure(4, minsize=50,weight=1)
        self.window.columnconfigure(0, minsize=100,weight=1)
        self.window.columnconfigure(1, minsize=100,weight=1)
        self.window.columnconfigure(2, minsize=100,weight=1)
        #DANDO TAMANHO A INDICAÇÃO DE JOGADOR USANDO LABEL
        
        
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
        
        self.label_vez = tk.Label(self.window)
        self.label_vez.configure(font="Courier 14 bold")
        self.label_vez.grid(row = 3, column = 0, columnspan=3)
        self.label_vez.configure(text='Vez do: Jogador 1')
        
        self.botao_reiniciar = tk.Button (self.window)
        self.botao_reiniciar.grid (row=4, column = 1, sticky = "nsew")  
        self.botao_reiniciar.configure (text = "Reiniciar")
        self.botao_reiniciar.configure(font="Courier 14 bold")
        self.botao_reiniciar.configure(command= self.reiniciar)
        
        self.B_00_clicado = False
        self.B_10_clicado = False
        self.B_20_clicado = False
        self.B_11_clicado = False
        self.B_12_clicado = False
        self.B_01_clicado = False
        self.B_02_clicado = False
        self.B_22_clicado = False
        self.B_21_clicado = False
        
        
        #Precisamos descobrir como importar a classe Jogo para usar a muda_jogador

  #AÇÕES DOS BOTÕES , SÓ UM EXEMPLO
    def clique (self, i, j):
        print ("botao {0} x {1} clicado".format(i,j))        
       
        
    def botao_00clicado(self):
        if (self.B_00_clicado == False):
            if (self.venceu==False):
                self.B_00_clicado = True
                self.clique(0,0)
                if(self.jogador==1):
                    self.botao_00.configure(text = "X")
                else:
                    self.botao_00.configure(text = "O")
                self.muda_jogador()
                self.verifica_vencedor()
            
       # recebe_jogada(0,0)
    def botao_01clicado(self):
        if (self.B_01_clicado == False):
            if (self.venceu==False):
                self.B_01_clicado = True
                self.clique(0,1)
                if(self.jogador==1):
                    self.botao_01.configure(text = "X")
                else:
                    self.botao_01.configure(text = "O")
                self.muda_jogador()
                self.verifica_vencedor()
            
        
      #  recebe_jogada(0,1)
    def botao_10clicado(self):
        if (self.B_10_clicado == False):
            if (self.venceu==False):
                self.B_10_clicado = True
                self.clique(1,0)
                if(self.jogador==1):
                    self.botao_10.configure(text = "X")
                else:
                    self.botao_10.configure(text = "O")
                self.muda_jogador()
                self.verifica_vencedor()
            
     #      recebe_jogada(1,0)
    def botao_20clicado(self):
        if (self.B_20_clicado == False):
            if (self.venceu==False):
                self.B_20_clicado = True
                self.clique(2,0)
                if(self.jogador==1):
                    self.botao_20.configure(text = "X")
                else:
                    self.botao_20.configure(text = "O")
                self.muda_jogador()
                self.verifica_vencedor()
           
      #  recebe_jogada(2,0)
    def botao_11clicado(self):
        if (self.B_11_clicado == False):
            if (self.venceu==False):
                self.B_11_clicado = True
                self.clique(1,1)
                if(self.jogador==1):
                    self.botao_11.configure(text = "X")
                else:
                    self.botao_11.configure(text = "O")
                self.muda_jogador()
                self.verifica_vencedor()
            
      #  recebe_jogada(1,1)
    def botao_12clicado(self):
        if (self.B_12_clicado == False):
            if (self.venceu==False):
                self.B_12_clicado = True
                self.clique(1,2)
                if(self.jogador==1):
                    self.botao_12.configure(text = "X")
                else:
                    self.botao_12.configure(text = "O")
                self.muda_jogador()
                self.verifica_vencedor()
            
      #  recebe_jogada(1,2)
    def botao_21clicado(self):
      if (self.B_21_clicado == False):
            if (self.venceu==False):
                self.B_21_clicado = True
                self.clique(2,1)
                if(self.jogador==1):
                    self.botao_21.configure(text = "X")
                else:
                    self.botao_21.configure(text = "O")
                self.muda_jogador()
                self.verifica_vencedor()
            
      #  recebe_jogada(2,1)
    def botao_22clicado(self):
        if (self.B_22_clicado == False):
            if (self.venceu==False):
                self.B_22_clicado = True
                self.clique(2,2)
                if(self.jogador==1):
                    self.botao_22.configure(text = "X")
                else:
                    self.botao_22.configure(text = "O")
                self.muda_jogador()
                self.verifica_vencedor()
            
     #   recebe_jogada(2,2)
    def botao_02clicado(self):
        if (self.B_02_clicado == False):
            if (self.venceu==False):
                self.B_02_clicado = True
                self.clique(0,2)
                if(self.jogador==1):
                    self.botao_02.configure(text = "X")
                else:
                    self.botao_02.configure(text = "O")
                self.muda_jogador()
                self.verifica_vencedor()
            
      #  recebe_jogada(0,2)

    def iniciar(self):
        self.window.mainloop()
        
    def reiniciar (self):
            self.B_00_clicado = False
            self.botao_00.configure(text = "")
            self.B_10_clicado = False
            self.botao_10.configure(text = "")
            self.B_20_clicado = False
            self.botao_20.configure(text = "")
            self.B_11_clicado = False
            self.botao_11.configure(text = "")
            self.B_12_clicado = False
            self.botao_12.configure(text = "")
            self.B_01_clicado = False
            self.botao_01.configure(text = "")
            self.B_02_clicado = False
            self.botao_02.configure(text = "")
            self.B_22_clicado = False
            self.botao_22.configure(text = "")
            self.B_21_clicado = False
            self.botao_21.configure(text = "")
            self.venceu=False
            self.jogador=1
            self.label_vez.configure(text='Vez do: Jogador 1')
            
    def muda_jogador(self):
        if (self.jogador==1):
            self.label_vez.configure(text='Vez do: Jogador 2')
            self.jogador = 2
                    
        elif(self.jogador==2):
            self.label_vez.configure(text='Vez do: Jogador 1')
            self.jogador= 1
            
    def X_vencedor (self):
        self.label_vez.configure(text='Vencedor: Jogador 1')
        self.venceu=True
        
    def Y_vencedor (self):
         self.label_vez.configure(text='Vencedor: Jogador 2')
         self.venceu=True
         
    def verifica_vencedor (self):
      
        if (self.botao_00["text"] =="X" and  self.botao_01["text"] =="X" and  self.botao_02["text"] =="X") or (self.botao_00["text"] =="X" and  self.botao_10["text"] =="X" and  self.botao_20["text"] =="X") or (self.botao_00["text"] =="X" and  self.botao_11["text"] =="X" and  self.botao_22["text"] =="X") or (self.botao_10["text"] =="X" and  self.botao_11["text"] =="X" and  self.botao_12["text"] =="X") or (self.botao_20["text"] =="X" and  self.botao_21["text"] =="X" and  self.botao_22["text"] =="X") or (self.botao_01["text"] =="X" and  self.botao_11["text"] =="X" and  self.botao_21["text"] =="X") or (self.botao_02["text"] =="X" and  self.botao_12["text"] =="X" and  self.botao_22["text"] =="X") or (self.botao_02["text"] =="X" and  self.botao_11["text"] =="X" and  self.botao_20["text"] =="X")  :
            self.X_vencedor () 
            
                               
        elif (self.botao_00["text"] =="O" and  self.botao_01["text"] =="O" and  self.botao_02["text"] =="O") or (self.botao_00["text"] =="O" and  self.botao_10["text"] =="O" and  self.botao_20["text"] =="O") or (self.botao_00["text"] =="O" and  self.botao_11["text"] =="O" and  self.botao_22["text"] =="O") or (self.botao_10["text"] =="O" and  self.botao_11["text"] =="O" and  self.botao_12["text"] =="O") or (self.botao_20["text"] =="O" and  self.botao_21["text"] =="O" and  self.botao_22["text"] =="O") or (self.botao_01["text"] =="O" and  self.botao_11["text"] =="O" and  self.botao_21["text"] =="O") or (self.botao_02["text"] =="O" and  self.botao_12["text"] =="O" and  self.botao_22["text"] =="O") or (self.botao_02["text"] =="O" and  self.botao_11["text"] =="O" and  self.botao_20["text"] =="O")  :
            self.Y_vencedor () 
            
            
        elif (self.B_00_clicado == True) and (self.B_01_clicado == True) and (self.B_02_clicado == True) and (self.B_10_clicado == True) and (self.B_11_clicado == True) and (self.B_12_clicado == True) and (self.B_20_clicado == True) and (self.B_21_clicado == True) and (self.B_22_clicado == True):
            self.label_vez.configure(text='Deu Velha!')
            self.venceu=True 
           
        
        

class Jogo:
    def __init__(self):
        import tabuleiro
        #self.jogador=1
app = tabuleiro ()
app.iniciar()