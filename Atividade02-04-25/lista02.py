# dadas duas listas P1 e P2, ambas com n valores reais que representam
# as notas de uma turma na prova 1 e na prova 2, respactivamente, escreva
# um programa que calcule a média da turma nas provas 1 e 2,
# imprimindo as médias. o programa tem que receber as notas 
# de qualquer numero e se for fornecido mais notas em qualquer uma das 
# provas o programas continua a somar.
# ex: tamano da turma:
#     P1: 7.0, 8.3, 10.0, 6.5, 9.3 
#     P2: 8.5, 6.9, 5.0, 9.8
    
#     médoa da turma na prova 1: 8.22
#     média da turma na prova2: 7.54

# Criando listas vazias para armazenar as notas
P1 = []
P2 = []

# Solicitando notas da Prova 1
print("Digite as notas da Prova 1 (ou pressione Enter para finalizar):")
while True:
    nota = input()
    if nota == "":
        break
    try:
        P1.append(float(nota))
    except ValueError:
        print("Entrada inválida! Digite um número válido.")

# Solicitando notas da Prova 2
print("Digite as notas da Prova 2 (ou pressione Enter para finalizar):")
while True:
    nota = input()
    if nota == "":
        break
    try:
        P2.append(float(nota))
    except ValueError:
        print("Entrada inválida! Digite um número válido.")

# Calculando médias
media_P1 = sum(P1) / len(P1) if len(P1) > 0 else 0
media_P2 = sum(P2) / len(P2) if len(P2) > 0 else 0

# Exibindo resultados
print(f"Média da turma na Prova 1: {media_P1:.2f}")
print(f"Média da turma na Prova 2: {media_P2:.2f}")
