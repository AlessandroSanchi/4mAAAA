class MaterialeBiblioteca:
    def __init__(self,titolo:str ,anno_pubblicazione:int ,disponibile:bool=True ):
     self.titolo = titolo
     self.anno_pubblicazione = anno_pubblicazione
     self.disponibile = disponibile

    def get_titolo(self):
        return self.titolo
  
    
    def get_anno_pubblicazione(self):
        return self.anno_pubblicazione


    def is_disponibile(self):
        return self.disponibile

        
    def prestito(self) -> bool:
     if self.is_disponibile():
        self.disponibile = False
        return True


    def restituzione(self):
        if self.is_disponibile():
            raise Exception("Il libro non e stato prestato")
        self.disponibile = True

    @staticmethod
    def ricerca(materiali, titolo=None,anno_pubblicazione=None):
        for materiale in materiali:
            if materiale.get_titolo() == titolo:
                return materiale
        return None


class libro(MaterialeBiblioteca):
    def __init__(self,titolo: str ,anno_pubblicazione: int ,autore,numero_pagine):
     super().__init__(titolo,anno_pubblicazione,)
    
     self.autore = autore
     self.numero_pagine = numero_pagine

    def get_titolo(self):
        return self.titolo
    
    def get_autore(self):
        return self.autore


class Rivista(MaterialeBiblioteca):
    def __init__(self,titolo: str ,anno_pubblicazione: int , mese_pubblicazione,numero_edizione):
     super().__init__(titolo,anno_pubblicazione)

     self.mese_pubblicazione = mese_pubblicazione
     self.numero_edizione = numero_edizione

    def get_numero_edizione(self):
        return self.numero_edizione
    def get_titolo(self):
        return self.titolo




class DvD(MaterialeBiblioteca):
    def __init__(self,titolo: str ,anno_pubblicazione: int , regista,durata):
     super().__init__(titolo,anno_pubblicazione)
     self.regista = regista
     self.durata = durata
    def get_regista(self):
        return self.regista

    def get_durata(self):
        return self.durata





# Esempio di utilizzo
libro = libro("Il Signore degli Anelli", 1954, "J.K.R. Tolkien", 1178)
print(libro.get_titolo())  # Output: Il Signore degli Anelli
print(libro.get_autore())  # Output: J.R.R. Tolkien
libro.prestito()
print(libro.is_disponibile())  # Output: False
libro.restituzione()
print(libro.is_disponibile())  # Output: True

rivista = Rivista("National Geographic", 2023, 5, "Maggio")
print(rivista.get_titolo())  # Output: National Geographic
print(rivista.get_numero_edizione())  # Output: 5

dvd = DvD("Inception", 2010, "Christopher Nolan", 148)
print(dvd.get_titolo())  # Output: Inception
print(dvd.get_regista())  # Output: Christopher Nolan

materiali = [libro, rivista, dvd]
risultato = MaterialeBiblioteca.ricerca(materiali, titolo="Inception")
print(risultato.get_titolo())  # Output: Inception