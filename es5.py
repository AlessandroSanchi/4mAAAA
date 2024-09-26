class Dipendente():
    def __init__(self,nome,stipendio):
        self.nome = nome
        self.stipendio = stipendio

    @classmethod
    def cambia_nome(cls, nuovo_nome):
        cls.impiegato = nuovo_nome



class Manager(Dipendente):
    def __init__(self,nome,stipendio,numero_di_team):
     super().__init__(nome, stipendio)
     self.numero_di_team = numero_di_team

    def Get_num_team(self):
       return f"{self.numero_di_team}"
    
    def Get_nome(self):
       return f"{self.nome}"

    def Get_stipendio(self):
       return f"{self.stipendio}"


class Developer(Dipendente):
   def __init__(self,nome,stipendio,codice):
     super().__init__(nome, stipendio)
     self.codice = codice

   def Get_nome(self):
       return f"{self.nome}"

   def Get_stipendio(self):
       return f"{self.stipendio}"
   
   def Get_Codice(self):
       return f"{self.codice}"



manager = Manager("Alice", 50000, 3)
print(manager.Get_nome())  # Output: Alice
print(manager.Get_stipendio())  # Output: 50000
print(manager.Get_num_team())  # Output: 3

print("---------------")

Developer = Developer("Bob", 40000, "Python")
print(Developer.Get_nome())  # Output: Bob
print(Developer.Get_stipendio())  # Output: 40000
print(Developer.Get_Codice())  # Output: Python