# 87 - Verifique se o número possui dígitos repetidos
n = input("Digite um número: ")

if len(set(n)) < len(n):
    print("O número possui dígitos repetidos.")
else:
    print("Todos os dígitos são únicos.")
