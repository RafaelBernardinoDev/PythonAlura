class Bank:
    banks = []

    def __init__(self,name,adress):
        self._name = name
        self._adress = adress 
        Bank.banks.append(self)

    def __str__(self):
        return self._name, self._adress
    
    @classmethod
    def list_banks(cls):
        for bank in cls.banks:
            print(f'Name:{bank._name}\nAdress: {bank._adress}')
    

banco1 = Bank('Bradesco', 'Avenida das tantas nº 4000')