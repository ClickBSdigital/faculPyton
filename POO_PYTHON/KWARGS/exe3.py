# **KWARGS
def concatena (**kwargs):
 print(f'Valores recebidos: {kwargs}')
 resultado = ""
 for valor in kwargs.values():
  resultado += f'{valor} '
 return resultado
print(concatena(a="Python", b="Academy", c="Rules!"))



# =================================
# Vamos analisar detalhadamente esse código que usa **kwargs e concatenar valores. Vou explicar linha por linha.

# 1️⃣ O que é **kwargs

# **kwargs permite que a função receba qualquer quantidade de argumentos nomeados (chave=valor).

# Internamente, o Python cria um dicionário com esses argumentos, onde:

# Chave = nome do argumento (a, b, c)

# Valor = valor passado ("Python", "Academy", "Rules!")

# 2️⃣ Código original
# def concatena(**kwargs):
#     print(f'Valores recebidos: {kwargs}')  # imprime o dicionário completo
#     resultado = ""
    
#     for valor in kwargs.values():          # percorre apenas os valores do dicionário
#         resultado += f'{valor} '          # adiciona cada valor à string, com espaço
    
#     return resultado                       # retorna a string final

# print(concatena(a="Python", b="Academy", c="Rules!"))

# 3️⃣ Explicação linha a linha
# Linha 1: definição da função
# def concatena(**kwargs):


# Função concatena recebe qualquer número de argumentos nomeados.

# Exemplo de chamada: concatena(a="Python", b="Academy", c="Rules!").

# Internamente:

# kwargs = {'a': 'Python', 'b': 'Academy', 'c': 'Rules!'}

# Linha 2: imprime os valores recebidos
# print(f'Valores recebidos: {kwargs}')


# Mostra o dicionário completo que foi recebido.

# Saída nesse exemplo:

# Valores recebidos: {'a': 'Python', 'b': 'Academy', 'c': 'Rules!'}

# Linha 3: inicializa a string resultado
# resultado = ""


# Criamos uma variável vazia resultado que vai armazenar todos os valores concatenados.

# Linha 4-5: percorre os valores e concatena
# for valor in kwargs.values():
#     resultado += f'{valor} '


# kwargs.values() pega todos os valores do dicionário ("Python", "Academy", "Rules!").

# resultado += f'{valor} ' → adiciona cada valor à string final, com um espaço entre eles.

# Resultado parcial da concatenação: "Python Academy Rules! "

# Linha 6: retorna a string final
# return resultado


# Retorna a string concatenada com todos os valores passados.

# No exemplo, o retorno é:

# "Python Academy Rules! "

# Linha 7: chamada da função
# print(concatena(a="Python", b="Academy", c="Rules!"))


# Imprime o retorno da função.

# Saída final no console:

# Valores recebidos: {'a': 'Python', 'b': 'Academy', 'c': 'Rules!'}
# Python Academy Rules! 


# 📌 Observação: você pode usar resultado.strip() antes de retornar para remover o espaço extra no final.

# 4️⃣ Resumo do conceito

# **kwargs → argumentos nomeados, transformados em dicionário dentro da função.

# .values() → pega apenas os valores do dicionário.

# É útil quando queremos processar argumentos opcionais sem saber previamente seus nomes.

# Permite criar funções muito flexíveis.