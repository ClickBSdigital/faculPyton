# 11 - As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o
# seguinte critério, baseado no salário atual:
# salários até R$ 280,55 (incluindo) : aumento de 22,51%
# salários entre R$ 280,55 e R$ 709,72(incluindo) : aumento de 15,39%
# salários entre R$ 709,72 e R$ 1501,33(incluindo) : aumento de 10,97%
# salários de R$ 1501,33 em diante : aumento de 5,19% Após o aumento ser realizado,
# informe na tela:
# o salário antes do reajuste;o percentual de aumento aplicado;o valor do aumento;
# o novo salário, após o aumento.
# Programa para calcular o reajuste salarial

# Entrada: ler o salário atual do colaborador
salario = float(input("Digite o salário atual do colaborador: R$ "))

# Verifica qual percentual de aumento aplicar
if salario <= 280.55:
    percentual = 20.51
elif salario <= 709.72:
    percentual = 15.39
elif salario <= 1501.33:
    percentual = 10.97
else:
    percentual = 5.19

# Calcula o valor do aumento
aumento = salario * (percentual / 100)

# Calcula o novo salário
novo_salario = salario + aumento

# Exibe os resultados
print("\n===== REAJUSTE SALARIAL =====")
print("Salário antes do reajuste: R$ {:.2f}".format(salario))
print("Percentual de aumento aplicado: {}%".format(percentual))
print("Valor do aumento: R$ {:.2f}".format(aumento))
print("Novo salário, após o aumento: R$ {:.2f}".format(novo_salario))
