def info(**kwargs):
    for chave, valor in kwargs.items():
        print(f'{chave} : {valor} ')

info(nome= "getulio" , idade = 22,altura = 1.25 , peso = 80)
#neste exemplo está criando a chave nome com o valor getulio, e a cada virgula se cria uma nova chave com novo valor.

'''def info(**kwargs): # aqui nos temos o identificador para cada valor
    if kwargs.get("nome", False) != False:
        print(f"Bem vindo {kwargs['nome']}")
    else:
        print("Bem vindo")


escolha = input("Você quer se indenficar?(s/n) ")

if escolha == "s":
    nome = input("Digite o seu nome: ")

    info(nome = nome)
else:
    info()'''