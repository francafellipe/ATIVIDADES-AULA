def media (*args): # utilizando *args podemos criar várias situações em que chamamos a mesma função
    soma = 0
    contagem = 0

    for i in args:
        soma+= i
        contagem +=1

    media = soma / contagem

    print(f'A média é : {media}')

media1 = media(1,2,3,4) #primeira situação
media1 = media(2,3,4) #segunda situação
media1 = media(3,4)#terceira situação
