

class libro:
    def __init__(self,titolo,autore,pagine):
        self._titolo = titolo
        self._autore = autore
        self._pagine = pagine



libro = libro("Il Signore degli Anelli", "J.R.R. Tolkien", 1200)
print(libro._titolo)  # Chiama automaticamente il getter
libro.titolo = "Lo Hobbit"  # Chiama automaticamente il setter
print(libro.titolo)

