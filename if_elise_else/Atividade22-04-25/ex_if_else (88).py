# 88 - Verifique se o número possui todos os dígitos em ordem crescente
numero = input("Digite um número: ")

if list(numero) == sorted(numero):
    print("Os dígitos estão em ordem crescente.")
else:
    print("Os dígitos não estão em ordem crescente.")
