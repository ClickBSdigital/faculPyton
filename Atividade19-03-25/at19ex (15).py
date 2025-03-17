# Input

# A empresa Umbrella Corporation está
# desenvolvendo seu sistema de cadastro de
# pacientes, e a primeira fase do projeto consiste
# um desenvolver um algoritmo que capte os dados
# de cadastro.


nome = input("Digite o nome do paciente: ")
idade = int(input("Digite a idade do paciente: "))
genero = input("Digite o gênero do paciente (M/F): ")
endereco = input("Digite o endereço do paciente: ")
telefone = input("Digite o telefone do paciente: ")
email = input("Digite o e-mail do paciente: ")


print("\nCadastro Completo!")
print(f"\nNome: {nome}")
print(f"\nIdade: {idade} anos")
print(f"\nGênero: {genero}")
print(f"\nEndereço: {endereco}")
print(f"\nTelefone: {telefone}")
print(f"\nE-mail: {email}")

