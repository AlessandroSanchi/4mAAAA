class Ristorante:
    def __init__(self):
        self.prenotazioni = []

    def aggiungi_prenotazione(self, prenotazione):
        self.prenotazioni.append(prenotazione)

    def cancella_prenotazione(self, prenotazione):
        self.prenotazioni.remove(prenotazione)

    def cerca_prenotazioni_per_nome(self, cognome_cliente):
        prenotazioni_trovate = [p for p in self.prenotazioni if p.cognome_cliente == cognome_cliente]
        return "\n".join(str(p) for p in prenotazioni_trovate) if prenotazioni_trovate else "Nessuna prenotazione trovata."

    def visualizza_prenotazioni(self):
        return "\n".join(str(p) for p in self.prenotazioni) if self.prenotazioni else "Nessuna prenotazione trovata."

    def __str__(self):
        return "\n".join(str(prenotazione) for prenotazione in self.prenotazioni)

class Prenotazione:
    def __init__(self, cognome_cliente, data, ora, numero_persone, stato):
        self.cognome_cliente = cognome_cliente
        self.data = data
        self.ora = ora
        self.numero_persone = numero_persone
        self.stato = stato

    def __str__(self):
        return f"{self.cognome_cliente} {self.data} {self.ora} {self.numero_persone} {self.stato}"

def main():
    risto = Ristorante()
    prenotazione1 = Prenotazione("Rossi", "2023-10-01", 19, 2, "Confermata")
    prenotazione2 = Prenotazione("Bianchi", "2023-10-02", 20, 4, "Confermata")
    prenotazione3 = Prenotazione("Verdi", "2023-10-03", 18, 3, "Annullata")
    
    risto.aggiungi_prenotazione(prenotazione1)
    risto.aggiungi_prenotazione(prenotazione2)
    risto.aggiungi_prenotazione(prenotazione3) 
    
    print(risto.cerca_prenotazioni_per_nome("Rossi"))  # Output: Rossi 2023-10-01 19 2 Confermata
    print(risto.visualizza_prenotazioni())  # Output: All reservations

if __name__ == "__main__":
    main()