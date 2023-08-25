'''lista = list()

for i in range(5):
    lista.append(float(input("Digite um numero qualquer: ")))

    # if lista[i] < 0:
    #     lista[i] = 0
# definir um contador para definir a posição na lista
contador = 0

for i in lista:
    if i < 0:
        lista[contador] = 0
    
    contador += 1
# utilizar o metodo len para mostrar a quantidade de itens na lista
for i in range(0, len(lista)):
    if lista [i]<0:
        lista[i] = 0

print(lista)'''

'''# o que define os dicionarios são as ' { } '
#forma de organizar a lista
dicio1 = {"Fellipe": [27, "Masculino", 1.80 ], "Carla": }

print(dicio1["Fellipe"])
#forma de organizar a lista
dicio1 = {
    "Getulio": [22, "Masculino"], 
    "Carla": [30, "Feminino"],
    "Getulio": ["idade: 23", "sexo: Masculino", "altura: 1.80"]
}

print(dicio1["Getulio"])
#como trocar o valor de algum dicionario 
dicio1 = {
    "Getulio": [22, "Masculino"], 
    "Carla": [30, "Feminino"]
}
#chame a lista que quer trocar e coloque o novo valor
dicio1["Getulio"] = ["idade: 23", "sexo: Masculino", "altura: 1.80"]

print(dicio1["Getulio"]) '''

'''dicio4 ={'Chave1': input('Digite o valor da primeira chave'), 'Chave2' : 'Valor2'}

print(dicio4['Chave1'])'''
'''
clientes = dict()

while True:
    escolha = int(input("Digite uma opção:\n" + 
                        "1 - Novo Clientes\n" +
                        "2 - Ver Clientes Cadastrados\n" +
                        "0 - Finalizar Sistema\n"))
    
    match escolha:
        case 1:
            nome = input('Digite o nome do cliente: ')
            idade = int(input('Digite a idade do cliente : '))
            endereco = input ('Digite o endereço do cliente : ')

            clientes[nome] = [idade,endereco]


            print(f'Cliente {nome} Cadastrado com sucesso')

        case 2 : 
            print(clientes)

        case 0:
            print('Programa finalizado ')

clientes = dict()

num_cliente = 1
    
while True:
    escolha = int(input("Digite uma opção:\n" + 
                        "1 - Novo Clientes\n" +
                        "2 - Ver Clientes Cadastrados\n" +
                        "0 - Finalizar Sistema\n"))
    
    match escolha:
        case 1:
            nome = input("Digite o nome do cliente: ")
            idade = int(input("Digite a idade do cliente: "))
            peso = float(input("Digite o peso do cliente: "))
            altura = float(input("Digite a altura do cliente: "))

            clientes[num_cliente] = [nome, idade, peso, altura]

            num_cliente += 1

        case 2:

            print(clientes)
    '''
'''clientes = dict()

num_cliente = 1
    
while True:
    escolha = int(input("Digite uma opção:\n" + 
                        "1 - Novo Clientes\n" +
                        "2 - Ver Clientes Cadastrados\n" +
                        "3 - Procurar Cliente\n" +
                        "0 - Finalizar Sistema\n"))
    
    match escolha:
        case 1:
            nome = input("Digite o nome do cliente: ")
            idade = int(input("Digite a idade do cliente: "))
            peso = float(input("Digite o peso do cliente: "))
            altura = float(input("Digite a altura do cliente: "))

            clientes[num_cliente] = [nome, idade, peso, altura]

            num_cliente += 1

        case 2:
            for i in clientes:
                print(f"cliente {i} - {clientes[i]}")

        case 3:
            numero_cliente = int(input("Qual o numero do cliente: "))

            print(clientes[num_cliente][0])'''

'''dicio = {}

for i in range (5):
    dicio[i] = input(f'Digite o {i + 1 }º nome:')

print(dicio.get(5, "Não existe"))

print(dicio.pop(1, "Não existe"))
print(dicio)'''

#variaveis

'''dicionario1 = {}
numcliente = 1
while True:
    escolha = input('Digite uma opção:\n' +
                    '1 - Cadastrar o nome e idade da pessoa ?\n' +
                    '2 - Buscar a idade da pessoa ?\n' +
                    '3 - Finalizar programa.\n')
    
    match escolha:
        case 1 :
            nome = input('Digite o Nome da pessoa ')
            idade = input(f'Qual a idade da(o): {nome}')
            dicionario1[numcliente] = [nome][idade]
            numcliente += 1

        case 2 :
           idadePessoa = input('Qual o nome da pessoa que você quer saber a idade?')


        case 3 :
            print('Programa Finalizado .')
            break'''

dicionario1 = dict()

nom_pessoa = 1
    
while True:
    escolha = int(input("Digite uma opção:\n" + 
                        "1 -Cadastrar nome e idade da pessoa ?\n" +
                        "2 - Buscar idade da pessoa ?\n" +
                        "0 - Finalizar Sistema\n"))
    
    match escolha:
        case 1:
            nome = input("Digite o nome da pessoa: ")
            idade = int(input(f"{nome} tem quantos anos ?  "))

            dicionario1[nom_pessoa] = [nome, idade]

            nom_pessoa += 1

        case 2:
            for i in [dicionario1]:
                n1 = input('Qual o nome da  pessoa você quer saber a idade ?')
                print(dicionario1[n1][2])


       