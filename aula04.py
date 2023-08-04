
'''for i in range (3):
    numero = int(input("Digite o numero :"))

    if numero > numeroMaior:
        numeroMaior = numero
print (f"O maior número é : {numeroMaior}")'''

'''numeroMaior =0 
contador = 0

while contador <= 2:
    numero = int(input(f"Digite o {contador + 1} numero :"))

    if numero > numeroMaior:
        numeroMaior = numero
    
    contador += 1
print (f"O maior número digitado é : {numeroMaior}")'''
numeroMaior =0 
contador = 0

while True:
    numero = int(input(f"Digite o {contador + 1} numero :"))

    if numero > numeroMaior:
        numeroMaior = numero
    
    contador += 1

    if contador == 3:
        break
print (f"O maior número digitado é : {numeroMaior}")