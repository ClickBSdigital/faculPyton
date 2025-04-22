# Verifique se um número é múltiplo de 4 e não é múltiplo de 8
numero = int(input("Digite um número: "))

if numero % 4 == 0 and numero % 8 != 0:
    print("O número é múltiplo de 4 e não é múltiplo de 8.")
else:
    print("O número não atende à condição.")
