ARQUIVO = "2UC\construcao_facil\clientes.txt"

def salvar_cliente(cliente):
    with open(ARQUIVO, "a") as f:
        f.write(f"{cliente['id']};{cliente['nome']};{cliente['telefone']}\n")

def listar_clientes():
    try:
        with open(ARQUIVO, "r") as f:
            for linha in f:
                id, nome, telefone = linha.strip().split(";")
                print(f"[{id}] {nome} - {telefone}")
    except FileNotFoundError:
        print("Nenhum cliente cadastrado ainda.")

def buscar_cliente_por_id(id_busca):
    with open(ARQUIVO, "r") as f:
        linhas = f.readlines()
    for linha in linhas:
        id, nome, telefone = linha.strip().split(";")
        if id == id_busca:
            return {"id": id, "nome": nome, "telefone": telefone}
    return None

def editar_cliente():
    id_busca = input("ID do cliente a editar: ")
    cliente = buscar_cliente_por_id(id_busca)
    if not cliente:
        print("Cliente não encontrado.")
        return

    novo_nome = input(f"Novo nome ({cliente['nome']}): ") or cliente['nome']
    novo_telefone = input(f"Novo telefone ({cliente['telefone']}): ") or cliente['telefone']

    with open(ARQUIVO, "r") as f:
        linhas = f.readlines()
    with open(ARQUIVO, "w") as f:
        for linha in linhas:
            id, _, _ = linha.strip().split(";")
            if id == id_busca:
                f.write(f"{id};{novo_nome};{novo_telefone}\n")
            else:
                f.write(linha)
    print("Cliente atualizado.")

def deletar_cliente():
    id_busca = input("ID do cliente a excluir: ")
    with open(ARQUIVO, "r") as f:
        linhas = f.readlines()
    with open(ARQUIVO, "w") as f:
        for linha in linhas:
            if not linha.startswith(id_busca + ";"):
                f.write(linha)
    print("Cliente excluído.")

def menu_clientes():
    while True:
        print("\n--- Menu Clientes ---")
        print("1. Cadastrar cliente")
        print("2. Listar clientes")
        print("3. Editar cliente")
        print("4. Deletar cliente")
        print("0. Voltar ao menu principal")
        opcao = input("Opção: ")

        if opcao == "1":
            id = input("ID do cliente: ")
            nome = input("Nome do cliente: ")
            telefone = input("Telefone: ")
            salvar_cliente({"id": id, "nome": nome, "telefone": telefone})
            print("Cliente cadastrado.")
        elif opcao == "2":
            listar_clientes()
        elif opcao == "3":
            editar_cliente()
        elif opcao == "4":
            deletar_cliente()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")
