from tkinter import *
def calcularimc ():
    imc = float(entrypeso.get()) / (float(entryaltura.get()) ** 2)
    if imc < 18.8 :
        mostrarresultadolabel.config(text= f"{entrynome.get()} seu IMC é {imc:.2f} \n e você esta abaixo do peso ")

    elif 18.6 > imc < 24.9 :
        mostrarresultadolabel.config(text=f"{entrynome.get()} seu IMC é {imc:.2f} , \n Peso ideal parabéns")

    elif 25 > imc < 29.9 :
        mostrarresultadolabel.config(text=f"{entrynome.get()} seu IMC é {imc:.2f} , \n Levemente acima do peso ")

    elif 30 > imc < 34.9 :
        mostrarresultadolabel.config(text=f"{entrynome.get()} seu IMC é {imc:.2f} , \n Obesidade grau 1")

    elif 35 > imc < 39.9 :
        mostrarresultadolabel.config(text=f"{entrynome.get()}seu IMC é {imc:.2f} , \n Obesidade grau 2 (severa)")

    elif imc > 40 :
        mostrarresultadolabel.config(text =f"{entrynome.get()} seu IMC é {imc:.2f} , \n Obesidade grau 3 morbida ")

    entrynome.delete(0,END)
    entryaltura.delete(0,END)
    entrypeso.delete(0,END)

janela = Tk()
janela.title("Calcular imc")


labelnome = Label(janela,text= "Digite o nome : ",font="bold" )
labelnome.pack()
entrynome = Entry(janela)
entrynome.pack()
labelpeso = Label(janela, text= "Qual o seu peso : ",font="bold")
labelpeso.pack()
entrypeso = Entry (janela)
entrypeso.pack()
labelaltura = Label (janela, text='Qual a sua altura : ',font="bold")
labelaltura.pack()
entryaltura = Entry(janela)
entryaltura.pack()

botaocalc = Button (janela, text= "Calcular IMC ",command= calcularimc,font="bold")
botaocalc.pack() 

mostrarresultadolabel = Label (janela , text= "O seu IMC é ",font="bold")
mostrarresultadolabel.pack()

janela.mainloop()