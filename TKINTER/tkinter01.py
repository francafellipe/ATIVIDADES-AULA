'''from tkinter import *
def cadastrar ():
    nome = Button (janela, text= 'Nome : ')
    matricula = Button(janela, text='Digite a matricula do aluno :')
    alunos[matricula]=nome.lower()
def remover ():
    matricula = input('Digite o número da matricula :')
    alunos.pop(matricula)

def visualizar ():
    print("Lista de alunos:")
    for matricula, nome in alunos.items():
        print(f'Matrícula: {matricula}\n '
              f'Nome: {nome}')
def finalizar():
    print("Cadastro Encerrado")

alunos = {}
    
janela = Tk()
#widgets

titulo = Label(text=" Cadastro de alunos",
               fg="red",
               bg="white")
titulo.pack()
#labels

#entrys


#botoes
cadastraraluno = Button(janela,text="Cadastrar aluno ?", command=cadastrar )
cadastraraluno.pack()
visualizaralunos = Button(janela,text="Visualizar dados dos alunos ?", command= visualizar)
visualizaralunos.pack()
apagaralunos = Button(janela,text= "Apagar aluno cadastrado ", command= remover)
apagaralunos.pack()
finalizarprograma = Button(janela,text="Finalizar Cadastro !")
finalizarprograma.pack()

#localização



janela.mainloop()
#fimalgoritmo'''

from tkinter import Tk,Label, Entry,Button

def cadastrar():
    print(f"O aluno de nome {nome.get()}, tem {idade.get()} anos e tirou nota {nota.get()}")

    nome.delete(0, "end")
    idade.delete(0, "end")
    nota.delete(0, "end")

janela = Tk()

l_nome = Label(janela, text= "Nome: ")
l_nome.pack()

nome = Entry(janela)
nome.pack()

l_idade = Label(janela, text= "Idade: ")
l_idade.pack()

idade = Entry(janela)
idade.pack()