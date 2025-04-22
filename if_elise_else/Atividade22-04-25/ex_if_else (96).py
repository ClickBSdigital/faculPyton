# 96 - Verifique se todos os dígitos de um número são ímpares
num = input("Digite um número: ")

if all(int(d) % 2 != 0 for d in num):
    print("Todos os dígitos são ímpares.")
else:
    print("Nem todos os dígitos são ímpares.")


# =======================================

# 96 - Verifique se um número é divisível por 2, 3 e 5
numero = int(input("Digite um número: "))
if numero % 2 == 0 and numero % 3 == 0 and numero % 5 == 0:
    print("O número é divisível por 2, 3 e 5.")
else:
    print("O número NÃO é divisível por 2, 3 e 5.")