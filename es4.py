

class Calcolatrice:
    def __init__(self, numero1: int , numero2: int):
        self.numero1 = numero1
        self.numero2 = numero2
    @staticmethod
    def addizione(numero1,numero2):
        risultato = numero1 + numero2
        return f"{risultato}"

    def sottrazione (numero1,numero2):
        risultato = numero1 - numero2
        return f"{risultato}"
    
    def moltiplicazione (numero1,numero2):
        risultato = numero1 * numero2
        return f"{risultato}"
    
    def divisione(numero1,numero2):
        if numero2 == 0:
           return "Error"
        else:
         risultato = numero1 / numero2
         return f"{risultato}"

print(Calcolatrice.addizione(2,5))
print(Calcolatrice.sottrazione(2,5))
print(Calcolatrice.moltiplicazione(2,5))
print(Calcolatrice.divisione(65,0.1))

    