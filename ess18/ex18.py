class Palestra:
    def __init__(self, nome, indirizzo):
        self._nome = nome
        self._indirizzo = indirizzo

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def indirizzo(self):
        return self._indirizzo

    @indirizzo.setter
    def indirizzo(self, indirizzo):
        self._indirizzo = indirizzo


    

class Allenatore:
    def __init__(self, nome, cognome, specializzazione):
        self._nome = nome
        self._cognome = cognome
        self._specializzazione = specializzazione
        self.membri = []
        self.corsi = []


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def cognome(self):
        return self._cognome

    @cognome.setter
    def cognome(self, cognome):
        self._cognome = cognome

    @property
    def specializzazione(self):
        return self._specializzazione

    @specializzazione.setter
    def specializzazione(self, specializzazione):
        self._specializzazione = specializzazione


    def set_membri(self, membro):
        self.membro = membro
        membro.membri.append(self)  
        return self.membro
    
    def __str__(self):
         return f"{self.nome} {self.cognome} con l'insegnante {self.specializzazione}  {self.membri}"

class Membro:
    def __init__(self, nome, cognome):
        self._nome = nome
        self._cognome = cognome
        self.corsi = []
        self.Allenatore = None
        self.scheda_allenamento = None

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def cognome(self):
        return self._cognome

    @cognome.setter
    def cognome(self, cognome):
        self._cognome = cognome

    
    def set_Allenatore(self, Allenatore):
        self.Allenatore = Allenatore 
        return self.Allenatore
    
    def iscrivi_corso(self,Corso):
        self.corsi.append(Corso)

    def set_scheda_allenamento(self, scheda_allenamento):
        self.scheda_allenamento = scheda_allenamento 
        return self.scheda_allenamento    


class Corso:
    def __init__(self, nome, durata, allenatore):
        self._nome = nome
        self._durata = durata
        self.Allenatore = allenatore 

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def durata(self):
        return self._durata

    @durata.setter
    def durata(self, durata):
        self._durata = durata

    def set_Allenatore(self, allenatore):
        self.Allenatore = allenatore 
        return self.Allenatore
    
    def set_scheda_allenamento(self, allenatore):
        self.Allenatore = allenatore 
        return self.Allenatore



class SchedaAllenamento:
    def __init__(self, descrizione, esercizi):
        self._descrizione = descrizione
        self._esercizi = [esercizi]

    @property
    def descrizione(self):
        return self._descrizione

    @descrizione.setter
    def descrizione(self, descrizione):
        self._descrizione = descrizione

    @property
    def esercizi(self):
        return self._esercizi

    @esercizi.setter
    def esercizi(self, esercizi):
        self._esercizi = esercizi




















def main():
    # Creazione degli allenatori
    allenatore1 = Allenatore("Giovanni", "Rossi", "Fitness")
    allenatore2 = Allenatore("Luca", "Bianchi", "Yoga")

    # Creazione dei membri
    membro1 = Membro("Anna", "Verdi")
    membro2 = Membro("Marco", "Neri")

    # Assegnazione degli allenatori ai membri
    membro1.set_Allenatore(allenatore1)
    membro2.set_Allenatore(allenatore2)

    # Creazione dei corsi
    corso1 = Corso("Pilates", "3 mesi", allenatore1)
    corso2 = Corso("HIIT", "6 mesi", allenatore1)
    corso3 = Corso("Yoga Avanzato", "4 mesi", allenatore2)

    # Iscrizione dei membri ai corsi
    membro1.iscrivi_corso(corso1)
    membro1.iscrivi_corso(corso2)
    membro2.iscrivi_corso(corso3)

    # Creazione delle schede di allenamento
    scheda1 = SchedaAllenamento(membro1, ["Esercizio 1: Squat", "Esercizio 2: Push-up"])
    scheda2 = SchedaAllenamento(membro2, ["Esercizio 1: Plank", "Esercizio 2: Burpee"])

    # Assegnazione delle schede di allenamento ai membri
    membro1.set_scheda_allenamento(scheda1)
    membro2.set_scheda_allenamento(scheda2)

    # Stampa delle informazioni
    print(membro1)
    print(membro2)

if __name__ == "__main__":
    main()