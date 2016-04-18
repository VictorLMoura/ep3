#Criando o tabuleiro
import tkinter as tk

#CRIANDO OS BOTOES    
window = tk.Tk()

botao_00 = tk.Button (window) #00 é a localização do botao esse no caso é o superior esquerdo
botao_00.grid()

botao_01 = tk.Button (window)
botao_01.grid()

botao_02 =tk.Button (window)
botao_02.grid ()

botao_10=tk.Button (window)
botao_10.grid()

botao_20=tk.Button (window)
botao_20.grid()

botao_11=tk.Button (window)
botao_11.grid()

botao_21=tk.Button (window)
botao_21.grid()

botao_12=tk.Button (window)
botao_12.grid()

botao_22 = tk.Button (window)
botao_22.grid()

window.mainloop()