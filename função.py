'''def fatorial(numero):
    acumulador = 1
    expressão = f"{numero} "
    # for i in range(1, numero + 1):
    #     acumulador *= i

    for i in range(numero, 0, -1):
        acumulador *= i

        if i != numero:
            expressão += f"* {i} "

    expressão += f"= {acumulador}"

    return expressão

numero = int(input('Digite um numero inteiro e positivo: '))

print(fatorial(numero))'''

'''def pessoa ():
    idade = int(input('Digite sua idade: '))

    return idade

nascimento = 2023 - pessoa()

print (f'Você nasceu em : {nascimento}')'''
def janela(altura=50, largura=50,cor = "Branca",fullscreen =False):
    print(altura,largura,cor,fullscreen)

janela(altura=180,fullscreen=True)


#(*args) permite receber uma quantidade variável de parâmetros posicionais 
#(*kwargs) permite receber parâmetros nomeados 

