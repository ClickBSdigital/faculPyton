# Ex 01. Strings
# Escrever um programa na linguagem Python que conte o
# número de palavras em um texto.
# Como entrada, um texto será digitado de forma interativa no
# teclado.
# Como saída será impresso o texto, bem como a quantidade
# de caracteres desse texto.

texto = input("Digite um texto: ")

num_palavras = len(texto.split())
num_caracteres = len(texto)

print(f"\nTexto digitado: {texto}")
print(f"\nNúmero de palavras: {num_palavras}")
print(f"Número de caracteres: {num_caracteres}")