# 15. Ler 10 números e mostrar pares, ímpares e soma

pares = impares = soma = 0

for _ in range(10):
    num = int(input("Digite um número: "))
    soma += num
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Quantidade de pares: {pares}")
print(f"Quantidade de ímpares: {impares}")
print(f"Soma total: {soma}")