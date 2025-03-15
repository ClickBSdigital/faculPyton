# Ex 04. Strings
# Faça um programa que leia um nome e imprima as 4
# primeiras letras do nome.

nome = input("Digite um nome: ")

if len(nome) >= 4:
    primeiras_letras = nome[:4]
else:
    primeiras_letras = nome

print(f"As 4 primeiras letras do nome sao: {primeiras_letras}")