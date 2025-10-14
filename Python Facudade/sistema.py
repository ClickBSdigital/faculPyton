from Produto import Produto


# p1 = Produto("Monitor", "LG", "27 PLO", 1900)
# print(f"O nome do produto é: {p1.get_nome()}")

##################################
lista_prods = []

i = 0
while i < 2:
    nome = input("Digite o nome do Produto: ")
    marca = input("Digite a marca do Produto: ")
    modelo = input("Digite o modelo do Produto: ")      
    preco = input("Digite o preço do Produto: ")
    prod = Produto(nome, marca, modelo, preco)
    lista_prods.append(prod)
    i += 1
    
for item in lista_prods:
    print(f"Nome: {item.get_nome()} - Marca: {item.marca} - Modelo: {item.modelo} - Preço: {item.preco}")
