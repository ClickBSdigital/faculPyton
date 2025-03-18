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

# Uma lista "alinhada" geralmente se refere a uma lista onde os elementos estão organizados ou alinhados de forma visualmente clara e consistente, podendo ser útil para melhorar a legibilidade, especialmente ao imprimir ou manipular dados em um formato tabular.

# Aqui está um exemplo de como você pode criar uma lista de números ou strings e alinhá-los para melhorar a visualização, utilizando a formatação de strings em Python:

# Exemplo 1: Alinhando números em uma lista
# Se você tem uma lista de números e deseja alinhá-los para que fiquem na mesma coluna ao serem impressos, pode usar a formatação de strings com a função format() ou f-strings.

# python
# Copiar
# Editar
# # Lista de números
# numeros = [12, 345, 6789, 12345, 678901]

# # Alinhando à direita com largura de 10 caracteres
# for num in numeros:
#     print(f"{num:>10}")  # Alinha à direita com espaço de 10 caracteres
# Saída:

# markdown
# Copiar
# Editar
#        12
#       345
#      6789
#     12345
#    678901
# Exemplo 2: Alinhando strings em uma lista
# Agora, se você tem uma lista de strings e quer alinhá-las à esquerda ou ao centro, também pode usar formatação:

# python
# Copiar
# Editar
# # Lista de strings
# nomes = ["Alice", "Bob", "Carlos", "Diana", "Eduarda"]

# # Alinhando à esquerda com largura de 10 caracteres
# for nome in nomes:
#     print(f"{nome:<10}")  # Alinha à esquerda

# # Alinhando ao centro com largura de 10 caracteres
# for nome in nomes:
#     print(f"{nome:^10}")  # Alinha ao centro
# Saída (alinhamento à esquerda):

# nginx
# Copiar
# Editar
# Alice     
# Bob       
# Carlos    
# Diana     
# Eduarda   
# Saída (alinhamento ao centro):

# nginx
# Copiar
# Editar
#   Alice   
#    Bob    
#   Carlos  
#   Diana   
#  Eduarda  
# Exemplo 3: Alinhando em uma tabela
# Você pode criar uma tabela onde tanto números quanto strings são alinhados corretamente:

# python
# Copiar
# Editar
# # Lista de dados
# dados = [
#     ["Nome", "Idade", "Profissão"],
#     ["Alice", 28, "Engenheira"],
#     ["Bob", 35, "Médico"],
#     ["Carlos", 40, "Professor"],
#     ["Diana", 22, "Estudante"]
# ]

# # Alinhando a tabela
# for linha in dados:
#     print(f"{linha[0]:<10} {linha[1]:>5} {linha[2]:<12}")
# Saída:

# nginx
# Copiar
# Editar
# Nome       Idade Profissão  
# Alice         28 Engenheira
# Bob           35 Médico    
# Carlos        40 Professor 
# Diana         22 Estudante 
# Detalhes sobre o alinhamento:
# <: Alinha à esquerda.
# >: Alinha à direita.
# ^: Alinha ao centro.
# O número após o : define a largura do campo (por exemplo, 10 para 10 caracteres).
# Esses são alguns exemplos de como alinhar listas de maneira eficiente para garantir uma boa apresentação dos dados. Se precisar de mais ajuda com algo específico, é só falar!







# Você disse:
# lista de lista
# O ChatGPT disse:
# Uma lista de listas em Python é simplesmente uma lista onde cada elemento é uma outra lista. Isso cria uma estrutura de dados bidimensional (ou "matriz") que pode ser útil para representar tabelas, matrizes matemáticas, ou outros tipos de coleções que precisam de mais de uma dimensão.

# Exemplo básico de lista de listas:
# python
# Copiar
# Editar
# # Criando uma lista de listas
# lista_de_listas = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(lista_de_listas)
# Saída:

# lua
# Copiar
# Editar
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Acessando elementos de uma lista de listas:
# Para acessar um elemento dentro de uma lista de listas, você usa dois índices. O primeiro índice acessa a lista interna, e o segundo índice acessa o elemento dentro dessa lista.

# python
# Copiar
# Editar
# # Acessando o elemento na 2ª linha e 3ª coluna (índices 1 e 2)
# print(lista_de_listas[1][2])  # Saída: 6
# Modificando um elemento:
# Você pode modificar um valor específico dentro da lista de listas usando dois índices, da mesma forma que faz para acessar os elementos.

# python
# Copiar
# Editar
# # Modificando o elemento na 1ª linha e 2ª coluna
# lista_de_listas[0][1] = 10
# print(lista_de_listas)  # Saída: [[1, 10, 3], [4, 5, 6], [7, 8, 9]]
# Iterando sobre uma lista de listas:
# Você pode usar loops para percorrer os elementos dentro da lista de listas.

# python
# Copiar
# Editar
# # Iterando sobre a lista de listas
# for sub_lista in lista_de_listas:
#     for item in sub_lista:
#         print(item, end=' ')  # Saída: 1 10 3 4 5 6 7 8 9
#     print()  # Para quebrar linha entre as sublistas
# Exemplo com listas de diferentes tamanhos:
# As listas internas de uma lista de listas não precisam ter o mesmo tamanho.

# python
# Copiar
# Editar
# # Lista de listas com diferentes tamanhos
# lista_de_listas = [
#     [1, 2],
#     [3, 4, 5],
#     [6]
# ]

# print(lista_de_listas)  # Saída: [[1, 2], [3, 4, 5], [6]]
# Usando uma lista de listas para uma matriz:
# Uma lista de listas pode ser usada para representar uma matriz (por exemplo, uma matriz 3x3).

# python
# Copiar
# Editar
# # Matriz 3x3
# matriz = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# # Acessando um valor na 2ª linha e 1ª coluna (índices 1 e 0)
# print(matriz[1][0])  # Saída: 4
# Conclusão:
# Uma lista de listas é uma maneira muito útil de organizar 
# dados em Python, especialmente quando você precisa trabalhar com várias 
# dimensões ou quando precisa representar dados tabulares.

# Uma lista aninhada em Python é uma lista que contém outras listas como elementos. Isso cria uma estrutura de dados hierárquica ou multidimensional, onde cada elemento da lista pode ser uma lista por si só, permitindo representar dados mais complexos, como matrizes, tabelas, ou hierarquias.

# Exemplo de uma lista aninhada:
# python
# Copiar
# Editar
# # Criando uma lista aninhada (lista de listas)
# lista_aninhada = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(lista_aninhada)
# Saída:

# lua
# Copiar
# Editar
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Acessando elementos em uma lista aninhada:
# Você pode acessar os elementos das listas internas usando dois índices. O primeiro índice acessa a lista interna e o segundo índice acessa o valor dentro dessa lista.

# python
# Copiar
# Editar
# # Acessando o elemento na 2ª linha e 3ª coluna
# print(lista_aninhada[1][2])  # Saída: 6
# Modificando elementos em uma lista aninhada:
# Assim como acessar, para modificar um elemento, você usa dois índices.

# python
# Copiar
# Editar
# # Modificando o valor na 1ª linha, 2ª coluna
# lista_aninhada[0][1] = 10
# print(lista_aninhada)  # Saída: [[1, 10, 3], [4, 5, 6], [7, 8, 9]]
# Iterando sobre uma lista aninhada:
# Você pode usar loops para iterar sobre uma lista aninhada. O primeiro loop percorre as sublistas, e o segundo percorre os itens de cada sublista.

# python
# Copiar
# Editar
# # Iterando sobre a lista aninhada
# for sub_lista in lista_aninhada:
#     for item in sub_lista:
#         print(item, end=' ')  # Saída: 1 10 3 4 5 6 7 8 9
#     print()  # Quebra linha entre as sublistas
# Lista aninhada com diferentes tamanhos:
# As listas internas não precisam ter o mesmo número de elementos.

# python
# Copiar
# Editar
# # Lista aninhada com tamanhos diferentes
# lista_aninhada = [
#     [1, 2],
#     [3, 4, 5],
#     [6]
# ]

# print(lista_aninhada)  # Saída: [[1, 2], [3, 4, 5], [6]]
# Usando lista aninhada para uma matriz:
# Você pode representar uma matriz (por exemplo, uma 3x3) com uma lista aninhada.

# python
# Copiar
# Editar
# # Matriz 3x3
# matriz = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# # Acessando um elemento específico (linha 2, coluna 1)
# print(matriz[1][0])  # Saída: 4
# Conclusão:
# Listas aninhadas são uma ferramenta poderosa para organizar dados 
# mais complexos em Python. Elas são muito usadas quando você precisa de 
# uma estrutura bidimensional ou mais complexa, como uma tabela, uma matriz
# ou quando trabalha com dados hierárquicos.

# Uma lista aninhada em Python é uma lista que contém outras listas como elementos. Isso cria uma estrutura de dados hierárquica ou multidimensional, onde cada elemento da lista pode ser uma lista por si só, permitindo representar dados mais complexos, como matrizes, tabelas, ou hierarquias.

# Exemplo de uma lista aninhada:
# python
# Copiar
# Editar
# # Criando uma lista aninhada (lista de listas)
# lista_aninhada = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# print(lista_aninhada)
# Saída:

# lua
# Copiar
# Editar
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Acessando elementos em uma lista aninhada:
# Você pode acessar os elementos das listas internas usando dois índices. O primeiro índice acessa a lista interna e o segundo índice acessa o valor dentro dessa lista.

# python
# Copiar
# Editar
# # Acessando o elemento na 2ª linha e 3ª coluna
# print(lista_aninhada[1][2])  # Saída: 6
# Modificando elementos em uma lista aninhada:
# Assim como acessar, para modificar um elemento, você usa dois índices.

# python
# Copiar
# Editar
# # Modificando o valor na 1ª linha, 2ª coluna
# lista_aninhada[0][1] = 10
# print(lista_aninhada)  # Saída: [[1, 10, 3], [4, 5, 6], [7, 8, 9]]
# Iterando sobre uma lista aninhada:
# Você pode usar loops para iterar sobre uma lista aninhada. O primeiro loop percorre as sublistas, e o segundo percorre os itens de cada sublista.

# python
# Copiar
# Editar
# # Iterando sobre a lista aninhada
# for sub_lista in lista_aninhada:
#     for item in sub_lista:
#         print(item, end=' ')  # Saída: 1 10 3 4 5 6 7 8 9
#     print()  # Quebra linha entre as sublistas
# Lista aninhada com diferentes tamanhos:
# As listas internas não precisam ter o mesmo número de elementos.

# python
# Copiar
# Editar
# # Lista aninhada com tamanhos diferentes
# lista_aninhada = [
#     [1, 2],
#     [3, 4, 5],
#     [6]
# ]

# print(lista_aninhada)  # Saída: [[1, 2], [3, 4, 5], [6]]
# Usando lista aninhada para uma matriz:
# Você pode representar uma matriz (por exemplo, uma 3x3) com uma lista aninhada.

# python
# Copiar
# Editar
# # Matriz 3x3
# matriz = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# # Acessando um elemento específico (linha 2, coluna 1)
# print(matriz[1][0])  # Saída: 4
# Conclusão:
# Listas aninhadas são uma ferramenta poderosa para organizar dados mais complexos em Python. Elas são muito usadas quando você precisa de uma estrutura bidimensional ou mais complexa, como uma tabela, uma matriz ou quando trabalha com dados hierárquicos.

# Se precisar de exemplos mais específicos ou tiver dúvidas, é só falar!

# Você disse:
# len de aninha

# O comando len() em Python pode ser utilizado para obter o comprimento de uma lista, ou seja, o número de elementos presentes nela. Quando aplicamos o len() a uma lista aninhada, ele retorna a quantidade de sublistas presentes, e não a quantidade de elementos dentro das sublistas.

# Vamos ver alguns exemplos:

# Exemplo 1: Usando len() em uma lista aninhada

# # Lista aninhada
# lista_aninhada = [
#     [1, 2, 3],
#     [4, 5],
#     [6, 7, 8, 9]
# ]

# # Obter o número de sublistas
# print(len(lista_aninhada))  # Saída: 3 (porque existem 3 sublistas)
# Saída:


# 3
# O resultado é 3 porque a lista lista_aninhada contém 3 sublistas.

# Exemplo 2: Usando len() em sublistas individuais
# Se você quiser obter o número de elementos dentro de cada sublista, você pode aplicar o len() em cada sublista individualmente:


# # Obtendo o número de elementos de cada sublista
# for sub_lista in lista_aninhada:
#     print(len(sub_lista))  # Exibe o comprimento de cada sublista
# Saída:


# 3  # Número de elementos na primeira sublista
# 2  # Número de elementos na segunda sublista
# 4  # Número de elementos na terceira sublista
# Exemplo 3: Número total de elementos em todas as sublistas
# Se você quiser o número total de elementos dentro de todas as sublistas, 
# pode usar um loop para somar o comprimento de cada sublista:


# # Somando o número total de elementos em todas as sublistas
# total_elementos = sum(len(sub_lista) for sub_lista in lista_aninhada)
# print(total_elementos)  # Saída: 9 (porque 3 + 2 + 4 = 9)
# Saída:


# 9
# Conclusão:
# len(lista_aninhada) retorna o número de sublistas dentro da lista aninhada.
# len(sub_lista) retorna o número de elementos em cada sublista.
# Para calcular o número total de elementos em todas as sublistas, você pode usar 
# sum(len(sub_lista) for sub_lista in lista_aninhada).
