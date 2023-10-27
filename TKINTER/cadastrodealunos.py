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
def finalizar():
    print("Cadastro Encerrado")
    

#fimalgoritmo