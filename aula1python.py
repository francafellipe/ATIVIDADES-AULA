'''lista = [1,'dois',2.5,True]
print 

lista_numerica = [1,2,3,4,5,6,7,8,9,10]

lista_numerica [3] = "Jas"

print (lista_numerica)

print (lista_numerica[5])

print (lista_numerica[1:7:1])

print (lista_numerica[:4])

print (lista_numerica[4:])

print (lista_numerica[7:0:-1])'''

'''lista_letras = ["a", 'b', 'c', 'd', 'e' , 'f']

for i in lista_letras:
    if i not in ['c','d','e']:
        print(i)

       append( )

Insere um novo valor a lista, mas apenas no final.

insert( )

Insere um valor na lista em uma posição especifica.

pop( )

Irá apagar o ultimo valor se não passar uma posição, e se passado uma posição apaga um valor especifico.

del( )

Mesma função do pop, as apaga um intervalo de valores.

remove( )

Remove um valor especifico.

sort( )

Ordena toda a lista, se tiver um tipo de valor (str, int ou float).

clear( )

Limpa a lista.

len( )

Devolve a quantidade de itens na lista. 

reverse()

Inverte a ordem dos elementos na lista.'''

'''lista_nomes =['alice','carlos','maria','Pedro']

lista_nomes.append('John')
#adiciona o nome John ao final

lista_nomes.insert(0, 'Kleber')
#adiciona o nome Kleber na posição 0 da lista
print(lista_nomes)'''

'''lista_nomes = list()

for i in range (5):
    nome = input('Digite um nome: ')

    lista_nomes.append(nome)

print(lista_nomes)'''
import random

lista_nomes = list()
while True:
    escolha = int(input('Escolha uma das opções:\n'+
                        '1 - Adicionar um novo nome? \n'+
                        '2 - Vizualizar todos os nomes. \n'+
                        '3 - Vizualizar uma posição especifica ? \n'+
                        '4 - Excluir um nome \n'+
                        '5 - Reordenar a lista\n'+
                        '6 - Sortear um nome .\n'+
                        '0 - Finalizar o programa .\n'))
    
    match escolha:

        case 1 : 
            nome = input('Digite um nome: ')
            

            lista_nomes.append(nome.lower)

        case 2 :

            print(lista_nomes)

        case 3 :
            posicao = int(input('Digite a posição:'))

            print( f'O nome na posição {posicao} é igual á {lista_nomes[posicao - 1]}' if posicao -1 <len(lista_nomes) else 'Posição maior que a lista')
        
        case 4 :
            nome = input ('Digite o nome ')
            if nome in lista_nome:
                lista_nome.remove(nome.lower())
            else:
                print("Nome inexistente")
        case 5 :
            lista_nomes.sort()
        case 6 :
           print(random.choice(lista_nomes))

        case 0 :
            print('Fim da lista de nomes')
            break

        case _:
            print('Opção invalida')

'''
lista_nomes = ['aa','bb','cc','dd','ee','ff','gg']

lista_nomes.pop(2)

del(lista_nomes[1:3])

lista_nomes.remove('gg')

print(lista_nomes)'''