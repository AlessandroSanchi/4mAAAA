
#Implementa una funzione verifica_ingredienti che prende una lista di ricette e restituisce quelle che possono essere preparate con gli ingredienti disponibili.

class Ricetta:
    def __init__(self,nome,tempo_preparazione,difficolta):
     self.nome = nome
     self.tempo_preparazione = tempo_preparazione
     self.difficolta = difficolta


    def __str__(self):
        return f"{self.nome} - {self.tempo_preparazione} min - Difficoltà: {self.difficolta}"


    
class Primo(Ricetta):
    def __init__(self,nome,tempo_preparazione,ingredienti,difficolta,tipo_pasta,sugo):
        super().__init__(nome,tempo_preparazione,difficolta)
        self.tipo_pasta = tipo_pasta
        self.sugo = sugo
        self.ingredienti = ingredienti
     
    def __str__(self):
        return f"{self.nome} - {self.tempo_preparazione} min - Difficoltà: {self.difficolta}" 

class Secondo(Ricetta):
    def __init__(self,nome,tempo_preparazione,ingredienti,difficolta,tipo_carne,cottura):
         super().__init__(nome,tempo_preparazione,difficolta)
         self.tipo_carne = tipo_carne
         self.cottura = cottura
         self.ingredienti = ingredienti
    
       


    def __str__(self):
        return f"{self.nome} - {self.tempo_preparazione} min - Difficoltà: {self.difficolta}"

class Dolce(Ricetta):
    def __init__(self,nome,tempo_preparazione,ingredienti,difficolta,tipo_dolce,zucchero):
         super().__init__(nome,tempo_preparazione,difficolta)
         self.tipo_dolce = tipo_dolce 
         self.difficolta = difficolta
         self.ingredienti = ingredienti
     
        


    def __str__(self):
        return f"{self.nome} - {self.tempo_preparazione} min - Difficoltà: {self.difficolta}"



def stampa_ricette(ricette):
    for ricetta in ricette:
        print(ricetta)

def verifica_ingredienti(ricette, ingredienti):
    ricette_possibili = []
    
    for ricetta in ricette:
        # Controlla se tutti gli ingredienti della ricetta sono disponibili
        if all(ingrediente in ingredienti for ingrediente in ricetta.ingredienti):
            ricette_possibili.append(ricetta)
    
    return ricette_possibili


# Esempio di utilizzo
primo = Primo("Spaghetti alla Carbonara", 20, ["Spaghetti", "Uova", "Pancetta"], "Media", "Spaghetti", "Carbonara")
secondo = Secondo("Bistecca alla Fiorentina", 30, ["Bistecca", "Sale", "Pepe"], "Alta", "Manzo", "Media")
dolce = Dolce("Tiramisù", 30, ["Mascarpone", "Caffè", "Savoiardi"], "Media", 200, "Dessert")

ricette = [primo, secondo, dolce]
ingredienti = ["Spaghetti", "Uova", "Pancetta", "Bistecca", "Sale", "Pepe", "Mascarpone", "Caffè", "Savoiardi", "Pane", "Pomodoro", "Basilico"]
ricette_possibili = verifica_ingredienti(ricette, ingredienti)
print(f"Ricette che possono essere preparate: {len(ricette_possibili)}")

print("\nInformazioni sulle ricette:")
stampa_ricette(ricette)