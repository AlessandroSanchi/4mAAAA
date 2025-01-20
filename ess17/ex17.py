class Insegnante:
    def __init__(self, nome, cognome, strumento):
        self._nome = nome
        self._cognome = cognome
        self._strumento = strumento
        self.studenti = []

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
    def strumento(self):
        return self._strumento

    @strumento.setter
    def strumento(self, strumento):
        self._strumento = strumento

        


class Studente:
    def __init__(self, nome, cognome):
        self._nome = nome
        self._cognome = cognome
        self.insegnante = None
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

    def set_insegnante(self, insegnante):
        self.insegnante = insegnante
        insegnante.studenti.append(self)  
        return self.insegnante

    def iscrivi_corso(self, corso):
        if corso in self.corsi:
         print("Già nel corso") 
        else: 
         self.corsi.append(corso)
         corso.studenti.append(self)  

    def __str__(self):
        corsi_str = ', '.join(f"{corso.nome} per {corso.durata}" for corso in self.corsi)
        return f"{self.nome} {self.cognome} con l'insegnante {self.insegnante.nome} partecipa ai corsi: {corsi_str}"


class Corso:
    def __init__(self, nome, durata):
        self._nome = nome
        self._durata = durata
        self.studenti = []

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









def main():
    # Creazione degli insegnanti
    insegnante1 = Insegnante("Mario", "Rossi", "Pianoforte")
    insegnante2 = Insegnante("Luca", "Bianchi", "Chitarra")

    # Creazione degli studenti
    studente1 = Studente("Anna", "Verdi")
    studente2 = Studente("Marco", "Neri")

    # Assegnazione degli insegnanti agli studenti
    studente1.set_insegnante(insegnante1)
    studente2.set_insegnante(insegnante2)

    # Creazione dei corsi
    corso1 = Corso("Teoria Musicale", "3 mesi")
    corso2 = Corso("Tecnica Pianistica", "6 mesi")

    # Iscrizione degli studenti ai corsi
    studente1.iscrivi_corso(corso1)
    studente1.iscrivi_corso(corso2)
    studente2.iscrivi_corso(corso1)

    # Stampa delle informazioni
    print(studente1)
    print(studente2)

if __name__ == "__main__":
    main()