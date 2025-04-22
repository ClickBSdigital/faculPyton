# Verifique se um número está entre 0 e 50 e é par
valor = int(input("Digite um número: "))

if 0 <= valor <= 50 and valor % 2 == 0:
    print("O número está entre 0 e 50 e é par.")
else:
    print("A condição não foi atendida.")
