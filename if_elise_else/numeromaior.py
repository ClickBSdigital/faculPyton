# faça um programa que peça dois numeros 
# e imprima o maior deles:

num1 = float(input("Digite um numero: "))
num2 = float(input("Digite outro numero: "))

if num1 > num2:
    print(f"O maior número é: {num1}")
elif num2 > num1:
    print(f"O maior número é: {num2}")
else:
    print("Os dois numeros são iguais. ")