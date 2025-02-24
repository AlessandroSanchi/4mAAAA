class Flotta:
    def __init__(self):
        self.Veicoli = []

    def Aggiungi_Veicoli(self,Veicolo):
        if Veicolo is not self.Veicoli:
         self.Veicoli.append(Veicolo)
        else:
            pass

    def VisualizzaInfo(self):
        return self.Veicoli




class Veicolo:
    def __init__(self,marca,modello,carburante):
        self.marca = marca 
        self.modello = modello 
        self.carburante = carburante 



class Auto(Veicolo):
    def __init__(self,marca,modello,carburante):
        super().__init__(marca,modello,carburante)




class Camion(Veicolo):
    def __init__(self,marca,modello,carburante):
        super().__init__(marca,modello,carburante)



def main():
    # Create an instance of Flotta
    flotta = Flotta()

    # Create some vehicle instances
    auto1 = Auto("Fiat", "Panda", "Benzina")
    auto2 = Auto("Toyota", "Yaris", "Ibrido")
    camion1 = Camion("Iveco", "Stralis", "Diesel")

    # Add vehicles to the fleet
    flotta.Aggiungi_Veicoli(auto1)
    flotta.Aggiungi_Veicoli(auto2)
    flotta.Aggiungi_Veicoli(camion1)

    # Attempt to add the same vehicle again (should not be added)
    flotta.Aggiungi_Veicoli(auto1)

    # Display the information of the vehicles in the fleet
    veicoli_info = flotta.VisualizzaInfo()
    for veicolo in veicoli_info:
        print(f"Marca: {veicolo.marca}, Modello: {veicolo.modello}, Carburante: {veicolo.carburante}")




if __name__ == "__main__":
    main()