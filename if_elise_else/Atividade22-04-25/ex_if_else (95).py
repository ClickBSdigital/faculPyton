# 95 - Verifique se todos os dígitos de um número são pares
num = input("Digite um número: ")

if all(int(d) % 2 == 0 for d in num):
    print("Todos os dígitos são pares.")
else:
    print("Nem todos os dígitos são pares.")
