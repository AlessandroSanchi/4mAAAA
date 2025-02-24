Gestione di una libreria di film. Ogni film ha un titolo, un regista, un anno di uscita, un genere (azione, commedia, drammatico, horror, documentario) e una valutazione (da 1 a 10). Il sistema deve permettere di:
Aggiungere nuovi film alla libreria.
Cercare film per titolo o regista.
Visualizzare tutti i film presenti nella libreria.
Calcolare la valutazione media dei film.
Il sistema deve includere due classi principali:
: rappresenta un singolo film nella libreria.
: gestisce i film e le operazioni associate.




```mermaid
classDiagram
    class Film {
        - str titolo
        - str regista
        - int AnnoDiUscita
        - str genere
        - int valutazione
    }

    class LibreriaFilm {
        + aggiungiFilm(Film,film)
        + cercaFilmPerTitolo(str titolo)   List[Film]
        + cercaFilmPerRegista(str regista) List[Film]
        + visualizzaFilm() : List[Film]
        + calcolaValutazioneMedia() 
    }

    LibreriaFilm --> Film