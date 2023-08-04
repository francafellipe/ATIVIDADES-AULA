nNotas = int(input("Digite a quantidade de notas :"))
soma = 0

for i in range (nNotas):
    numero = float (input("Digite a nota :"))

    soma += numero
media = soma / nNotas

print(f"a soma das notas é : {soma}, e a media das notas é : {media:.1f}")
