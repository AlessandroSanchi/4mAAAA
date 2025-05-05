Creare un programma di trading automatizzato che utilizza flussi economici per prendere decisioni d'acquisto e vendita.
 Il programma deve implementare strategie di trading semplici e includere funzioni di gestione del rischio.



 ```mermaid
classDiagram
    class CryptoManager {
        + TracciaAPI() Crypto
        + LeggiCryptoDaComprare(Crypto) CryptoC
        + CalcolaRischio(CryptoC) CryptoDaComprare
        + CompraCrypto(Portafoglio,CryptoDaComprare) 
        + LeggiCryptoDaVendere(Crypto) CryptoDaVendere
        + VendiCrypto(CryptoDaVendere)
    }


    class Portafoglio {
        - float Conto 
    }


    CryptoManager "1" -- "1" Portafoglio : "Utilizza"
