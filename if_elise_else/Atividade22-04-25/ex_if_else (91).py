# 91 - Verifique se uma palavra é palíndromo
palavra = input("Digite uma palavra: ")

if palavra == palavra[::-1]:
    print("A palavra é palíndroma.")
else:
    print("A palavra não é palíndroma.")
