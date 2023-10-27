from abc import ABC, abstractmethod

class Ingresso(ABC):
    def __init__(self, indetificador, titulo):
        self.__indetificador = indetificador
        self.titulo = titulo

    @abstractmethod
    def localizacao(self):
        pass
        
    @abstractmethod
    def info(self):
        print(f'Ingresso: {self.__indetificador} - {self.titulo} -', end=' ')

class IngressoPista(Ingresso):
    def __init__(self, indetificador, titulo):
        super().__init__(indetificador, titulo)
        self.tipo = 'Pista'
        self.valor = 100.00

    def localizacao(self):
        print(f'Ingresso {self.tipo}')

    def info(self):
        super().info()
        print(f'{self.valor}')
    
class IngressoVip(Ingresso):
    def __init__(self, indetificador, titulo):
        super().__init__(indetificador, titulo)
        self.tipo = 'Vip'
        self.valor = 200.00

    def localizacao(self):
        print(f'Ingresso {self.tipo}')

    def info(self):
        super().info()
        print(f'{self.valor}')

class IngressoCamarote(Ingresso):
    def __init__(self, indetificador, titulo):
        super().__init__(indetificador, titulo)
        self.tipo = 'Camarote'
        self.valor = 300.00

    def localizacao(self):
        print(f'Ingresso {self.tipo}')

    def info(self):
        super().info()
        print(f'{self.valor}')