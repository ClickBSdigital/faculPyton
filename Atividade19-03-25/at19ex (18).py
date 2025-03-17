# Ex 05. Strings 
# Faça um programa que leia um nome e imprima 
# apenas a letra do primeiro nome em maiúsculo.


nome = input("Digite um nome completo: ")

primeira_letra = nome.split()[0][0].upper()

print(f"A primeira letra do primeiro nome em maiúsculo é: {primeira_letra}")

