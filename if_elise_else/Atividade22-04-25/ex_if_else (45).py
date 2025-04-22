# 45 – Verifique se um número é múltiplo de 3 e 5 ao mesmo tempo
num = int(input("Digite um número: "))

if num % 3 == 0 and num % 5 == 0:
    print("O número é múltiplo de 3 e 5 ao mesmo tempo.")
else:
    print("O número não é múltiplo de 3 e 5 ao mesmo tempo.")
