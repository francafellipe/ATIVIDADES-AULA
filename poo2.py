class Animal:
    def __init__(self,respirar,comer,andar):
        self.respirar = respirar
        self.comer = comer
        self.andar = andar


        
class Cachorro(Animal):
    def __init__(self,nome,peso,raca,respirar,comer,andar) -> None: #init e o metodo construtor , e para inicializar as caracteristicas da classe
        super().__init__(self,respirar,comer,andar)
        self.nome = nome 
        self.peso = peso 
        self.raca = raca

    def comer(self):
        return "Croc Croc Croc "
    
class Gato(Animal):
    def __init__(self,nome,peso,raca,respirar,comer,andar):# e o metodo construtor , usado para inicializar as caracteristicas da classe
        super().__init__(respirar,comer,andar)
        self.nome = nome 
        self.peso = peso 
        self.raca = raca 

    def derrubarCoisas(self):
        return f"O gato {self.nome} quebrou algo"
    
akita = Cachorro("Joaozinho ","Akita",25)
beagle = Cachorro ("Totozinho","Beagle",12)
        
print(f"O cachorro {akita.nome} da raça {akita.raca} pesa {akita.peso}kg e come: \n"
      f"{akita.comer()}")
print(f"O cachorro {beagle.nome} da raça {beagle.raca} pesa {beagle.peso} kg e come: \n"
      f"{beagle.comer()}")

    
gato = Gato(nome="Bichano",peso=25,raca="Siames")

print(gato.derrubarCoisas())
