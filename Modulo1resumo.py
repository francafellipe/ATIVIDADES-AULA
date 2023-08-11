while True:
    escolha = int(input("Escolha uma das opções:\n"
                        "1 - calcular media for;\n"
                        "2 - calcular media while;\n"
                        "0 - sair\n"))
    
    match escolha:
        case 1:
            acumladorNota = 0

            for i in range(4):
                nota = float(input())
                acumladorNota += nota

            media = acumladorNota / 4
            print(media)

        case 2:
            acumladorNota = 0
            contadorVolta = 0

            while contadorVolta <= 3:
                nota = float(input())
                acumladorNota += nota

                contadorVolta += 1
            
            media = acumladorNota / (contadorVolta + 1)
            print(media)

        case 0:
            break