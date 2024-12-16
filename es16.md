```mermaid

classDiagram
    Ospedale "1"--|>"n"Reparto : ha
    Reparto "1"--|>"n" Medico : contiene
    Medico"n" -- "n"Farmaco : prescrive
    Medico "n"-- "n"Paziente :tratta
    Paziente"n" -- "n"Farmaco : riceve
    Infermiere"n" --"n" Medico : aiuta
    Infermiere"n"-- "n"Paziente : tratta
    Paziente"1" --|>"1" Cartella_Clinica :possiede
    Medico"n"-- "n"VisitaMedica : tratta
    Paziente "1"--|>"n" VisitaMedica : ha


   class Reparto {
    +String Nome 
   }
   class Ospedale {
    +String Nome
    +String Indirizzo 
    +String reparti
   }
    class Paziente{
    +String Nome 
    +String Cognome 
 }     
    class Farmaco{
    +String Nome 
    +String dose 
 }     
    class Medico{
    +String Nome 
    +String Cognome 
    +String Specializzazione
 }     
    class Cartella_Clinica{
  }    
   class Infermiere{
    +String Nome 
    +String Cognome 
  

 }
    class VisitaMedica{
    +String Data 
    +String Annotazioni
  

 }