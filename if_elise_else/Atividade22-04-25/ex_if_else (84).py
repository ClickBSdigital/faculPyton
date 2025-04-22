# 84 - Verifique se um número é um cubo perfeito
num = int(input("Digite um número: "))
raiz_cubo = round(num ** (1/3))

if raiz_cubo ** 3 == num:
    print("O número é um cubo perfeito.")
else:
    print("O número não é um cubo perfeito.")
