

class Veicolo:
    numero_veicoli = 0 
    def __init__(self, marca, modello,):
        self.marca = marca
        self.modello = modello
        Veicolo.numero_veicoli += 1
    @classmethod
    def get_numero_veicoli(self):
        return (f'{Veicolo.numero_veicoli}')
   

    def descrizione(self):
     return f'{self.marca} {self.modello}'





class Auto(Veicolo):
    def __init__(self, marca, modello):
        super().__init__(marca, modello)
        
    
    def descrizione_auto(self):
        return f'{self.marca} {self.modello}'
    

class Moto(Veicolo):
    def __init__(self, marca, modello):
        super().__init__(marca, modello)
        
    
    def descrizione_moto(self):
        return f'{self.marca} {self.modello}'
    


veicolo1 = Auto('Toyota', 'Yaris')
veicolo2 = Moto('Yamaha', 'R1')

print(Veicolo.get_numero_veicoli())
print(veicolo1.descrizione())
print(veicolo2.descrizione())

