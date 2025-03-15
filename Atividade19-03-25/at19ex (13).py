# Ex 07. Strings
# Faça um programa que leia um nome completo de uma
# pessoa e imprima do índice 0 ao índice 8 (inclusive).

nome =  input("Digite um nome completo: ")

substring = nome[:9]

print(f"Os caracteres do índice 0 ao 8 sao: {substring}")