import random
import time
from tkinter import *

class Application:
    def __init__(self, master=None):
     self.fontePadrao = ("Arial", "20")
     self.primeiroContainer = Frame(master)
     self.primeiroContainer["pady"] = 10
     self.primeiroContainer.pack()

     self.segundoContainer = Frame(master)
     self.segundoContainer["padx"] = 20
     self.segundoContainer.pack()
     
     self.terceiroContainer = Frame(master)
     self.terceiroContainer["padx"] = 20
     self.terceiroContainer.pack()
     
     self.quartoContainer = Frame(master)
     self.quartoContainer["pady"] = 30
     self.quartoContainer.pack()


     self.lblNumeroMaximo =Label(self.primeiroContainer, text="Digite o número máximo a ser sorteado")
     self.lblNumeroMaximo["font"] = ("Arial", "15", "bold")
     self.lblNumeroMaximo.pack()
 
     self.numeroMaximo = Entry(self.segundoContainer)
     self.numeroMaximo["width"] = 30
     self.numeroMaximo["font"] = self.fontePadrao
     self.numeroMaximo.pack(side=LEFT) 
 
     self.resultado = Label(self.terceiroContainer, text='Resultado:')
     self.resultado["width"] = 20
     self.resultado["font"] = self.fontePadrao
     self.resultado.pack(side=LEFT) 
    
     self.botao = Button(self.quartoContainer, text='SORTEAR')  
     self.botao["width"] = 20
     self.botao["font"] = self.fontePadrao
     self.botao["command"] = self.mudarTexto
     self.botao.pack(side=LEFT) 

    
    
    
    # FUNÇÃO PRINCIPAL
    
    def mudarTexto(self):

        ValorNumeroMaximo = int(self.numeroMaximo.get())
        self.resultado["background"] = "aqua"
        for c in range(0,10):
         self.resultado["text"] = random.randint(1,ValorNumeroMaximo)
         self.terceiroContainer.update()
         time.sleep(0.)
        self.resultado["background"] = "green"

root = Tk()
Application(root)
root.mainloop()