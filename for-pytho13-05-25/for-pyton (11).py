# 11. Acidentes em 5 cidades – menor índice

menor_indice = None
codigo_menor = 0

for i in range(5):
    codigo = int(input("Código da cidade: "))
    veiculos = int(input("Nº de veículos de passeio: "))
    acidentes = int(input("Nº de acidentes com vítimas: "))
    
    indice = acidentes / veiculos if veiculos > 0 else float('inf')
    
    if menor_indice is None or indice < menor_indice:
        menor_indice = indice
        codigo_menor = codigo

print(f"Cidade com menor índice de acidentes: {codigo_menor} (índice: {menor_indice:.2f})")