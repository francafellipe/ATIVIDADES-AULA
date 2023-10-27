from cadastroingresso import (IngressoPista, IngressoVip, IngressoCamarote)
from random import randint

def main():
    pista = list()
    vip = list()
    camarote = list()

    while True:
        escolha = int(input('Escolha o tipo de ingresso:\n'
                            '1 - Pista\n'
                            '2 - Vip\n'
                            '3 - Camarote\n'
                            '4 - Sair\n'
                            '>>> '))
        if (
            (escolha == 1 and len(pista) == 3) or
            (escolha == 2 and len(vip) == 3) or
            (escolha == 3 and len(camarote) == 3)
            ):
            print('Ingressos esgotados! Escolha outro tipo de ingresso.')
            continue


        match escolha:
            case 1:
                i = randint(1, 3)

                while i in pista:
                    i = randint(1, 3)
                    
                pista.append(i)
                ingresso = IngressoPista(i, 'Show do Metallica')
                ingresso.info()
                ingresso.localizacao()
            case 2:
                i = randint(4, 6)

                while i in vip:
                    i = randint(4, 6)

                vip.append(i)
                ingresso = IngressoVip(i, 'Show do Metallica')
                ingresso.info()
                ingresso.localizacao()
            case 3:
                i = randint(7, 9)

                while i in camarote:
                    i = randint(7, 9)

                camarote.append(i)
                ingresso = IngressoCamarote(i, 'Show do Metallica')
                ingresso.info()
                ingresso.localizacao()
            case 4:
                break
            
            case _:
                print('Opção inválida!')

if __name__ == '__main__':
    main()