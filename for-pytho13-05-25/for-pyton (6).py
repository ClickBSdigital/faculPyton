# 6. Ler 5 números, exibir soma e média (sem lista, len ou sum)

soma = 0
for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    soma += num

media = soma / 5
print("Soma:", soma)
print("Média:", media)