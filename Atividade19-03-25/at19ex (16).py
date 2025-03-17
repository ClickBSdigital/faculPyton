# Tal cadastro solicitará os seguintes dados:
# (nome, cpf, rg, data de nascimento, sexo, peso,
# tipo sanguíneo, renda, endereço, telefone, cidade
# e estado)

   
nome = input("Digite o nome do paciente: ")
cpf = input("Digite o CPF do paciente: ")
rg = input("Digite o RG do paciente: ")
data_nascimento = input("Digite a data de nascimento do paciente (dd/mm/aaaa): ")
sexo = input("Digite o sexo do paciente (M/F): ")
peso = float(input("Digite o peso do paciente (kg): "))
tipo_sanguineo = input("Digite o tipo sanguíneo do paciente: ")
renda = float(input("Digite a renda mensal do paciente (R$): "))
endereco = input("Digite o endereço do paciente: ")
telefone = input("Digite o telefone do paciente: ")
cidade = input("Digite a cidade do paciente: ")
estado = input("Digite o estado do paciente: ")


print("\nCadastro Completo!")
print(f"Nome: {nome}")
print(f"CPF: {cpf}")
print(f"RG: {rg}")
print(f"Data de Nascimento: {data_nascimento}")
print(f"Sexo: {sexo}")
print(f"Peso: {peso} kg")
print(f"Tipo Sanguíneo: {tipo_sanguineo}")
print(f"Renda: R$ {renda:.2f}")
print(f"Endereço: {endereco}")
print(f"Telefone: {telefone}")
print(f"Cidade: {cidade}")
print(f"Estado: {estado}")

