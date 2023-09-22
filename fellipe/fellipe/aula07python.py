from random import choice

# pedra , papel , tesoura 

def jogo ():
    escolhas = (1,2,3)
    escolha_usuario = (int(input('Escolha \n'
                                '1 - Pedra :\n'
                                '2 - Papel :\n'
                                '3 - Tesoura : \n'
                                )))

    escolha_computador = choice(escolhas)
     
    if escolha_usuario == 1 :
        if escolha_computador == 2 :
            print('Computador venceu ')
                

        if escolha_computador == 3 :
             print('Você venceu ')
                

        if escolha_computador == 1:
            print('Empate')
            
    if escolha_usuario == 2 :
        if escolha_computador == 2 :
            print('Empate ')
                

        if escolha_computador == 3 :
            print('Computador Venceu ')
                

        if escolha_computador == 1:
                print('Voce venceu')
    if escolha_usuario == 3:
         
         if escolha_computador == 1:
              print('Voce perdeu')
         if escolha_computador == 2:
              print('Você venceu')
         if escolha_computador == 3:
              print('Empate ')

        
         

            
jogo()

