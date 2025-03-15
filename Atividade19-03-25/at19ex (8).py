# Ex 02. Strings
# Tamanho de strings. Faça um programa que leia 2 strings e
# informe o conteúdo delas seguido do seu comprimento.

str1 = input("Digite a primeira satring: ")
str2 = input("Digite a segunda string: ")

tam1 = len(str1)
tam2 = len(str2)

print("\n--- Resultados ---")
print(f"String 1: \"{str1}\" - Tamanho: {tam1} caracteres")
print(f"String 2: \"{str2}\" - Tamanho: {tam2} caracteres")