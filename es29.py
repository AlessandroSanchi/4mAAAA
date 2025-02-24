class ParcoNaturale:
    def __init__(self):
        self.ecosistemi = []

    def monitora_parametri(self, sensore):
        if sensore.attivo:
            print(f"Monitorando parametri")
            return {
                "umidita": 50, 
                "temperatura": 22, 
                "qualita_aria": "Buona"  
            }
        else:
            print(f"Sensore {sensore.tipo} non attivo.")
            return None

    def regola_parametri(self, sensore):
        if sensore.attivo:
            print(f"Regolazione parametri:")
            return True
        else:
            print(f"Sensore {sensore.tipo} non attivo.")
            return False

    def accendi_dispositivi(self, dispositivo):
        dispositivo.stato = "Acceso"
        print(f"Dispositivo {dispositivo.tipo} è stato acceso.")

    def spegni_dispositivi(self, dispositivo):
        dispositivo.stato = "Spento"
        print(f"Dispositivo {dispositivo.tipo} è stato spento.")

    def get_parametri_aree(self, ecosistema):
        print(f"Prendendo parametri: {ecosistema.tipo}")
        return {
            "umidita": ecosistema.umidita,
            "temperatura": ecosistema.temperatura,
            "qualita_aria": ecosistema.qualita_aria
        }


class Ecosistema:
    def __init__(self, tipo, umidita, temperatura, qualita_aria):
        self.umidita = umidita
        self.temperatura = temperatura
        self.qualita_aria = qualita_aria
        self.tipo = tipo 
        self.sensori = []  
        self.dispositivi = []  

    def aggiungi_sensore(self, sensore):
        self.sensori.append(sensore)
        sensore.ecosistema = self 

    def aggiungi_dispositivo(self, dispositivo):
        self.dispositivi.append(dispositivo)
        dispositivo.ecosistema = self 


class Sensore:
    def __init__(self, tipo, attivo):
        self.tipo = tipo
        self.attivo = attivo
        self.ecosistema = None 
        self.parco_naturale = None  


class Dispositivo:
    def __init__(self, tipo, stato):
        self.tipo = tipo
        self.stato = stato
        self.ecosistema = None  
        self.parco_naturale = None  


parco = ParcoNaturale()
ecosistema1 = Ecosistema("Foresta", 60, 20, "Buona")
sensore1 = Sensore("Temperatura", True)
dispositivo1 = Dispositivo("Irrigatore", "Spento")


ecosistema1.aggiungi_sensore(sensore1)
ecosistema1.aggiungi_dispositivo(dispositivo1)


parco.ecosistemi.append(ecosistema1)


parametri = parco.monitora_parametri(sensore1)
print(parametri)


parco.regola_parametri(sensore1)


parco.accendi_dispositivi(dispositivo1)


parametri_ecosistema = parco.get_parametri_aree(ecosistema1)
print(parametri_ecosistema)

parco.spegni_dispositivi(dispositivo1)