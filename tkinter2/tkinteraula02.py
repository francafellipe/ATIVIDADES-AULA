'''from tkinter import *
from tkinter import ttk

class Application:
    def __init__(self):
        self.janela = Tk()
        self.janela.title("Janela Principal")

        self.notebook = ttk.Notebook(self.janela)

        self.guia1()
        self.guia2()
        self.guia3()

        self.notebook.pack(padx=10, pady=10)

        self.janela.mainloop()

    def guia1(self):
        guia1 = ttk.Frame(self.notebook)
        self.notebook.add(guia1, text="Guia 1")

        dias_semanas = ["Domingo", "Segunda", "Terça", 
                        "Quarta", "Quinta", "Sexta", "Sábado"]
        
        combobox = ttk.Combobox(guia1, values=dias_semanas)
        combobox.pack(padx=10, pady=10)
    
    def guia2(self):
        guia2 = ttk.Frame(self.notebook)
        self.notebook.add(guia2, text="Guia 2")

        self.label2 = Label(guia2, text="Label 2")
        self.entry = Entry(guia2)

        self.label2.pack(padx=10, pady=10)
        self.entry.pack(padx=10, pady=10)
    
    def guia3(self):
        guia3 = ttk.Frame(self.notebook)
        self.notebook.add(guia3, text="Guia 3")

        self.button = Button(guia3, text="Button 3")
        self.button.pack(padx=10, pady=10)

app = Application()'''
from tkinter import *
from tkinter import ttk
'''
def comeca_progesso():
    botao_iniciar.configure(state=DISABLED) # Desabilita o botão "Iniciar"
    preenche_progresso(0) # chama a função para preencher a barra de progresso

def preenche_progresso(value):
    barra_de_progresso["value"] = value # atualiza o valor de progresso da barra

    if value < 1000:
        value += 1
        janela.after(300, preenche_progresso,value) # chama a função recursivamente após 0.02 segundos
    else:
        botao_iniciar.configure(state=NORMAL) # Habilita o botão "Iniciar"

janela = Tk()
janela.title("Ex de Progressbar")

barra_de_progresso = ttk.Progressbar(janela, length= 1000,mode= "determinate")
barra_de_progresso.pack(pady=400)

botao_iniciar= ttk.Button(janela, text= "Play",command= comeca_progesso)
botao_iniciar.pack(pady=10)

janela.mainloop()'''
janela = Tk()
janela.title("Exemplo de Separador")

label1 = ttk.Label (janela, text="Texto 1")
label1.pack(pady=10)

separador = ttk.Separator(janela, orient= HORIZONTAL)
separador.pack(padx=50,ipadx=30)

label2 = ttk.Label(janela,text= "Texto 2")
label2.pack(pady=10)

janela.mainloop()


