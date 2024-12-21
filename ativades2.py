# 1 - Crie uma lista para cada informação a seguir:

# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.

# numeros = [1,2,3,4,5,6,7,8,9,10]
# nomes = ['Rafael','João','Maria','José']
# anos = [2001,2024]

# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
# numeros = [1,2,3,4,5,6,7,8,9,10]
# for numero in numeros:
#     print(numero)
# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# soma = 0  # Inicializa a variável soma

# for numero in numeros:
#     if numero % 2 != 0:  
#         soma += numero  

# print("A soma dos números ímpares de 1 a 10 é:", soma)

    

# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.
# for numero in range(10,0,-1):
#     print(numero)

# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
# numeroInput = input("Insira um número número: ")
# numero = int(numeroInput)

# for i in range(1,11,1):
#     multi = numero * i
#     print(f'A multiplicação de {numero} por {i} é {multi}')
# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.
# Cria uma lista de números
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# soma = 0
# try:
#     for numero in numeros:
#         soma += numero  # Soma cada elemento da lista
#     print(f"A soma dos números é: {soma}")
# except TypeError as e:
#     print(f"Erro: Um dos elementos na lista não é um número. Detalhes: {e}")
# except Exception as e:
#     print(f"Ocorreu um erro inesperado: {e}")


# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
# Lista de valores
valores = [10, 20, 30, 40, 50]  # Você pode substituir ou deixar vazia para testar o caso de exceção

try:
    # Verifica se a lista está vazia
    if len(valores) == 0:
        raise ValueError("A lista está vazia. Não é possível calcular a média.")
    
    # Calcula a soma e a média
    soma = sum(valores)
    media = soma / len(valores)
    
    print(f"A média dos valores é: {media:.2f}")
    
except ZeroDivisionError:
    print("Erro: Tentativa de divisão por zero. Certifique-se de que a lista contém elementos.")
except ValueError as e:
    print(f"Erro: {e}")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")

