# 10. Panificadora: preço do pão até 50 unidades

preco = float(input("Digite o preço do pão: R$ "))

print("Panificadora Pão Quente - Tabela de preços")
for i in range(1, 51):
    print(f"{i} - R$ {preco * i:.2f}")