# Ex 08. Strings
# Faça um programa que leia um nome completo de uma
# pessoa e imprima a frequência de ocorrência da letra a.

nome = input("Digite um nome completo: ")

frequencia_a = nome.lower().count('a')

print(f"A letra 'a' aparece {frequencia_a} vezes no nome.")
