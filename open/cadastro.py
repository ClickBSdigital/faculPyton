cadastros = []

while True:
    print("\n===== MENU PRINCIPAL =====")
    print("1 - Cadastrar Pessoa")
    print("2 - Consultar Cadastro")
    print("3 - Sair")
    opcao = input("Escolha uma opção (1/2/3): ").strip()

    if opcao == "1":
        while True:
            try:
                nome = input("Nome: ").strip().title()
                idade = int(input("Idade: ").strip())
                sexo = input("Sexo (M/F): ").strip().upper()
                if sexo not in ["M", "F"]:
                    raise ValueError("Sexo inválido. Use M ou F.")
                cpf = input("CPF (somente números): ").strip()
                if not cpf.isdigit() or len(cpf) != 11:
                    raise ValueError("CPF inválido. Deve conter 11 números.")
                endereco = input("Endereço: ").strip()
                cidade = input("Cidade: ").strip().title()
                estado = input("Estado (sigla): ").strip().upper()

                pessoa = f"Nome: {nome}, Idade: {idade}, Sexo:{sexo}, CPF: {cpf}, Endereço: {endereco}, Cidade: {cidade}, Estado: {estado}"
                cadastros.append(pessoa)

                continuar = input("Deseja cadastrar outra pessoa? (s/n): ").strip().lower()
                if continuar != "s":
                    break

            except ValueError as erro:
                print(f"Erro: {erro}. Tente novamente.")

        with open("open/cadastro.txt", "a", encoding="utf-8") as arquivo:
            for pessoa in cadastros:
                arquivo.write(pessoa + "\n" + "-"*100 + "\n")
        cadastros.clear()

    elif opcao == "2":
        try:
            with open("open/cadastro.txt", "r", encoding="utf-8") as arquivo:
                linhas = arquivo.readlines()
                if not linhas:
                    print("⚠ Arquivo vazio. Nenhum cadastro ainda.")
                else:
                    print(f"Total de registros: {len(linhas)//2}")
                    num = int(input("Digite o número da pessoa que deseja consultar (1, 2, 3...): ").strip())
                    index = (num - 1) * 2
                    if index < len(linhas):
                        print("\n🧾 Registro encontrado:")
                        print(linhas[index])
                    else:
                        print("❌ Número inválido.")
        except FileNotFoundError:
            print("⚠ Arquivo não encontrado. Nenhum dado cadastrado ainda.")

    elif opcao == "3":
        print("Encerrando o programa. 👋")
        break

    else:
        print("❌ Opção inválida. Escolha 1, 2 ou 3.")




# ================================================================
# Elaindro Silva.
# Diego Santos.
# ================================================================
# Crie um programa em Python que cadastre usuários com nome e idade, sexo, CPF, Endereço, Cidade e Estado, armazenando esses dados em listas e, ao final, salve todas as informações em um arquivo cadastro.txt.
# O Aplicativo deverá ter um módulo de consulta de todos os dados.
# Regras:

# Cadastro:
# O usuário pode cadastrar quantas pessoas quiser.
# O programa deve perguntar ao final de cada cadastro se deseja cadastrar outra pessoa.
# Use try e except para garantir valores válidos.
# Após encerrar os cadastros, grave os dados no arquivo cadastro.txt, no formato:

# Consultas:
# O usuário deverá consultar somente uma linha e retornar apenas o que foi solicitado.

# Sair
# Ao definir sair, o programa será encerrado e os dados preservados.


# Ex.
# Nome: Maria, Idade: 22, Sexo:F, Endereço: Rua Afonso Penas, 4995, Cidade: Campo Grande, Estado: MS
# -------------------------------------------------------------------------------------------------- 
# Nome: João, Idade: 30, Sexo:M, Endereço: Rua Afonso Penas, 4996, Cidade: Campo Grande, Estado: MS ...