# fazer um algorítimo que ao receber o salario de um 
# funcionário, calcule o valor do novo salário reajustado
# de acordo com a tabela abaixo:
#     salario atual 
#     Abaixo de R$500.00 reajuste de 15%
#     de R$500,00 até R$ 1000.00 reajuste de 10%
#     Acima de R$1000.00 reajuste de 5%
# Solicita o salário atual
salario = float(input("Digite o salário atual do funcionário: R$ "))

# Aplica o reajuste conforme a faixa salarial
if salario < 500:
    novo_salario = salario * 1.15
elif salario <= 1000:
    novo_salario = salario * 1.10
else:
    novo_salario = salario * 1.05

# Exibe o resultado
print("O novo salário reajustado é: R$ {:.2f}".format(novo_salario))
