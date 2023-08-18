'''lista = [1,2,3,4,5,6,7,8,9,10,11,12]

x = lista [int(input('Qual posição inicial da soma'))]
y = lista [int(input('Qual posição final da soma'))]

print (x+y)
'''

lista = []
contagem = 0
while True :
    numero = int(input('Digite um numero :'))
    if numero %2 != 0 :
        lista.append (numero)
        contagem+=1

    if contagem == 10:
        break
lista.sort()
print (lista)
