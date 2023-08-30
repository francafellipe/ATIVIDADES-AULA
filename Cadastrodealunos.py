#var
alunos = {}
matricula = 101
#inicio
while True:
    escolha = int(input('Escolha uma opção :\n'
                        '1 - Cadastrar novo aluno ?\n'
                        '2 - Dados do aluno : \n'
                        '3 - Finalizar cadastros .\n'))
    match escolha:
        case 1 :
            nome = input('Nome : ')
            idade = input('Idade: ')
            sexo = input ('Sexo : ')
            matricula +=1
            alunos[nome.lower]=idade , sexo.lower(), matricula

        case 2 :
            aluno = input('De qual aluno quer saber os dados ? ')
            print (f'O {aluno} tem {[idade]} anos , é do sexo : {[sexo]} e a matricula é : {[matricula]} .')

        case 3 :
            print('Cadastro de alunos finalizado !')
            break
        
#fimalgoritmo