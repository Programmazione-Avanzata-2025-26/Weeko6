# Classe utilizzata come DTO, per "mappare" una riga
# della tabella User del database in un oggetto Python

class UserDTO:
    def __init__(self, id, name, phone): # Con gli attributi (colonne) della tabella
        self.id = id
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"{self.id}, {self.name}, {self.phone}"

    def __eq__(self, other):
        return self.id == other.id

    def __lt__(self, other):
        return self.id - other.id

    def __hash__(self):
        return hash(self.id)
