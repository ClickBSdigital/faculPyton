# faça um programa que pergunte o preço de três
# produtos e informe qual o produto vo deve complrar. 
# sabendo que a decisao é compra o mais barato

# Programa para escolher o produto mais barato

# Entrada de dados
preco1 = float(input("Digite o preço do primeiro produto: R$ "))
preco2 = float(input("Digite o preço do segundo produto: R$ "))
preco3 = float(input("Digite o preço do terceiro produto: R$ "))

# Verificando o menor preço
if preco1 < preco2 and preco1 < preco3:
    print("Você deve comprar o primeiro produto.")
elif preco2 < preco1 and preco2 < preco3:
    print("Você deve comprar o segundo produto.")
elif preco3 < preco1 and preco3 < preco2:
    print("Você deve comprar o terceiro produto.")
else:
    print("Há produtos com o mesmo preço. Escolha qualquer um deles!")
