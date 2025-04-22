# 89 - Verifique se o número possui todos os dígitos em ordem decrescente
num = input("Digite um número: ")

if list(num) == sorted(num, reverse=True):
    print("Os dígitos estão em ordem decrescente.")
else:
    print("Os dígitos não estão em ordem decrescente.")
