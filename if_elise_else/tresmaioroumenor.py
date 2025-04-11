# faça um programa que leia 
# três numeros e mostre o maior e o menor deles
# Programa para encontrar o maior, o menor e o número do meio

# Lendo os três números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if num1 == num2 == num3:
    print("Todos os números são iguais:", num1)
else:
    # Verificando o maior número
    maior = num1
    if num2 > maior:
        maior = num2
    if num3 > maior:
        maior = num3

    # Verificando o menor número
    menor = num1
    if num2 < menor:
        menor = num2
    if num3 < menor:
        menor = num3

    # Encontrando o número do meio
    if (num1 != maior and num1 != menor):
        medio = num1
    elif (num2 != maior and num2 != menor):
        medio = num2
    else:
        medio = num3

    print("Menor:", menor)
    print("Médio:", medio)
    print("Maior:", maior)
