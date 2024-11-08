class Casa: 
    def __init__(self,indirizzo,proprietario):
        self.indirizzo = indirizzo
        self.proprietario = proprietario
        self.stanze = []


    def get_indirizzo(self):
        return self.indirizzo

    def get_proprietario(self):
        return self.proprietario
    
    def aggiungi_stanza(self,stanza):
        self.stanze.append(stanza)
        stanza.casa = self
    
    def stampa_stanze(self):
        print (f"{self.stanze}")




class Stanza:
    def __init__(self,nome,superficie):
        self.nome = nome 
        self.superficie = superficie
        self.casa = None

    def get_nome(self):
        return self.nome

    def get_superficie(self):
        return self.superficie

















# Creazione dell'istanza di Casa
casa = Casa("Via delle Rose 15", "Maria Rossi")

# Creazione delle istanze di Stanza
soggiorno = Stanza("Soggiorno", 30)
cucina = Stanza("Cucina", 15)
camera = Stanza("Camera da Letto", 20)

# Aggiunta delle stanze alla casa
casa.aggiungi_stanza(soggiorno)
casa.aggiungi_stanza(cucina)
casa.aggiungi_stanza(camera)

# Verifica dell'associazione
print(f"Casa di {casa.proprietario} situata in {casa.indirizzo} contiene le seguenti stanze:")
for stanza in casa.stanze:
    print(f"- {stanza.nome} ({stanza.superficie} mq)")