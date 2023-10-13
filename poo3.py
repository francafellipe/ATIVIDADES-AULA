'''class Humano:
    def __init__(self, nome, altura, sexo, cpf, idade):
        self.nome = nome
        self.altura = altura
        self.sexo = sexo
        self.cpf = cpf
        self.idade = idade
    
    def falar(self):
        print(f'{self.nome} está falando.')

class Empregado(Humano):
    def trabalhar(self):
        print(f'{self.nome} está trabalhando.')

class Gerente(Empregado):
    def gerenciar(self):
        print(f'{self.nome} está gerenciando.')

class Jogador(Humano):
    def jogar(self):
        print(f'{self.nome} está jogando.')

    def passe(self, jogador):
        print(f'{self.nome} está passando para {jogador}')
    

neymar = Jogador('Neymar', 1.75, 'M', '123.456.789-00', 29)

neymar.passe('Messi')
        '''
from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def comer(self):
        pass

    @abstractmethod
    def beber(self):
        pass

    def respirar(self):
        print(f'{self.nome} está respirando.')

class Mamifero(Animal):
    def comer(self):
        print(f'{self.nome} está comendo com a boca.')

    def beber(self):
        print(f'{self.nome} está bebendo com a boca.')
    
class Ave(Animal):
    def comer(self):
        print(f'{self.nome} está comendo com o bico.')
    
    def beber(self):
        print(f'{self.nome} está bebendo com o bico.')


gato = Mamifero('Gato')
passaro = Ave("Aguia")

gato.comer()
gato.beber()
gato.respirar()
passaro.comer()
passaro.beber()
passaro.respirar()