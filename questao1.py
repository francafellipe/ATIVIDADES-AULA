#1°: Faça um programa que verifique e mostre os números entre 1.000 e 2.000 (inclusive) que, quando divididos por 11 produzam resto igual a 2.

'''for i in range (1000,2001):
    if i % 11 == 2 :
        print (i)
'''
'''numero = int(input("Digite um numero inteiro :"))

for i in range (1,numero+1):
    if i % 2 == 0:
        print (f"O numero {i} é par ")

for i in range (1,numero+1):
    if i % 2 != 0:
        print (f'O numero {i} é impar ')
'''
velhos = 0
acumuladorAltura = 0
porcentagem = 0
quantidade_de_pessoas_entre_10_20 = 0
quantidade_de_pessoasmagras = 0
for i in range (5):
    idade = int(input("Digite a Idade "))
    altura = int (input("Digite a Altura"))
    peso  = int (input("Digite o peso"))
    
    if idade > 50:
        velhos += 1

    if  10 < idade < 20 :
        acumuladorAltura += altura 
        quantidade_de_pessoas_entre_10_20 += 1

    if peso < 40 :
        quantidade_de_pessoasmagras +=1
        porcentagem = quantidade_de_pessoasmagras / 100

media = acumuladorAltura / quantidade_de_pessoasmagras

print (f"a quantidade de velhos é {velhos}") 
print (f"a media das alturas das pessoas com idade entre 10 e 20 é : {media}")
print (f"A porcentagem das pessoas com peso inferior a 40 kg é :{porcentagem}")
    

    
https://github.com/infinity-repositorios/atividades/blob/main/Atividades/Python/aula1.md