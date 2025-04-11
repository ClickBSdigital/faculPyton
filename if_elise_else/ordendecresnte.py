# faça um programa que leia três numeros e mostre-os 
# em ordem decrecente.
# Programa que lê três números e mostra em ordem decrescente

# Entrada de dados
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

# Coloca os números em uma lista
numeros = [num1, num2, num3]

# Ordena a lista em ordem decrescente
numeros.sort(reverse=True)

# Mostra os números
print("Números em ordem decrescente:", numeros)
