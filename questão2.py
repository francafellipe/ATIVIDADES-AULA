while True:

    numero = int(input("Digite um numero que você quer ver a tabuada de soma :"))

    if numero > 10 or numero < 1 :
        print ("Numero não está entre 1 a 10 :")

    else :
        for i in range (1,11):
            print (f"{numero} + {i}= {numero + i}")

        break