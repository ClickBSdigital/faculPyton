# 78 - Verifique se um número está fora de um intervalo (ex: menor que 10 ou maior que 100)
num = int(input("Digite um número: "))

if num < 10 or num > 100:
    print("O número está fora do intervalo de 10 a 100.")
else:
    print("O número está dentro do intervalo de 10 a 100.")
