# lista = [0,1,2,3,4,5,6,7,8,9,10]
# intervalo de1 a 9;
# intervalo de 8 a 10;
# núneros pares;
# números ímpares
# liosta reserva
# Criando a lista
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. Intervalo de 1 a 9 (considerando índices)
intervalo_1_9 = lista[1:10]  # Pega do índice 1 ao 9 (o último índice 10 é excluído)

# 2. Intervalo de 8 a 10
intervalo_8_10 = lista[8:]  # Pegando do índice 8 ao 10

# 3. Números pares
numeros_pares = [num for num in lista if num % 2 == 0]

# 4. Números ímpares
numeros_impares = [num for num in lista if num % 2 != 0]

# 5. Lista reversa
lista_reversa = lista[::-1]  # Invertendo a lista

# Exibindo os resultados
print("Intervalo de 1 a 9:", intervalo_1_9)
print("Intervalo de 8 a 10:", intervalo_8_10)
print("Números pares:", numeros_pares)
print("Números ímpares:", numeros_impares)
print("Lista reversa:", lista_reversa)
