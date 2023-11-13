import tkinter as tk
from tkinter import simpledialog

class Times:
    def __init__(self, nometime, cidadetime, mascotetime):
        self.nometime = nometime
        self.cidadetime = cidadetime
        self.mascotetime = mascotetime

class Jogadores:
    def __init__(self, nomejogador, numero, nometimejoga):
        self.nomejogador = nomejogador
        self.numerocamisa = numero
        self.nometimejoga = nometimejoga

class Comissao:
    def __init__(self, nome, time):
        self.nome = nome
        self.time = time

class Tecnico(Comissao):
    def __init__(self, nome, time, esquemat):
        super().__init__(nome, time)
        self.esquemat = esquemat


class Auxiliar(Comissao):
    def __init__(self, nome, time, esquematx):
        super().__init__(nome, time)
        self.esquematx = esquematx


class Preparador(Comissao):
    def __init__(self, nome, time, parte):
        super().__init__(nome, time)
        self.parte = parte


def cadastrar_time():
    nometime = simpledialog.askstring("Cadastrar Time", "Digite o nome do time:")
    cidadetime = simpledialog.askstring("Cadastrar Time", "O time é de qual cidade?")
    mascotetime = simpledialog.askstring("Cadastrar Time", "Qual o mascote do time?")
    time = Times(nometime, cidadetime, mascotetime)


def cadastrar_jogador():

    nomejogador = simpledialog.askstring("Cadastrar Jogador", "Qual é o nome do jogador?")
    numerocamisa = simpledialog.askinteger("Cadastrar Jogador", "Qual é o número da camisa?")
    nometimejoga = simpledialog.askstring("Cadastrar Jogador", "Em qual time o jogador atua?")
    jogador = Jogadores(nomejogador, numerocamisa, nometimejoga)
def coletiva_tecnico():
    janela = tk.Toplevel()
    janela.title("Coletiva do Técnico")
    label = tk.Label(janela, text="O técnico está dando coletiva")
    label.pack()

def coletiva_auxiliar():
    janela = tk.Toplevel()
    janela.title("Coletiva do Auxiliar")
    label = tk.Label(janela, text="O auxiliar está dando coletiva")
    label.pack()

def coletiva_preparador():
    janela = tk.Toplevel()
    janela.title("Coletiva do Preparador")
    label = tk.Label(janela, text="O preparador está dando coletiva")
    label.pack()
def dar_coletiva():
    while True:
        colet = simpledialog.askinteger('Coletiva de imprensa ','1 - Convidar técnico \n 2- Convidar auxiliar  \n3 - Convidar preparador \n4- Fim da coletiva ')
        if colet == 1:
            coletiva_tecnico()

        elif colet == 2:
            coletiva_auxiliar()

        elif colet == 3 :
            coletiva_preparador()

        elif colet == 4:
            break


def cadastrar_comissao():
    while True:
        escolha2 = simpledialog.askinteger("Cadastrar Comissão", "1 - Cadastrar técnico\n2 - Cadastrar auxiliar\n3 - Cadastrar preparador\n0 - Finalizar Cadastro da comissão")
        
        if escolha2 == 1:
            nometecnico = simpledialog.askstring("Cadastrar Técnico", "Qual é o nome do técnico?")
            timetreinador = simpledialog.askstring("Cadastrar Técnico", "Qual time ele treina?")
            esquemapreferidotec = simpledialog.askstring("Cadastrar Técnico", "Qual é o esquema tático preferido?")
            tec = Tecnico(nometecnico, timetreinador, esquemapreferidotec)
        

        if escolha2 == 2:
            nomeauxiliar = simpledialog.askstring("Cadastrar Auxiliar", "Qual é o nome do Auxiliar?")
            timeaux = simpledialog.askstring("Cadastrar Auxiliar", "Qual time o auxiliar treina?")
            esquemapreferidoaux = simpledialog.askstring("Cadastrar Auxiliar", "Qual é o esquema tático preferido?")
            aux = Auxiliar(nomeauxiliar, timeaux, esquemapreferidoaux)
            

        if escolha2 == 3:
            nomepreparador = simpledialog.askstring("Cadastrar Preparador", "Qual é o nome do preparador?")
            timepreparador = simpledialog.askstring("Cadastrar Preparador", "Qual time o preparador trabalha?")
            partepreparo = simpledialog.askstring("Cadastrar Preparador", "Qual parte do time é preparada?")
            prep = Preparador(nomepreparador, timepreparador, partepreparo)
            

        if escolha2 == 0:
            break

def menu():
    root = tk.Tk()
    root.title("Menu FIFA")
    root.geometry('500x400')

    button_cadastrar_time = tk.Button(root, text="Cadastrar novo time", command=cadastrar_time)
    button_cadastrar_time.pack()

    button_cadastrar_jogador = tk.Button(root, text="Cadastrar novo jogador", command=cadastrar_jogador)
    button_cadastrar_jogador.pack()

    button_cadastrar_comissao = tk.Button(root, text="Cadastrar comissão técnica", command=cadastrar_comissao)
    button_cadastrar_comissao.pack()

    button_darcoletiva = tk.Button(root, text= 'Coletiva de imprensa', command= dar_coletiva)
    button_darcoletiva.pack()

    button_sair = tk.Button(root, text="Finalizar menu", command=root.destroy)
    button_sair.pack()

    root.mainloop()

menu()
