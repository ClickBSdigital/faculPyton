# 7. Dado N números, mostrar maior, menor e soma (sem sum/media/prontos)

n = int(input("Quantos números deseja digitar? "))

soma = 0
maior = menor = int(input("Digite um número: "))
soma += maior

for _ in range(n - 1):
    num = int(input("Digite um número: "))
    soma += num
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print("Maior número:", maior)
print("Menor número:", menor)
print("Soma total:", soma)