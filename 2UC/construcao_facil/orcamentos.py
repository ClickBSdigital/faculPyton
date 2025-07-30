from produtos import buscar_produto_por_id, listar_produtos
from clientes import buscar_cliente_por_id, listar_clientes

ARQUIVO = "2UC\construcao_facil\orcamentos.txt"

def menu_orcamentos():
    print("\n--- Novo Orçamento ---")
    listar_clientes()
    cliente_id = input("ID do cliente: ")
    cliente = buscar_cliente_por_id(cliente_id)
    if not cliente:
        print("Cliente não encontrado.")
        return

    produtos = []
    total = 0.0

    while True:
        listar_produtos()
        produto_id = input("ID do produto (ou 0 para finalizar): ")
        if produto_id == "0":
            break
        produto = buscar_produto_por_id(produto_id)
        if produto:
            produtos.append(produto)
            total += float(produto['preco'])
        else:
            print("Produto não encontrado.")

    if not produtos:
        print("Nenhum produto adicionado.")
        return

    with open(ARQUIVO, "a") as f:
        linha = f"{cliente['id']};{cliente['nome']};"
        linha += ",".join([p['nome'] for p in produtos])
        linha += f";Total: R${total:.2f}\n"
        f.write(linha)

    print(f"Orçamento salvo com sucesso! Total: R${total:.2f}")
