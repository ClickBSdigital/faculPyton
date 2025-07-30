ARQUIVO = "2UC\construcao_facil\produtos.txt"

def salvar_produto(produto):
    with open(ARQUIVO, "a") as f:
        f.write(f"{produto['id']};{produto['nome']};{produto['preco']}\n")

def listar_produtos():
    try:
        with open(ARQUIVO, "r") as f:
            for linha in f:
                id, nome, preco = linha.strip().split(";")
                print(f"[{id}] {nome} - R$ {preco}")
    except FileNotFoundError:
        print("Nenhum produto cadastrado ainda.")

def buscar_produto_por_id(id_busca):
    with open(ARQUIVO, "r") as f:
        linhas = f.readlines()
    for linha in linhas:
        id, nome, preco = linha.strip().split(";")
        if id == id_busca:
            return {"id": id, "nome": nome, "preco": preco}
    return None

def editar_produto():
    id_busca = input("ID do produto a editar: ")
    produto = buscar_produto_por_id(id_busca)
    if not produto:
        print("Produto não encontrado.")
        return

    novo_nome = input(f"Novo nome ({produto['nome']}): ") or produto['nome']
    novo_preco = input(f"Novo preço ({produto['preco']}): ") or produto['preco']

    with open(ARQUIVO, "r") as f:
        linhas = f.readlines()
    with open(ARQUIVO, "w") as f:
        for linha in linhas:
            id, _, _ = linha.strip().split(";")
            if id == id_busca:
                f.write(f"{id};{novo_nome};{novo_preco}\n")
            else:
                f.write(linha)
    print("Produto atualizado.")

def deletar_produto():
    id_busca = input("ID do produto a excluir: ")
    with open(ARQUIVO, "r") as f:
        linhas = f.readlines()
    with open(ARQUIVO, "w") as f:
        for linha in linhas:
            if not linha.startswith(id_busca + ";"):
                f.write(linha)
    print("Produto excluído.")

def menu_produtos():
    while True:
        print("\n--- Menu Produtos ---")
        print("1. Cadastrar produto")
        print("2. Listar produtos")
        print("3. Editar produto")
        print("4. Deletar produto")
        print("0. Voltar ao menu principal")
        opcao = input("Opção: ")

        if opcao == "1":
            id = input("ID do produto: ")
            nome = input("Nome do produto: ")
            preco = input("Preço: ")
            salvar_produto({"id": id, "nome": nome, "preco": preco})
            print("Produto cadastrado.")
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            editar_produto()
        elif opcao == "4":
            deletar_produto()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")
