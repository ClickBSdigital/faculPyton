nome = input("Digite seu nome: ")
genero = input("Dgite seu genero: ")
idade = int(input("Digite a sua idade: "))
if idade >= 17:
    print("Menor ou igual a 17")
    if genero == "M":
        print("Obrigatório o alistamento militar")
    else:
        print("Não é obrigatório se alistar")
else:
    print("calma jovem, gafanhoto!!!")