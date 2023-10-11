def cadastro (totalProdutos):
    produto = input('Digite o nome do produto : ')
    valor = float(input('Digite o valor do produto :'))
    quantidade = int(input('Digite a Quantidade :'))
    if quantidade <= 0:
        print('quantidade invalida')
    else :
        total = valor * quantidade
        totalProdutos += total
        listadecompras[produto.lower()] = (valor,quantidade)

    print(f'{produto} , foi cadastrado com sucesso .')
    return totalProdutos
    

def atualizar():
    procurarProduto = input('Qual produto deseja atualizar ?').lower()
    if procurarProduto in listadecompras:
        procurarProduto = input('Qual novo produto a cadastrar ')
        valor = int(input('Digite o valor :'))
        quantidade = int(input('Quantidade :'))
        listadecompras[procurarProduto]=(valor,quantidade)
        print('Dados do produto atualizados !')

    else:
        print('Produto não encontrado .')

def excluir():
    produtoexcluir = input('Nome do item a excluir').lower()
    if produtoexcluir in listadecompras:
        listadecompras.pop(produtoexcluir)
        print(f'O item : {produtoexcluir} foi excluido com sucesso !')

    else :
        print('O produto não foi encontrado .')


# lista de compras
listadecompras = {}
totalProdutos = 0 

# adicionar produtos a lista de compras 
print('Bem vindo a lista de compras ! \n'
      '')
while True : 
    escolha = int(input('    Escolha uma opção : \n'
                        '1 - Adicionar novo produto a lista : \n'
                        '2 - Visualizar lista de compras : \n'
                        '3 - Atualizar informações de um produto \n'
                        '4 - Excluir item da lista. \n'
                        '5 - Ver o valor total dos itens da compra.\n'
                        '0 - Finalizar lista de compras .\n'
                        ''))
    if escolha == 1 :
        totalProdutos = cadastro(totalProdutos)

    elif escolha == 2 :
        for produto, (valor, quantidade) in listadecompras .items():

            print (f'Produto:{produto},Valor = R${valor:.2f}, Quantidade:{quantidade} unidades, Valor Total = {quantidade*valor}')
        print(f'O valor total dos produtos é : {totalProdutos}')

        
    
    elif escolha == 3:
        atualizar()

    elif escolha == 4:
        excluir()

    elif escolha == 5:
        print(f'O valor total dos produtos é : {totalProdutos} .')

    elif escolha == 0:
        print('Fim do programa ')
        break