class Studente:
    def __init__(self,nome,matricola):
        self.nome = nome
        self.matricola = matricola
        self.corsi = []
    


    def get_matricola(self):
        return self.matricola
    
    def get_codice(self):
        return self.codice
    

    def aggiungi_corso(self, corso):
         for x in self.corsi:
          if x.titolo == corso.titolo:
            print("Gia Aggiunto")
            return
          
             
         self.corsi.append(corso)
         corso.studenti.append(self)


class Corso:
    def __init__(self, titolo,codice):
        self.titolo = titolo
        self.codice = codice
        self.studenti = []


    def get_titolo(self):
        return self.titolo
    
    def get_codice(self):
        return self.codice
    

    def aggiungi_studente(self, studente):
        for x in self.studenti:
          if x.nome == studente.nome:
            print("Gia Aggiunto")
            return

        self.studenti.append(studente)
        studente.corsi.append(self)










# Creazione delle istanze di Studente
studente1 = Studente("Alice Rossi", "MAT123")
studente2 = Studente("Marco Bianchi", "MAT456")

# Creazione delle istanze di Corso
corso1 = Corso("Programmazione Python", "PY101")
corso2 = Corso("Database Relazionali", "DB201")
corso3 = Corso("Sistemi Operativi", "SO301")

# Associazione tra studenti e corsi
studente1.aggiungi_corso(corso1)
studente1.aggiungi_corso(corso2)
studente2.aggiungi_corso(corso2)
studente2.aggiungi_corso(corso3)

# Verifica delle associazioni
print(f"{studente1.nome} è iscritto ai seguenti corsi:")
for corso in studente1.corsi:
    print(f"- {corso.titolo} ({corso.codice})")

print(f"\n{corso2.titolo} ha i seguenti studenti iscritti:")
for studente in corso2.studenti:
    print(f"- {studente.nome} ({studente.matricola})")