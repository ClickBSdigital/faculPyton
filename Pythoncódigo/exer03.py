# nome = input("Digite seu nome: ")
# print("O nome digitado foi: ",nome)

# idade = input("Digite sua idade: ")
# print(type(idade))

salario = int(input('Salario?: '))
print('seu salario é: ',salario)

imposto = float(input('Digite o imposto: '))
print('o imposto foi: ',imposto)

aumento = (salario * imposto) / 100

soma = salario + aumento
print('Seu salario de: ',salario,', com o impostto de: ',imposto,', fica um total de: ',soma)

print('O salario digitado foi %d'%salario)