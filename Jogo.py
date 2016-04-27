class Jogo:
    def __init__(self):
        self.vencedor= 0
        self.limpar_jogada()
        
    def limpar_jogada(self):
        self.B_00_clicado = 0
        self.B_10_clicado = 0
        self.B_20_clicado = 0
        self.B_01_clicado = 0
        self.B_02_clicado = 0
        self.B_11_clicado = 0
        self.B_12_clicado = 0
        self.B_21_clicado = 0
        self.B_22_clicado = 0
        self.venceu= 0
        self.jogador=1
        
    def muda_jogador(self):
      if (self.jogador==1):
          self.jogador = 2
                       
      elif(self.jogador==2):
          self.jogador= 1
                
    def X_vencedor (self):
      self.venceu=1
      self.vencedor=1
      
    def Y_vencedor (self):
      self.venceu=2
      self.vencedor=2
     
    def Velha (self):
      self.venceu=3
      self.vencedor=3
         
    def verifica_vencedor (self):
      
      if (self.B_00_clicado==1 and  self.B_01_clicado==1 and  self.B_02_clicado==1) or (self.B_00_clicado==1 and  self.B_10_clicado==1 and  self.B_20_clicado==1) or (self.B_00_clicado==1 and  self.B_11_clicado==1 and  self.B_22_clicado==1) or (self.B_10_clicado==1 and  self.B_11_clicado==1 and  self.B_12_clicado==1) or (self.B_20_clicado==1 and  self.B_21_clicado==1 and  self.B_22_clicado==1) or (self.B_01_clicado==1 and  self.B_11_clicado==1 and  self.B_21_clicado==1) or (self.B_02_clicado==1 and  self.B_12_clicado==1 and  self.B_22_clicado==1) or (self.B_02_clicado==1 and  self.B_11_clicado==1 and  self.B_20_clicado==1)  :
          self.X_vencedor () 
         
      elif (self.B_00_clicado==2 and  self.B_01_clicado==2 and  self.B_02_clicado==2) or (self.B_00_clicado==2 and  self.B_10_clicado==2 and  self.B_20_clicado==2) or (self.B_00_clicado==2 and  self.B_11_clicado==2 and  self.B_22_clicado==2) or (self.B_10_clicado==2 and  self.B_11_clicado==2 and  self.B_12_clicado==2) or (self.B_20_clicado==2 and  self.B_21_clicado==2 and  self.B_22_clicado==2) or (self.B_01_clicado==2 and  self.B_11_clicado==2 and  self.B_21_clicado==2) or (self.B_02_clicado==2 and  self.B_12_clicado==2 and  self.B_22_clicado==2) or (self.B_02_clicado==2 and  self.B_11_clicado==2 and  self.B_20_clicado==2)  :
         self.Y_vencedor () 
            
      elif (self.B_00_clicado != 0) and (self.B_01_clicado != 0) and (self.B_02_clicado != 0) and (self.B_10_clicado != 0) and (self.B_11_clicado != 0) and (self.B_12_clicado != 0) and (self.B_20_clicado != 0) and (self.B_21_clicado != 0) and (self.B_22_clicado != 0):
         self.Velha()
           