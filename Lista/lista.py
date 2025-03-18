# Listas em Python são uma estrutura de dados que armazena múltiplos itens em uma única variável. Elas podem conter diferentes tipos de dados, como números, strings, listas ou até objetos complexos. Uma lista é criada utilizando colchetes [], e os elementos são separados por vírgulas.

# Exemplo básico de lista:

# # Criando uma lista
# minha_lista = [1, 2, 3, 4, 5]
# print(minha_lista)
# Acessando elementos:
# Você pode acessar elementos da lista utilizando índices. Lembre-se de que os índices começam em 0.


# # Acessando o primeiro elemento (índice 0)
# print(minha_lista[0])  # Saída: 1
# Modificando elementos:
# Você pode alterar os elementos de uma lista diretamente.


# # Modificando o terceiro elemento (índice 2)
# minha_lista[2] = 10
# print(minha_lista)  # Saída: [1, 2, 10, 4, 5]
# Métodos úteis de listas:
# append(): Adiciona um item ao final da lista.
# insert(): Insere um item em uma posição específica.
# remove(): Remove a primeira ocorrência de um item.
# pop(): Remove e retorna um item de uma posição específica.
# sort(): Ordena a lista.
# reverse(): Inverte a ordem dos elementos.
# Exemplo de uso de métodos:

# # Adicionando elementos
# minha_lista.append(6)
# print(minha_lista)  # Saída: [1, 2, 10, 4, 5, 6]

# # Inserindo um elemento na posição 1
# minha_lista.insert(1, 15)
# print(minha_lista)  # Saída: [1, 15, 2, 10, 4, 5, 6]

# # Removendo o número 10
# minha_lista.remove(10)
# print(minha_lista)  # Saída: [1, 15, 2, 4, 5, 6]

# # Ordenando a lista
# minha_lista.sort()
# print(minha_lista)  # Saída: [1, 2, 4, 5, 6, 15]

# # Invertendo a lista
# minha_lista.reverse()
# print(minha_lista)  # Saída: [15, 6, 5, 4, 2, 1]
# Listas aninhadas:
# Você pode criar listas dentro de outras listas, formando listas aninhadas.


# # Lista aninhada
# lista_aninhada = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(lista_aninhada[0])  # Saída: [1, 2, 3]
# print(lista_aninhada[0][1])  # Saída: 2

lista1 = [10, 20, 30, 40]
lista2 = ["apam","buerger","chess"]
print(lista1, lista2)
print(type(lista1))