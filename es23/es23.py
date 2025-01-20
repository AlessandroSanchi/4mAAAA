from datetime import datetime
from typing import List

class Commento:
    def __init__(self, testo: str, utente: 'Utente', foto: 'Foto'):
        self.testo = testo
        self.utente = utente
        self.foto = foto

    def scrivi_commento(self):
        print(f"{self.utente.nome} ha scritto un commento: {self.testo}")

class Foto:
    def __init__(self, id: int, titolo: str, descrizione: str, utente: 'Utente', album: 'Album'):
        self.id = id
        self.titolo = titolo
        self.descrizione = descrizione
        self.data_caricamento = datetime.now()
        self.utente = utente
        self.album = album
        self.commenti: List[Commento] = []

    def aggiungi_commento(self, commento: Commento):
        self.commenti.append(commento)
        commento.scrivi_commento()

class Album:
    def __init__(self, titolo: str, descrizione: str, utente: 'Utente'):
        self.titolo = titolo
        self.descrizione = descrizione
        self.utente = utente
        self.foto: List[Foto] = []

    def aggiungi_foto(self, foto: Foto):
        self.foto.append(foto)
        print(f"Foto '{foto.titolo}' aggiunta all'album '{self.titolo}'.")

class Utente:
    def __init__(self, nome: str, email: str, password: str, immagine: str, biografia: str):
        self.nome = nome
        self.email = email
        self.password = password
        self.immagine = immagine
        self.biografia = biografia
        self.commenti: List[Commento] = []

    def carica_foto(self, foto: Foto):
        print(f"{self.nome} ha caricato la foto '{foto.titolo}'.")

    def crea_album(self, titolo: str, descrizione: str) -> Album:
        album = Album(titolo, descrizione, self)
        print(f"{self.nome} ha creato l'album '{titolo}'.")
        return album

    def segui_utente(self, utente: 'Utente'):
        print(f"{self.nome} sta seguendo {utente.nome}.")

# Example usage
if __name__ == "__main__":
    utente1 = Utente("Mario Rossi", "mario@example.com", "password123", "immagine1.jpg", "Biografia di Mario")
    utente2 = Utente("Luigi Bianchi", "luigi@example.com", "password456", "immagine2.jpg", "Biografia di Luigi")

    album1 = utente1.crea_album("Vacanze", "Foto delle vacanze estive")
    foto1 = Foto(1, "Spiaggia", "Una bellissima spiaggia", utente1, album1)
    album1.aggiungi_foto(foto1)

    commento1 = Commento("Che bella foto!", utente2, foto1)
    foto1.aggiungi_commento(commento1)

    utente1.carica_foto(foto1)