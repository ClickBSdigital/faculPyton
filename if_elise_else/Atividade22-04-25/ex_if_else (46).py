# 46 – Verifique se um número é par e positivo
valor = int(input("Digite um número: "))

if valor % 2 == 0 and valor > 0:
    print("O número é par e positivo.")
else:
    print("O número não é par e positivo.")
