from tkinter import *

mostrar = "" 

def adicionar(numero):
    global mostrar
    mostrar += str(numero)
    mostrar_resultado()

def soma():
    global mostrar
    mostrar += '+'
    mostrar_resultado()

def subtracao():
    global mostrar
    mostrar += '-'
    mostrar_resultado()

def mult():
    global mostrar
    mostrar += '*'
    mostrar_resultado()

def divisao():
    global mostrar
    mostrar += '/'
    mostrar_resultado()

def limpar():
    global mostrar
    mostrar += ""
    mostrar_resultado()

def mostrar_resultado():
    resultado['text'] = mostrar

def calcular_resultado():
    global mostrar
    try:
        resultado_final = eval(mostrar)
        resultado['text'] = "Resultado é: " + str(resultado_final)
        mostrar = str(resultado_final)
        mostrar = ''
    except Exception as e:
        resultado['text'] = "Erro"
        mostrar = ""

janela = Tk()
janela.title('Calculadora Fellipe')

# botões números
num1 = Button(janela, text='1', width=5, command=lambda: adicionar(1))
num1.grid(column=3, row=2)
num2 = Button(janela, text='2', width=5, command=lambda: adicionar(2))
num2.grid(column=4, row=2)
num3 = Button(janela, text='3', width=5, command=lambda: adicionar(3))
num3.grid(column=5, row=2)
num4 = Button(janela, text='4', width=5, command=lambda: adicionar(4))
num4.grid(column=3, row=3)
num5 = Button(janela, text='5', width=5, command=lambda: adicionar(5))
num5.grid(column=4, row=3)
num6 = Button(janela, text='6', width=5, command=lambda: adicionar(6))
num6.grid(column=5, row=3)
num7 = Button(janela, text='7', width=5, command=lambda: adicionar(7))
num7.grid(column=3, row=4)
num8 = Button(janela, text='8', width=5, command=lambda: adicionar(8))
num8.grid(column=4, row=4)
num9 = Button(janela, text='9', width=5, command=lambda: adicionar(9))
num9.grid(column=5, row=4)
num0 = Button(janela, text='0', width=5, command=lambda: adicionar(0))
num0.grid(column=4, row=5)

# botões comandos
botao_soma = Button(janela, text='+', command=soma)
botao_soma.grid(column=6, row=1)
botao_subtracao = Button(janela, text='-', command=subtracao)
botao_subtracao.grid(column=6, row=2)
botao_mult = Button(janela, text='x', command=mult)
botao_mult.grid(column=6, row=3)
botao_div = Button(janela, text='/', command=divisao)
botao_div.grid(column=6, row=4)
botao_igual = Button(janela, text='=', command=calcular_resultado)
botao_igual.grid(column=6, row=5)
botao_limpar = Button(janela,text='Limpar',command=limpar)
botao_limpar.grid(column = 6,row=6)

resultado = Label(janela, text='Resultado é:')
resultado.grid(column=3, row=1)

janela.mainloop()