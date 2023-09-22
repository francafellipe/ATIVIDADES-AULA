#funções 
def cadastrar ():
    nome = input('Nome : ')
    matricula = input('Digite a matricula do aluno :')
    alunos[matricula]=nome.lower()
def remover ():
    matricula = input('Digite o número da matricula :')
    alunos.pop(matricula)

def visualizar ():
    print("Lista de alunos:")
    for matricula, nome in alunos.items():
        print(f'Matrícula: {matricula}\n '
              f'Nome: {nome}')
#var

alunos = {}

#inicio
while True:
    escolha = int(input('Escolha uma opção :\n'
                        '1 - Cadastrar novo aluno ?\n'
                        '2 - Visualizar dados dos alunos : \n'
                        '3 - Apagar aluno cadastrado :\n'
                        '0 - Finalizar cadastros .\n'))
    match escolha:
        case 1 :
            cadastrar()

        case 2 :
            visualizar()
        
        case 3 :
            remover()

        case 0 :
            print('Cadastro de alunos finalizado !')
            break
        
#fimalgoritmo
