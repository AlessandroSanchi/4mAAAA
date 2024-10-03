class Piatto:
    def __init__(self,Nome,Prezzo,Disponibile : bool = True):
     self.nome = Nome
     self.prezzo = Prezzo
     self.Disponibile = Disponibile

    def __str__(self):
        print( f"{self.nome} - {self.prezzo}€ - {'Disponibile' if self.Disponibile else 'Non disponibile'}")

        


    def is_disponibile(self):
        return self.Disponibile


    def ordina(self):
        if self.is_disponibile():
           self.Disponibile = False

    def disponi(self):
        if self.is_disponibile():
           self.Disponibile = True 

        
    
class Antipasto(Piatto):
    def __init__(self,Nome,Prezzo,ingredienti,porzione):
     super().__init__(Nome,Prezzo)
     self.porzione = porzione
     self.ingredienti = ingredienti

    def get_ingredienti(self):
        return self.ingredienti

    def get_sugo(self):
        return self.porzione

    


class Primo(Piatto):
    def __init__(self,Nome,Prezzo,tipo_pasta,sugo):
     super().__init__(Nome,Prezzo)
     self.tipo_pasta = tipo_pasta
     self.sugo = sugo

    def get_tipo_pasta(self):
        return self.tipo_pasta

    def get_sugo(self):
        return self.sugo

      

class Secondo(Piatto):
    def __init__(self,Nome,Prezzo,tipo_carne,cottura):
      super().__init__(Nome,Prezzo)
      self.tipo_carne = tipo_carne
      self.cottura = cottura

    def get_tipo_carne(self):
        return self.tipo_carne

    def get_cottura(self):
        return self.cottura

      

class Dolce(Piatto):
    def __init__(self,Nome,Prezzo,tipo_dolce,calorie):
      super().__init__(Nome,Prezzo)
      self.tipo_dolce = tipo_dolce
      self.calorie = calorie

    def get_tipo_dolce(self):
         return self.tipo_dolce

    def get_calorie(self):
         return self.calorie

  
@staticmethod
def calcola_conto(piatti_ordinati):
    prezzo = 0
    for piatti in piatti_ordinati:
        prezzo += piatti.prezzo
    return prezzo

def stampa_menu(piatti_ordinati):
    for piatti in piatti_ordinati:
        print(piatti)





# Esempio di utilizzo
antipasto = Antipasto("Bruschetta", 5.0, ["Pane", "Pomodoro", "Basilico"], "Piccola")
primo = Primo("Spaghetti alla Carbonara", 12.0, "Spaghetti", "Carbonara")
secondo = Secondo("Bistecca alla Fiorentina", 25.0, "Manzo", "Media")
dolce = Dolce("Tiramisù", 6.0, "Tiramisù", 450)

piatti_ordinati = [antipasto, primo, secondo, dolce]
conto_totale = calcola_conto(piatti_ordinati)
print(f"Il conto totale è: {conto_totale}€")  # Output: Il conto totale è: 48.0€

print("\nMenu del Ristorante:")
stampa_menu(piatti_ordinati)


