import tkinter as tk
import Jogo
class Tabuleiro:
    def __init__(self):
        self.jogo=Jogo.Jogo()
        self.window = tk.Tk()
        self.window.title("Jogo da Velha!")
        self.window.geometry("400x400")
        self.window.rowconfigure(0, minsize=100,weight=1)
        self.window.rowconfigure(1,minsize=100,weight=1)
        self.window.rowconfigure(2, minsize=100,weight=1)
        self.window.rowconfigure(4, minsize=50,weight=1)
        self.window.columnconfigure(0, minsize=100,weight=1)
        self.window.columnconfigure(1, minsize=100,weight=1)
        self.window.columnconfigure(2, minsize=100,weight=1)
        
        
        self.botao_00 = tk.Button (self.window) 
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

        self.botao_reiniciar = tk.Button (self.window)
        self.botao_reiniciar.grid (row=4, column = 1, sticky = "nsew")  
        self.botao_reiniciar.configure (text = "Reiniciar")
        self.botao_reiniciar.configure(font="Courier 14 bold")
        self.botao_reiniciar.configure(command= self.reiniciar)

        self.label_vez = tk.Label(self.window)
        self.label_vez.configure(font="Courier 14 bold")
        self.label_vez.grid(row = 3, column = 0, columnspan=3)
        self.label_vez.configure(text='Vez do: Jogador 1')        
        
    def clique (self, i, j):
        if (self.jogo.jogador==1):
            self.label_vez = tk.Label(self.window)
            self.label_vez.configure(font="Courier 14 bold")
            self.label_vez.grid(row = 3, column = 0, columnspan=3)
            self.label_vez.configure(text='Vez do: Jogador 2')
        elif (self.jogo.jogador==2):
            self.label_vez = tk.Label(self.window)
            self.label_vez.configure(font="Courier 14 bold")
            self.label_vez.grid(row = 3, column = 0, columnspan=3)
            self.label_vez.configure(text='Vez do: Jogador 1')
        if (self.jogo.venceu == 1):
            self.label_vez.configure(text='Vencedor: Jogador 1')
        elif (self.jogo.venceu == 2):
            self.label_vez.configure(text='Vencedor: Jogador 2')
        elif (self.jogo.venceu == 3):
            self.label_vez.configure(text='Deu Velha')
        
    def botao_00clicado(self):
        if (self.jogo.B_00_clicado == 0):
            if (self.jogo.venceu==0):
                if(self.jogo.jogador==1):
                    self.jogo.B_00_clicado = 1
                    self.botao_00.configure(text = "X")
                else:
                    self.jogo.B_00_clicado = 2
                    self.botao_00.configure(text = "O")
                self.jogo.muda_jogador()
                self.jogo.verifica_vencedor()
                self.clique(0,0)
            
    def botao_01clicado(self):
        if (self.jogo.B_01_clicado == 0):
            if (self.jogo.venceu==0):
                if(self.jogo.jogador==1):
                    self.jogo.B_01_clicado = 1
                    self.botao_01.configure(text = "X")
                else:
                    self.jogo.B_01_clicado = 2
                    self.botao_01.configure(text = "O")
                self.jogo.muda_jogador()
                self.jogo.verifica_vencedor()
                self.clique(0,1)

    def botao_10clicado(self):
        if (self.jogo.B_10_clicado == 0):
            if (self.jogo.venceu==0):
                if(self.jogo.jogador==1):
                    self.jogo.B_10_clicado = 1
                    self.botao_10.configure(text = "X")
                else:
                    self.jogo.B_10_clicado = 2
                    self.botao_10.configure(text = "O")
                self.jogo.muda_jogador()
                self.jogo.verifica_vencedor()
                self.clique(1,0)

    def botao_20clicado(self):
        if (self.jogo.B_20_clicado == 0):
            if (self.jogo.venceu==0):
                if(self.jogo.jogador==1):
                    self.jogo.B_20_clicado = 1
                    self.botao_20.configure(text = "X")
                else:
                    self.jogo.B_20_clicado = 2
                    self.botao_20.configure(text = "O")
                self.jogo.muda_jogador()
                self.jogo.verifica_vencedor()
                self.clique(2,0)
                
    def botao_11clicado(self):
        if (self.jogo.B_11_clicado == 0):
            if (self.jogo.venceu==0):
                if(self.jogo.jogador==1):
                    self.jogo.B_11_clicado = 1
                    self.botao_11.configure(text = "X")
                else:
                    self.jogo.B_11_clicado = 2
                    self.botao_11.configure(text = "O")
                self.jogo.muda_jogador()
                self.jogo.verifica_vencedor()
                self.clique(1,1)
                
    def botao_12clicado(self):
        if (self.jogo.B_12_clicado == 0):
            if (self.jogo.venceu==0):
                if(self.jogo.jogador==1):
                    self.jogo.B_12_clicado = 1
                    self.botao_12.configure(text = "X")
                else:
                    self.jogo.B_12_clicado = 2
                    self.botao_12.configure(text = "O")
                self.jogo.muda_jogador()
                self.jogo.verifica_vencedor()
                self.clique(1,2)                
                
    def botao_21clicado(self):
        if (self.jogo.B_21_clicado == 0):
            if (self.jogo.venceu==0):
                if(self.jogo.jogador==1):
                    self.jogo.B_21_clicado = 1
                    self.botao_21.configure(text = "X")
                else:
                    self.jogo.B_21_clicado = 2
                    self.botao_21.configure(text = "O")
                self.jogo.muda_jogador()
                self.jogo.verifica_vencedor()
                self.clique(2,1)
                
    def botao_22clicado(self):
        if (self.jogo.B_22_clicado == 0):
            if (self.jogo.venceu==0):
                if(self.jogo.jogador==1):
                    self.jogo.B_22_clicado = 1
                    self.botao_22.configure(text = "X")
                else:
                    self.jogo.B_22_clicado = 2
                    self.botao_22.configure(text = "O")
                self.jogo.muda_jogador()
                self.jogo.verifica_vencedor()
                self.clique(2,2)
                
    def botao_02clicado(self):
        if (self.jogo.B_02_clicado == 0):
            if (self.jogo.venceu==0):
                self.clique(0,2)
                if(self.jogo.jogador==1):
                    self.jogo.B_02_clicado = 1
                    self.botao_02.configure(text = "X")
                else:
                    self.jogo.B_02_clicado = 2
                    self.botao_02.configure(text = "O")
                self.jogo.muda_jogador()
                self.jogo.verifica_vencedor()
                self.clique(0,2)
  
    def iniciar(self):
        self.window.mainloop()
        
    def reiniciar (self):
        self.botao_00.configure(text = "")
        self.botao_10.configure(text = "")
        self.botao_20.configure(text = "")
        self.botao_11.configure(text = "")
        self.botao_12.configure(text = "")
        self.botao_01.configure(text = "")
        self.botao_02.configure(text = "")
        self.botao_22.configure(text = "")
        self.botao_21.configure(text = "")
        self.jogo.limpar_jogada()
        self.jogo.venceu= 0
        self.jogo.jogador=1
        self.label_vez.configure(text='Vez do: Jogador 1')

app = Tabuleiro ()
app.iniciar()