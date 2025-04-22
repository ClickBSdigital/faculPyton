# 59 – Verifique se um número está fora do intervalo de 0 a 100
valor = int(input("Digite um número: "))

if valor < 0 or valor > 100:
    print("O número está fora do intervalo de 0 a 100.")
else:
    print("O número está dentro do intervalo de 0 a 100.")
