agenda = {}

# inicio
while True:
    escolha = int(input('Escolha uma opção: \n'+
                        '1 - Cadastrar Novo telefone .\n'+
                        '2 - Buscar Numero de telefone.\n'+
                        '3 - Finalizar .\n'))#declarei variavel escolha , tipo inteiro, e as opçoes para o match case
    match escolha: #caso em escolha seja digitado 
        case 1 :# caso digite 1 
            nome = input('Qual nome do usuario ? ')
            telefone = input(f'Qual a número do {nome} ?')# pergunte qual o nome, pergunte qual o numero 
            agenda[nome.lower()]= telefone #agenda recebe a chave 'Nome' e acrescenta o valor idade a chave 'nome'

        case 2 : #caso 2 para buscar  o numero na agenda 
                individuo = input('De qual pessoa quer saber número ?')#pergunta de qual pessoa quer saber o numero ao usuario
                telefone = agenda.get(individuo.lower()) #procura o valor telefone dentro da agenda  com a chave = ao nome do individuo
                if telefone is not None:# caso o telefone seja invalido ou indefinida
                     print(f'{telefone} é o telefone do {individuo}') #mostrar o telefone da pessoa x 
                else:
                     print(f'O {individuo} não possui telefone cadastrado, deseja cadastrar ?')# caso não tenha o nome da pessoa como chave mostrei que nao foi encontrado
        case 3 :
            print('Fim do programa ')
            break
        case _:
            print('Opção invalida, escolha 1, 2 ou 3.')#caso digite algum numero diferente , o programa alerta que e invalido
#fimalgoritmo