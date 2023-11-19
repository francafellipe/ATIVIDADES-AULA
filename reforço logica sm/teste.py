# vamos importar o módulo Tkinter
from tkinter import *
from tkinter.ttk import *

# variáveis globais
caixa_texto = None

# método principal
def main():
  # acessamos a variável global
  global caixa_texto
  
  # vamos criar o frame principal da aplicação Tkinter
  janela = Tk()

  # agora definimos o tamanho da janela
  janela.geometry("600x400")

  # criamos uma caixa de texto Entry de linha única
  caixa_texto = Entry(janela, width=40)
  caixa_texto.grid(column=0, row=0, sticky=W, padx=15, pady=10)

  # vamos criar um botão Button
  btn = Button(janela, text="Limpar Texto", width=15, command=limpar_conteudo)
  btn.grid(column=1, row=0, sticky=W, pady=10)

  # entramos no loop da aplicação
  janela.mainloop()  

# função para limpar o conteúdo digitado na caixa de texto
def limpar_conteudo():
  # limpamos o conteúdo da caixa de texto Entry
  caixa_texto.delete(0, END)

if __name__== "__main__":
  main()
