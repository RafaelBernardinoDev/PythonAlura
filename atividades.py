# 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.
# numberIn = input("Insira um número inteiro para verificar se é par ou impar: ")
# numberConvert = int(numberIn)
# calculate = numberConvert % 2

# if calculate == 0 :
#     print("O número é par")

# else:
#     print("O número é impar")



# 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos;
# Adulto: acima de 18 anos.

# IdadeIn = input("Insira a sua idade: ")
# IdadeInt = int(IdadeIn)

# if IdadeInt <= 12:
#     print("Você é uma criança")
# elif IdadeInt >= 13 and IdadeInt <=18:
#     print("Você é um Adolescente")
# elif IdadeInt > 18 and IdadeInt <120:
#     print("Você é um Adulto")
# elif IdadeInt > 120:
#     print("Você está brincando com a minha cara?")

# else:
#     print("Valor não identificado")


# 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

# user = "Admin"
# password = 1234

# userIn = input("Insira o nome de usuario: ")
# passworIn = input("Insira a senha: ")

# passwordConv = int(passworIn)

# if userIn != user and passwordConv != password:
#     print("Acesso negado")

# else:
#     print("Bem vindo ao sistema")

# 4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

# Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
# Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
# Terceiro Quadrante: os valores de x e y devem ser menores que zero;
# Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
# Caso contrário: o ponto está localizado no eixo ou origem.

# xInput = input("Insira o valor de X: ")
# yInput = input("Insira o valor de Y: ")

# xInt = int(xInput)
# yInt = int(yInput)

# if xInt > 0 and yInt > 0:
#     print("Primeiro Quadrante")
# elif xInt < 0 and yInt > 0:
#     print("Segundo Quadrante")
# elif xInt < 0 and yInt < 0:
#     print("Terceiro Quadrante")
# elif xInt > 0 and yInt < 0:
#     print("Quarto Quadrante")

# else:
#     print(" O ponto está localizado no eixo ou origem")