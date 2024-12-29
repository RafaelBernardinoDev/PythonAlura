class AccountBank:
    owners = []  

    def __init__(self, ownerName, balance):
        self._ownerName = ownerName.title()
        self._balance = float(balance)
        self._status = False
        AccountBank.owners.append(self)
        '''def object client name, balance and status. Append results in list'''

    def __str__(self):
        return f'{self._ownerName} {self._balance}'
    '''return client name and balance account'''
    

    @classmethod
    def listOwner(cls):
        for owner in cls.owners:
            print(f'Name: {owner._ownerName}\nBalance(U$): {owner._balance}\nStatus: {owner.status}\n')
            '''return name, balance and status for list'''

    @property
    def status(self):
        return 'Active' if self._status else 'Deactivated'
    ''''toggle boolean return for 'Active' and 'Deactivated'''

    def toggleStatus(self):  
        self._status = not self._status  
    """Toggle the status of the account between Active and Deactivated."""

owner1 = AccountBank('Steve Allison', 250.22)
owner1.toggleStatus()
owner2 = AccountBank('Michael Morin', 1850.22)
owner2.toggleStatus()


AccountBank.listOwner()
#start the class and return values