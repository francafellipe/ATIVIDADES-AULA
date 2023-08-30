'''Desafio: crie um sistema integrado para cadastro de pacientes num hospital, onde terá 3 opções de ação

1 - cadastrar paciente, onde terá como chave no dicionario um id que se autoincrementará ao cadastrar um novo paciente, e o valor será uma lista com as seguintes informações: nome, idade, peso e altura

2 - Ver todos os pacientes

3 - Apagar paciente

0 - Finalizar sistema
'''
#Algoritmo : Cadastro de Hospital 
#variaveis

id_paciente = 1
lista_pacientes = {}

#inicio
while True:
    escolha = int(input('Olá, o que quer fazer agora ? \n'
                        'Digite 1 para cadastrar novo paciente. \n'
                        'Digite 2 para consultar lista de pacientes.\n'
                        'Digite 3 para excluir algum cadastro.\n'
                        'Digite 0 , para finalizar o programa.\n'))
    match escolha:
        case 1 :
            nome = input('Digite o nome do paciente : ')
            idade = int(input('Idade : '))
            peso = float(input('Peso em kg : '))
            altura = float(input('Altura em cm : '))

            lista_pacientes[id_paciente] = nome.lower(),idade , peso , altura #cria chave nova + acrescenta os valores
            id_paciente+=1
            print('Cadastro finalizado !')
        case 2 :

            for matricula in lista_pacientes:
                valores = lista_pacientes.get(matricula)
                
                print (f'Matricula : {matricula}')# aprender como concatenar 
                print (f'Nome : {valores[0]}')# precisa mostrar o numero da matricula de cada usuario 'ok'
                print (f'Idade : {valores[1]} Anos')
                print (f'Peso : {valores[2]} Kg')
                print (f'Altura : {valores[3]} cm ')
                
        case 3 :
            id_paciente = int(input('Digite o numero do cadastro para excluir : '))
            del (lista_pacientes[id_paciente]) #faltava chamar o dicionario e especificar a chave []
                
        case 0 :
            print('Fim da pagina de cadastros !')
            break
        

#fimalgoritmo