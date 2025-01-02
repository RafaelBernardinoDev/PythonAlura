from models.bank import Bank

class Agency(Bank):
    def __init__(self,name,adress,number):
        super().__init__(name,adress)
        self._number = number
    def __str__(self):
        return self._number