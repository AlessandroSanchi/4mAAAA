

class frazione: 
    def __init__(self,numeratore,denominatore):
        self.numeratore = numeratore
        self.denominatore = denominatore


    def __add__(self,altro):
        return frazione(self.numeratore + altro.numeratore,self.denominatore)

        
    def __sub__(self,altro):
        return frazione(self.numeratore-altro.numeratore,self.denominatore)

    def __mul__(self,altro):
        return frazione(self.numeratore*altro.numeratore,self.denominatore*altro.denominatore)


    def __str__(self):
        return f"{self.numeratore,self.denominatore}"
                                                              










# Esempio di utilizzo
f1 = frazione(1, 2)
f2 = frazione(3, 2)

#Addizione
f3 = f1 + f2
print(f3)  # Output: Frazione(5, 4)

# Sottrazione
f4 = f1 - f2
print(f4)  # Output: Frazione(-1, 4)

# Moltiplicazione
f5 = f1 * f2
print(f5)  # Output: Frazione(3, 8)

# Rappresentazione
print(f1)  # Output: Frazione(1, 2)


