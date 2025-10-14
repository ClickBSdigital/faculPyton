# 11 - Crie uma função que receba como argumento uma lista, com
# valores de qualquer tipo. A função deve imprimir todos os
# elementos da lista numerando-os. Exemplo:
# 1, Pera
# 2, Uva
# 3, Maça
# 4, Salada mista

def imprimir_lista(lista):
    for i, valor in enumerate(lista, start=1):
        print(f"{i}, {valor}")

# Exemplo de uso:
itens = ["Pera", "Uva", "Maçã", "Salada mista"]
imprimir_lista(itens)