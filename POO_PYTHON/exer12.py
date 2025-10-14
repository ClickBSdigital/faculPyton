# 12 - Crie uma função que receba uma lista
# como argumento, os valores da lista devem ser
# numéricos, por fim retorne a média desses
# valores.

def calcular_media(lista):
    if len(lista) == 0:  # evita divisão por zero
        return 0
    
    soma = sum(lista)        # soma todos os elementos
    media = soma / len(lista)  # divide pela quantidade
    return media

# Exemplo de uso:
numeros = [10, 20, 30, 40, 50]
resultado = calcular_media(numeros)
print("Média:", resultado)
