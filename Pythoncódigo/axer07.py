# explique len, capitalize, casefold, lower, upper, islower, isupper detatlado passo a passo 
# O ChatGPT disse:
# Aqui está uma explicação detalhada, passo a passo, de cada uma dessas funções em Python:

# 📌 len()
# A função len() retorna o número de caracteres de uma string (ou o tamanho de uma lista, tupla, dicionário, etc.).

# Sintaxe:

# python
# Copiar
# Editar
# len(string)
# Exemplo:

# python
# Copiar
# Editar
# texto = "Python"
# tamanho = len(texto)
# print(tamanho)  # Saída: 6
# 👉 Conta todos os caracteres, incluindo espaços.

# 📌 capitalize()
# A função capitalize() transforma o primeiro caractere da string em maiúscula e todos os outros em minúsculas.

# Sintaxe:

# python
# Copiar
# Editar
# string.capitalize()
# Exemplo:

# python
# Copiar
# Editar
# texto = "python é incrível!"
# novo_texto = texto.capitalize()
# print(novo_texto)  # Saída: "Python é incrível!"
# 👉 Apenas a primeira letra da string fica maiúscula.

# 📌 casefold()
# A função casefold() converte a string para minúsculas, mas de forma mais forte que lower(), pois lida melhor com caracteres especiais e diferentes alfabetos.

# Sintaxe:

# python
# Copiar
# Editar
# string.casefold()
# Exemplo:

# python
# Copiar
# Editar
# texto = "MÜLLER"
# novo_texto = texto.casefold()
# print(novo_texto)  # Saída: "müller"
# 👉 casefold() é mais poderoso que lower(), pois considera variações linguísticas.

# 📌 lower()
# A função lower() transforma todos os caracteres da string em minúsculas.

# Sintaxe:

# python
# Copiar
# Editar
# string.lower()
# Exemplo:

# python
# Copiar
# Editar
# texto = "PYTHON É INCRÍVEL!"
# novo_texto = texto.lower()
# print(novo_texto)  # Saída: "python é incrível!"
# 👉 Funciona bem, mas casefold() pode ser mais eficaz para comparações sem diferenciar maiúsculas e minúsculas.

# 📌 upper()
# A função upper() transforma todos os caracteres da string em maiúsculas.

# Sintaxe:

# python
# Copiar
# Editar
# string.upper()
# Exemplo:

# python
# Copiar
# Editar
# texto = "Python é incrível!"
# novo_texto = texto.upper()
# print(novo_texto)  # Saída: "PYTHON É INCRÍVEL!"
# 👉 Todas as letras são convertidas para maiúsculas.

# 📌 islower()
# A função islower() verifica se todos os caracteres da string estão em minúsculas. Retorna True se estiverem e False caso contrário.

# Sintaxe:

# python
# Copiar
# Editar
# string.islower()
# Exemplo:

# python
# Copiar
# Editar
# texto1 = "python"
# print(texto1.islower())  # Saída: True

# texto2 = "Python"
# print(texto2.islower())  # Saída: False
# 👉 Se houver pelo menos uma letra maiúscula, retorna False.

# 📌 isupper()
# A função isupper() verifica se todos os caracteres da string estão em maiúsculas. Retorna True se estiverem e False caso contrário.

# Sintaxe:

# python
# Copiar
# Editar
# string.isupper()
# Exemplo:

# python
# Copiar
# Editar
# texto1 = "PYTHON"
# print(texto1.isupper())  # Saída: True

# texto2 = "Python"
# print(texto2.isupper())  # Saída: False
# 👉 Se houver pelo menos uma letra minúscula, retorna False.

# 🚀 Resumo rápido:
# Função	O que faz?
# len()	Retorna o tamanho da string.
# capitalize()	Primeira letra maiúscula, resto minúsculo.
# casefold()	Converte para minúsculas (mais forte que lower).
# lower()	Converte para minúsculas.
# upper()	Converte para maiúsculas.
# islower()	Verifica se a string está toda em minúsculas.
# isupper()	Verifica se a string está toda em maiúsculas.
# isdigit() verifica se uma string só possui números inteiros
# replace() troca todas as ocorrencias de uma string
# Quer mai


a ="ederson"

print(a.upper())

q= a.upper
print(q)

B = "EDERSON"
print(B.casefold())

b = "EDERSON"
print(b.lower())

C = "EDERSON"
print(C.islower())

C1 = "EDERSON"
print(C1.isupper())

w = "123456"
print(w.isdigit())

w1 = "12345fd6"
print(w1.isdigit())

w12 = "Eliandro Silva"
print(w12.replace("Silva","Costa"))

w13 = "Eliandro-Silva-Costa"
print(w13.split("-"))

# 📌 split()
# A função split() divide uma string em partes (substrings) com base em um separador e retorna uma lista com essas partes.

# 🛠️ Sintaxe:

# string.split(separador, maxsplit)
# separador (opcional): O caractere que será usado para dividir a string. Se não for informado, a separação será feita nos espaços em branco.
# maxsplit (opcional): O número máximo de divisões a serem feitas. O padrão é dividir tudo.
# 🏷️ Exemplos Práticos
# ✅ Exemplo 1: Sem especificar um separador

# texto = "Python é incrível"
# partes = texto.split()
# print(partes)  # Saída: ['Python', 'é', 'incrível']
# 👉 Quando não passamos um separador, a string é dividida pelos espaços.

# ✅ Exemplo 2: Usando um separador específico

# texto = "banana,maçã,laranja"
# frutas = texto.split(",")
# print(frutas)  # Saída: ['banana', 'maçã', 'laranja']
# 👉 Aqui, usamos a vírgula como separador.

# ✅ Exemplo 3: Limitando a quantidade de divisões (maxsplit)

# texto = "Python é uma linguagem poderosa"
# partes = texto.split(" ", 2)
# print(partes)  # Saída: ['Python', 'é', 'uma linguagem poderosa']
# 👉 Apenas duas divisões foram feitas. O restante da string permanece como o último elemento da lista.

# ✅ Exemplo 4: Dividindo uma string por uma quebra de linha (\n)

# texto = "Linha 1\nLinha 2\nLinha 3"
# linhas = texto.split("\n")
# print(linhas)  # Saída: ['Linha 1', 'Linha 2', 'Linha 3']
# 👉 Separação feita por quebras de linha.

# 🚀 Resumo Rápido
# Método	O que faz?
# split()	Divide a string em partes com base em um separador e retorna uma lista.
# split("X")	Divide a string onde encontrar "X".
# split("X", N)	Divide a string no máximo N vezes.
# split()	Separa pelos espaços por padrão.


r = "Eliandro Ap. Elias da Silva"
print(r.find("Silva"))


# 📌 find()
# A função find() procura um substring dentro de uma string e retorna o índice da primeira ocorrência encontrada. Se a substring não for encontrada, retorna -1.

# 🛠️ Sintaxe:

# string.find(substring, start, end)
# substring (obrigatório): O trecho que queremos encontrar.
# start (opcional): A posição inicial para a busca. Se omitido, começa do início da string.
# end (opcional): A posição final para a busca. Se omitido, vai até o final da string.
# 🏷️ Exemplos Práticos
# ✅ Exemplo 1: Encontrando um trecho dentro da string

# texto = "Python é incrível"
# indice = texto.find("é")
# print(indice)  # Saída: 7
# 👉 O caractere "é" aparece na posição 7 (contagem começa do zero).

# ✅ Exemplo 2: Quando o trecho não é encontrado

# texto = "Python é incrível"
# indice = texto.find("Java")
# print(indice)  # Saída: -1
# 👉 Como "Java" não está na string, find() retorna -1.

# ✅ Exemplo 3: Usando os parâmetros start e end

# texto = "banana, maçã, laranja, banana"
# indice = texto.find("banana", 10)  
# print(indice)  # Saída: 23
# 👉 Aqui, buscamos "banana" a partir da posição 10.
# 👉 A segunda ocorrência de "banana" começa na posição 23.

# 🚀 Resumo Rápido
# Método	O que faz?
# find("X")	Retorna a posição de "X" na string, ou -1 se não encontrar.
# find("X", start)	Começa a busca na posição start.
# find("X", start, end)	Busca entre as posições start e end.


# 📌 rfind()
# A função rfind() funciona da mesma forma que find(), mas busca a última ocorrência da substring na string.

# 🛠️ Sintaxe:
# python
# Copiar
# Editar
# string.rfind(substring, start, end)
# substring (obrigatório): O trecho que queremos encontrar.
# start (opcional): A posição inicial para a busca. Se omitido, começa do início da string.
# end (opcional): A posição final para a busca. Se omitido, vai até o final da string.
# 🏷️ Exemplos Práticos
# ✅ Exemplo 1: Encontrando a última ocorrência de um trecho
# python
# Copiar
# Editar
# texto = "banana, maçã, laranja, banana"
# indice = texto.rfind("banana")
# print(indice)  # Saída: 23
# 👉 "banana" aparece duas vezes:

# Índice 0 (primeira ocorrência)
# Índice 23 (última ocorrência, retornada por rfind())
# ✅ Exemplo 2: Quando o trecho não é encontrado
# python
# Copiar
# Editar
# texto = "Python é incrível"
# indice = texto.rfind("Java")
# print(indice)  # Saída: -1
# 👉 Como "Java" não está na string, rfind() retorna -1.

# ✅ Exemplo 3: Usando start e end
# python
# Copiar
# Editar
# texto = "banana, maçã, laranja, banana"
# indice = texto.rfind("banana", 0, 20)  
# print(indice)  # Saída: 0
# 👉 Aqui, procuramos "banana" entre os índices 0 e 20.
# 👉 A segunda ocorrência está em 23, mas fora do limite da busca, então rfind() retorna 0 (posição da primeira ocorrência).

# 🚀 Resumo Rápido
# Método	O que faz?
# rfind("X")	Retorna a posição da última ocorrência de "X" na string.
# rfind("X", start)	Começa a busca na posição start e procura para trás.
# rfind("X", start, end)	Busca entre as posições start e end.
# rfind("X") == -1	Indica que "X" não foi encontrado.

l = "ELIANDRO AP ELIAS "
print("AP" in l)

# 📌 in (Operador de Pertinência)
# O operador in verifica se uma substring está presente dentro de uma string. Ele retorna True se encontrar a substring e False caso contrário.

# 🛠️ Sintaxe:

# substring in string
# substring: O trecho que estamos procurando.
# string: A string onde faremos a busca.
# 🏷️ Exemplos Práticos
# ✅ Exemplo 1: Verificando se um texto está presente

# texto = "Python é incrível"
# resultado = "Python" in texto
# print(resultado)  # Saída: True
# 👉 "Python" está dentro da string, então a saída é True.

# ✅ Exemplo 2: Quando a substring não está presente

# texto = "Python é incrível"
# resultado = "Java" in texto
# print(resultado)  # Saída: False
# 👉 "Java" não está na string, então a saída é False.

# ✅ Exemplo 3: Usando in com if

# texto = "Aprender Python é divertido!"
# if "Python" in texto:
#     print("A palavra 'Python' está na frase!")
# 📝 Como "Python" está na string, o código imprime:

# nginx
# Copiar
# Editar
# A palavra 'Python' está na frase!
# ✅ Exemplo 4: Usando not in para verificar ausência


# texto = "Eu gosto de programação"
# if "C++" not in texto:
#     print("A palavra 'C++' NÃO está na frase!")
# 📝 Como "C++" não está na string, o código imprime:

# mathematica
# Copiar

# A palavra 'C++' NÃO está na frase!
# 🚀 Resumo Rápido
# Operador	O que faz?
# "X" in string	Retorna True se "X" existir dentro da string.
# "X" not in string	Retorna True se "X" não existir na string.
# if "X" in string:	Pode ser usado para executar ações se "X" estiver presente.

m = "Eliandro Silva Elias" 
print(m.count('n'))


# 📌 count()
# A função count() conta quantas vezes uma substring aparece dentro de uma string.

# 🛠️ Sintaxe:

# string.count(substring, start, end)
# substring (obrigatório): O trecho que queremos contar.
# start (opcional): A posição inicial para começar a contagem.
# end (opcional): A posição final para a contagem.
# 🏷️ Exemplos Práticos
# ✅ Exemplo 1: Contando palavras em uma string

# texto = "banana, maçã, banana, laranja, banana"
# quantidade = texto.count("banana")
# print(quantidade)  # Saída: 3
# 👉 "banana" aparece 3 vezes na string.

# ✅ Exemplo 2: Quando a palavra não existe

# texto = "Python é incrível"
# quantidade = texto.count("Java")
# print(quantidade)  # Saída: 0
# 👉 Como "Java" não está na string, a saída é 0.

# ✅ Exemplo 3: Contando dentro de um intervalo (start e end)

# texto = "banana, maçã, banana, laranja, banana"
# quantidade = texto.count("banana", 10, 30)
# print(quantidade)  # Saída: 1
# 👉 Aqui, contamos "banana" apenas entre os índices 10 e 30, então encontramos 1 ocorrência.

# 🚀 Resumo Rápido
# Método	O que faz?
# count("X")	Conta quantas vezes "X" aparece na string.
# count("X", start)	Começa a contar a partir da posição start.
# count("X", start, end)	Conta dentro do intervalo start a end.

s = "Olá Mundo!"

print(s[0])
print(s[2])
print(s[6])

# 📌 Explicação do Código
# O código acessa caracteres específicos da string s = "Olá Mundo!" usando indexação ([]).
# A contagem dos índices começa do 0 (zero), ou seja, o primeiro caractere está na posição 0, o segundo na posição 1 e assim por diante.

# 🛠️ Código e Saída

# s = "Olá Mundo!"

# print(s[0])  # Saída: O
# print(s[2])  # Saída: á
# print(s[6])  # Saída: u
# 📌 Analisando Cada Linha
# 🔹 s[0]:

# Acessa o primeiro caractere da string, que é "O".
# s = "Olá Mundo!"

#  0  1  2  3  4  5  6  7  8  9 10  
#  O  l  á     M  u  n  d  o  !  
# 🔹 s[2]:

# Acessa o terceiro caractere, que é "á".
# 🔹 s[6]:

# Acessa o sétimo caractere, que é "u".
# 🚀 Resumo
# Índice	Caractere
# s[0]	"O"
# s[2]	"á"
# s[6]	"u"
# Se tentar acessar um índice fora do limite da string, o Python gerará um erro 
# IndexError: string index out of range.

s = "Olá Mundo!"

print(s[1:3])

# 📌 Explicação do Código
# O código usa fatiamento de strings ([start:end]) para extrair uma parte da string s = "Olá Mundo!".

# 🛠️ Código e Saída

# s = "Olá Mundo!"

# print(s[1:3])  # Saída: lá
# 📌 Entendendo o Fatiamento [start:end]
# A sintaxe do fatiamento é:


# string[início:fim]
# início: Posição inicial (inclusiva).
# fim: Posição final (exclusiva, ou seja, não inclui esse índice).
# 🔹 No exemplo:


# s[1:3]
# 1 → Começa no índice 1 (letra "l").
# 3 → Vai até antes do índice 3 (ou seja, para no "á").
# 📌 A string original com os índices:


#   0   1   2   3   4   5   6   7   8   9  10  
#   O   l   á       M   u   n   d   o   !  
# 🔹 O trecho extraído é "lá".

# 🚀 Resumo
# Código	Saída	Explicação
# s[1:3]	"lá"	Pega do índice 1 ao 2 (o 3 não entra).


s = "Olá Mundo!"

print(s[:3])