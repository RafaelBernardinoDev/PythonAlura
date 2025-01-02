from models.agencybank import Agency

agency1 = Agency('Agencia São Miguel','Avenida São Miguel', 105)

def main():
    agency1.list_banks()

if __name__=='__main__':
    main()