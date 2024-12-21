import os


def options():
    print("1.Cadastro de Valor")
    print("2.Consulta de Valor")

def join():
    inJoin = input("Insira o valor que deseja salvar")
    inList = inJoin

def consult():
    join('inList')

def menu():
    print("Bem vindo ao Banco de Dados X")
    options()
    inMenu = input("Insira a opção que deseja realizar: ")
    inConvert = int(inMenu)

    if inConvert == 1:
        join()
    elif inConvert == 2:
        consult()



def main():
    menu()

if __name__ == "__main__":
    main()

