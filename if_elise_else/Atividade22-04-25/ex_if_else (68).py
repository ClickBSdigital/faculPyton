# Verifique se um número está fora do intervalo de 20 a 50 e é múltiplo de 3
num = int(input("Digite um número: "))

if (num < 20 or num > 50) and num % 3 == 0:
    print("O número está fora do intervalo de 20 a 50 e é múltiplo de 3.")
else:
    print("A condição não foi atendida.")
