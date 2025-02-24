class LibreriaFilm:
    def __init__(self):
        self.film = []

    def aggiungi_film(self, film):
        self.film.append(film)

    def rimuovi_film(self, film):
        self.film.remove(film)

    def cercaFilmPerTitolo(self, titolo):
        films_found = [f for f in self.film if f.titolo == titolo]
        return "\n".join(str(f) for f in films_found) if films_found else "Nessun film trovato."

    def cercaFilmPerRegista(self, regista):
        films_found = [f for f in self.film if f.regista == regista]
        return "\n".join(str(f) for f in films_found) if films_found else "Nessun film trovato."

    def calcolaValutazioneMedia(self):
        if not self.film:
            return 0
        return sum(f.valutazione for f in self.film) / len(self.film)

    def __str__(self):
        return "\n".join(str(film) for film in self.film)

class Film:
    def __init__(self, titolo, regista, anno, valutazione, genere):
        self.titolo = titolo
        self.regista = regista
        self.anno = anno
        self.valutazione = valutazione
        self.genere = genere

    def __str__(self):
        return f"{self.titolo} {self.regista} {self.anno} {self.valutazione} {self.genere}"

def main():
    libreria = LibreriaFilm()
    film1 = Film("Titanic", "James Cameron", 1997, 9, "Drammatico")
    film2 = Film("Avatar", "James Cameron", 2009, 8, "Fantascienza")
    film3 = Film("Il Padrino", "Francis Ford Coppola", 1972, 10, "Drammatico")
    libreria.aggiungi_film(film1)
    libreria.aggiungi_film(film2)
    libreria.aggiungi_film(film3) 
    print(libreria.cercaFilmPerTitolo("Titanic")) #output: Titanic James Cameron 1997 9 Drammatico
    print(libreria.cercaFilmPerRegista("James Cameron")) #output: Titanic James Cameron 1997 9 Drammatico\nAvatar James Cameron 2009 8 Fantascienza
    print(libreria.calcolaValutazioneMedia()) #output: 9

if __name__ == "__main__":
    main()