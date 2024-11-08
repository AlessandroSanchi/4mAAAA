class Auto:
    def __init__(self,marca,modello):
        self.marca = marca 
        self.modello = modello 
        self.motore = None

    def get_modello(self):
        return self.modello

     
    def get_tipo(self):
        return self.tipo
    

    def assegna_motore(self,motore):
        self.motore = motore 
        motore.auto = self
         
      


class Motore:
     def __init__(self,numero_seriale,tipo):
        self.numero_seriale = numero_seriale
        self.tipo = tipo
        self.auto = None

     def get_numero_seriale(self):
        return self.numero_serial

     
     def get_tipo(self):
        return self.tipo
     
     


# Creazione delle istanze
auto1 = Auto("Fiat", "500")
motore1 = Motore("ENG123456", "Benzina")

# Associazione tra auto e motore
auto1.assegna_motore(motore1)

# Verifica dell'associazione
print(f"{auto1.marca} {auto1.modello} ha il motore: {auto1.motore.numero_seriale}")
print(f"Il motore {motore1.numero_seriale} appartiene a: {motore1.auto.marca} {motore1.auto.modello}")