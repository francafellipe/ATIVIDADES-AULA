from divisão import divisão
from multiplicação import multiplicação
from soma import soma
from subtração import subtração
while True:
    escolha = int(input('Bem vindo a calculadora, escolha o que deseja fazer ?\n'
                        '1 - Divisão \n'
                        '2 - Multiplicação \n'
                        '3 - Soma \n'
                        '4 - Subtração \n'
                        '0 - Encerrar '))

    if escolha == 1:
        divisão()

    if escolha == 2:
        multiplicação()

    if escolha == 3:
        soma()

    if escolha == 4:
        subtração()

    if escolha == 0:
        break
    else :
        print('Opção invalida')
