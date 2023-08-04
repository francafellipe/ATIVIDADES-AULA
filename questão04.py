soma = 0
contador = 0

while True : 
    nota = float(input("Digite a sua nota:"))

    if nota == 0:
        break

    soma += nota
    contador += 1

media = soma / contador

print (f"O valor da média é : {media}")