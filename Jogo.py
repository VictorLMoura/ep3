class Jogo:
    def __init__(self):
        self.jogador=1
        self.venceu = False
      
    def muda_jogador(self):
      if (self.jogador==1):
          self.jogador = 2
                       
      elif(self.jogador==2):
          self.jogador= 1
                
    def X_vencedor (self):
      self.label_vez.configure(text='Vencedor: Jogador 1')
      self.venceu=True
        
    def Y_vencedor (self):
      self.label_vez.configure(text='Vencedor: Jogador 2')
      self.venceu=True
    
    def Velha (self):
      self.venceu=True
         
    def verifica_vencedor (self):
      
      if (self.botao_00["text"] =="X" and  self.botao_01["text"] =="X" and  self.botao_02["text"] =="X") or (self.botao_00["text"] =="X" and  self.botao_10["text"] =="X" and  self.botao_20["text"] =="X") or (self.botao_00["text"] =="X" and  self.botao_11["text"] =="X" and  self.botao_22["text"] =="X") or (self.botao_10["text"] =="X" and  self.botao_11["text"] =="X" and  self.botao_12["text"] =="X") or (self.botao_20["text"] =="X" and  self.botao_21["text"] =="X" and  self.botao_22["text"] =="X") or (self.botao_01["text"] =="X" and  self.botao_11["text"] =="X" and  self.botao_21["text"] =="X") or (self.botao_02["text"] =="X" and  self.botao_12["text"] =="X" and  self.botao_22["text"] =="X") or (self.botao_02["text"] =="X" and  self.botao_11["text"] =="X" and  self.botao_20["text"] =="X")  :
       self.X_vencedor ()   
         
            
                                
      elif (self.botao_00["text"] =="O" and  self.botao_01["text"] =="O" and  self.botao_02["text"] =="O") or (self.botao_00["text"] =="O" and  self.botao_10["text"] =="O" and  self.botao_20["text"] =="O") or (self.botao_00["text"] =="O" and  self.botao_11["text"] =="O" and  self.botao_22["text"] =="O") or (self.botao_10["text"] =="O" and  self.botao_11["text"] =="O" and  self.botao_12["text"] =="O") or (self.botao_20["text"] =="O" and  self.botao_21["text"] =="O" and  self.botao_22["text"] =="O") or (self.botao_01["text"] =="O" and  self.botao_11["text"] =="O" and  self.botao_21["text"] =="O") or (self.botao_02["text"] =="O" and  self.botao_12["text"] =="O" and  self.botao_22["text"] =="O") or (self.botao_02["text"] =="O" and  self.botao_11["text"] =="O" and  self.botao_20["text"] =="O")  :
         self.Y_vencedor () 
            
            
      elif (self.B_00_clicado == True) and (self.B_01_clicado == True) and (self.B_02_clicado == True) and (self.B_10_clicado == True) and (self.B_11_clicado == True) and (self.B_12_clicado == True) and (self.B_20_clicado == True) and (self.B_21_clicado == True) and (self.B_22_clicado == True):
         self.label_vez.configure(text='Deu Velha!')
         self.venceu=True 
           