from random import choice
from time import sleep

def jogador():
    escolha = int(input("Escolha uma das opções:\n" +
                        "1 - Pedra\n" +
                        "2 - Tesoura\n" +
                        "3 - Papel\n"))
    
    match escolha:
        case 1:
            return "Pedra"
        case 2:
            return "Tesoura"
        case 3:
            return "Papel"
        case _:
            return "Error"

def computador():
    escolha = ["Pedra", "Tesoura", "Papel"]

    return choice(escolha)

def jogo(jogador, computador):
    if jogador == "Error":
        print("Opção do jogador é invalida.")
    elif jogador == computador:
        print(f"jogadador -> {jogador}")
        sleep(2)
        print(f"computador -> {computador}")
        sleep(2)
        print("Empate")
    elif ((jogador == "Pedra" and computador == "Tesoura") or 
          (jogador == "Papel" and computador == "Pedra") or 
          (jogador == "Tesoura" and computador == "Papel")):
        print(f"jogadador -> {jogador}")
        sleep(2)
        print(f"computador -> {computador}")
        sleep(2)
        print("Jogador Venceu")
    else:
        print(f"jogadador -> {jogador}")
        sleep(2)
        print(f"computador -> {computador}")
        sleep(2)
        print("Computador Venceu")