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

     self.quintoContainer = Frame(master)
     self.quintoContainer["pady"] = 10
     self.quintoContainer.pack()

     self.sextoContainer = Frame(master)
     self.sextoContainer["padx"] = 20
     self.sextoContainer.pack()
     
     self.setimoContainer = Frame(master)
     self.setimoContainer["padx"] = 20
     self.setimoContainer.pack()
     
     self.oitavoContainer = Frame(master)
     self.oitavoContainer["pady"] = 30
     self.oitavoContainer.pack()



     self.lblNumeroMaximo =Label(self.primeiroContainer, text="Digite o número de pessoas a ser sorteado !!")
     self.lblNumeroMaximo["font"] = ("Arial", "15", "bold")
     self.lblNumeroMaximo.pack()
 
     self.numeroMaximo = Entry(self.segundoContainer)
     self.numeroMaximo["width"] = 30
     self.numeroMaximo["font"] = self.fontePadrao
     self.numeroMaximo.pack(side=LEFT) 
 
     self.resultado = Label(self.terceiroContainer, text='')
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
        
        self.resultado["background"] = "aqua"
        ValorNumeroMaximo = int(self.numeroMaximo.get())
        print(ValorNumeroMaximo)
        nomes = ["Fernando","Emerson","Vanderlei",
         "Gabriela","Fefê","Paulo","João","Carol","Flávia"] # VETOR
        if (ValorNumeroMaximo>len(nomes)):
           self.resultado["text"] = "Digite uma quantia menor"
        
        else:
            nomeSorteados = ""
            for p in range(0,ValorNumeroMaximo):
                print(p)
                self.resultado["background"] = "red"
                for c in range(0,10):
                    self.resultado["text"] = nomes[random.randint(0,len(nomes) -1)]
                    self.terceiroContainer.update()
                    time.sleep(0.2)
                self.resultado["background"] = "aqua"
                nomeSorteados += "\n" + self.resultado["text"]
                print(nomeSorteados)
                nomes.remove(self.resultado["text"])
                self.terceiroContainer.update()
                time.sleep(2)
            self.resultado["background"] = "grey"
            self.resultado["text"] = nomeSorteados
            self.terceiroContainer.update()

        

root = Tk()
Application(root)
root.mainloop()