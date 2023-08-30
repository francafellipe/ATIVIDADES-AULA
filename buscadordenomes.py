#var
dicio1 = {}

# inicio
while True:
    escolha = int(input('Escolha uma opção: \n'+
                        '1 - Novo Cadastro.\n'+
                        '2 - Buscar Usuario.\n'+
                        '3 - Finalizar .\n'))#declarei variavel escolha , tipo inteiro, e as opçoes para o match case
    match escolha: #caso em escolha seja digitado 
        case 1 :# caso digite 1 
            nome = input('Qual nome do usuario?')
            idade = input(f'Qual a idade do {nome} ')# pergunte qual o nome, pergunte qual a idade 
            dicio1[nome]= idade  #dicio1 recebe a chave 'Nome' e acrescenta o valor idade a chave 'nome'

        case 2 : #caso 2 para buscar o nome
                pessoa = input('De qual pessoa quer saber a idade ?')#pergunta de qual pessoa quer saber a idade ao usuario
                idade = dicio1.get(pessoa) #procura o valor idade dentro do dicinario 1 com a chave = ao nome 
                if idade is not None:# caso a idade seja invalida ou indefinida
                     print(f'A idade de {pessoa} e {idade}') #mostre a idade da pessoa se nao for indefinida.
                else:
                     print(f'O {pessoa} não foi encontrado')# caso não tenha o nome da pessoa como chave mostrei que nao foi encontrado
        case 3 :
            break
        case _:
            print('Opção invalida, escolha 1, 2 ou 3.')#caso digite algum numero diferente , o programa alerta que e invalido
#fimalgoritmo
 
'''dicio1['x']='Fellipe' # adiciona novo valor a chave 1
dicio1['idade']='20'
print (dicio1['idade'])
#fimalgoritmo'''