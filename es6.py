

class Pagamento:
    def __init__(self,Nome,Codice,Data,Pin,Email,Password):
        self.Nome = Nome
        self.Codice = Codice
        self.Data = Data
        self.Pin = Pin
        self.Email = Email
        self.Password = Password







class CartadiCredito(Pagamento):
    def __init__(self,Nome,Codice,Data,Pin):
     self.Nome = Nome
     self.Codice = Codice
     self.Data = Data
     self.Pin = Pin

    def processa_pagamento(self):
        print (f"Elaborazione pagamento con Carta di Credito per {self.Nome}")






class PayPal(Pagamento):
    def __init__(self,Email,Password):
      self.Email = Email
      self.Password = Password

    def processa_pagamento(self):
        print (f"Elaborazione pagamento con Paypal per {self.Email}")

def effettua_pagamento(metodo_di_pagamento: Pagamento):
    metodo_di_pagamento.processa_pagamento()


pagamento_carta = CartadiCredito("Mario Rossi", "1234 5678 9012 3456", "12/23", "123")
pagamento_paypal = PayPal("mario.rossi@example.com", "password123")

effettua_pagamento(pagamento_carta)  
effettua_pagamento(pagamento_paypal) 