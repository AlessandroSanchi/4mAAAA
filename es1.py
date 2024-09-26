
class Persona:
    def __init__(self, nome, eta, citta):
        self.nome = nome
        self.eta = eta
        self.citta = citta

    def saluta(self):
        print(f"Ciao, sono {self.nome}")
    
    def descrizione(self):
        print(f"ho {self.eta} anni, e vengo da {self.citta}")  

persona = Persona("Fabio", 6, "Catanzaro")
persona.saluta()
persona.descrizione()

