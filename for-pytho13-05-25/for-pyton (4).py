# 4. Mesmo anterior + soma final

inicio = int(input("Digite o primeiro número: "))
fim = int(input("Digite o segundo número: "))
soma = 0

for i in range(inicio + 1, fim):
    print(i)
    soma += i

print("Soma dos números no intervalo:", soma)