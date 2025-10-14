# 13 – Crie uma função que retorne uma lista com valor
# padrão. Para esta função, consideraremos como argumentos
# de entrada a quantidade de elementos e o valor padrão a
# ser atribuído a todos eles. Exemplo de retorno:
# [1,1,1,1,1,1,1,1]
# [“A”,”A”,”A”,”A”]

def criar_lista(qtd_elementos, valor_padrao):
    lista = [valor_padrao] * qtd_elementos  # multiplica o valor pelo número de elementos
    return lista

# Exemplos de uso:
numeros = criar_lista(8, 1)
print(numeros)  # Saída: [1, 1, 1, 1, 1, 1, 1, 1]

letras = criar_lista(4, "A")
print(letras)  # Saída: ['A', 'A', 'A', 'A']
