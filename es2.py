class Contobancario:
    def __init__(self, Numero_conto, intestatario, _saldo):
        self.Numero_conto = Numero_conto
        self.intestatario = intestatario
        self._saldo = _saldo
    

    def get_saldo(self):
        return self._saldo

    def deposita(self,_saldo):
        print("Deposito in corso...")
        print(f"Deposito di {_saldo} euro effettuato.")
        self._saldo = self._saldo + _saldo
        return self._saldo
    
    def preleva(self,_saldo):
        print("Prelievo in corso...")
        print(f"Prelievo di {_saldo} euro effettuato.")
        self._saldo = self._saldo - _saldo
        if _saldo < 0:
            print("Fondi insufficienti.")
            return self._saldo

    


conto = Contobancario("123456789", "Mario Rossi", 1000.0)
conto.deposita(100.0)
conto.preleva(1)

print(conto.get_saldo())

