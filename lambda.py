from functools import reduce
'''lambda a, b, c : a +b +c 

print((lambda x, y: x * y)(y=5,x=7)) #função lambda , parametros x,y recebem os valores e realiza a multiplicação e retorna o resultado 

a = (lambda *args: sum(args))(7,5,6,7,8) # sum = soma de tudo que tem dentro de args

print(a)

soma = lambda *args: sum(args)

print(soma(7,8,9,5,6,2))
'''
'''numero_par = lambda x: "par" if x % 2 == 0 else "impar" # numero par recebe função lambda de parametro x com valor "par" se x 
num = int(input('Digite um numero : '))
print(numero_par(num))
'''
#https://www.canva.com/design/DAFt2p_SjMg/PBZjAsiPq0He3a2VQjSwDg/view?utm_content=DAFt2p_SjMg&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink#30
'''numeros = [8, 6, 10, 1.5, 4]

quadrados = list(map(lambda x: x ** 2,numeros))

print(quadrados)'''
'''
def quadrados(x):
    return x ** 2

numeros = [8, 6, 10, 1.5, 4]

numeros_quadrados = list(map(quadrados, numeros))
'''
'''print(numeros_quadrados)

numero = [7, 3, 5, 12, 9]

impar = list(filter(lambda x: x % 2 != 0, numero))

print(impar)'''
'''def quadrados(x):
    return x ** 2

numeros = [8, 6, 10, 1.5, 4]

numeros_quadrados = list(map(quadrados, numeros))

for i in numeros:
    numeros_quadrados.append(i ** 2)

print(numeros_quadrados)'''

'''numero = [15,8,5,4,3,8]

soma = reduce(lambda x,y : x+y , numero)

print(soma)'''

'''strings = ["a" , "b ", " c" , "d "]

maiusculas = list(map(lambda x: x.upper(),strings))# variavel recebe lista que o map percorre a lista de strings e cada x se aplica o upper


print (maiusculas)'''

palavras =  ["abecedario","joao","maria","escorregador","cenario","alto"]

maioresDeCinco = list(filter(lambda x : len(x) < 4  ,palavras))

print (maioresDeCinco)

contatenar = lambda x, y: (x + y #função lambda recebe dois parametros 
                           if len(x) >= 5 and len(y) >= 5 else #so vao se juntar se a primeira palavra tiver + de 5 caracteres
                           "Palavras com menos de 5 caracteres")#

print(contatenar("pão","almoço"))