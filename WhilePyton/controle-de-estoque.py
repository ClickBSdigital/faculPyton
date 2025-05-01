# Dicionário inicial com os produtos e seus códigos
produtos = {
    10: {'nome': 'Caderno', 'estoque': 0},
    20: {'nome': 'Caneta', 'estoque': 0},
    30: {'nome': 'Lapis', 'estoque': 0},
    40: {'nome': 'Borracha', 'estoque': 0},
    50: {'nome': 'Régua', 'estoque': 0}
}

# Função para inicializar o estoque
def inicializar_estoque():
    print("\nINICIALIZAÇÃO DO ESTOQUE")
    for codigo in sorted(produtos.keys()):
        while True:
            try:
                qtd = int(input(f"Digite a quantidade inicial de {produtos[codigo]['nome']} (código {codigo}): "))
                if qtd >= 0:
                    produtos[codigo]['estoque'] = qtd
                    break
                else:
                    print("Quantidade não pode ser negativa!")
            except ValueError:
                print("Digite um número válido!")

# Função para exibir o menu
def exibir_menu():
    print("\nMENU DE OPÇÕES")
    print("E - Entrada no estoque")
    print("S - Saída no estoque")
    print("R - Relatório")
    print("C - Cadastrar novo produto")
    print("X - Sair")

# Função para cadastrar novo produto
def cadastrar_produto():
    print("\nCADASTRO DE NOVO PRODUTO")
    while True:
        try:
            codigo = int(input("Digite o código do novo produto (número inteiro): "))
            if codigo in produtos:
                print("Código já existe! Escolha outro.")
                continue
            
            nome = input("Digite o nome do produto: ").strip()
            if not nome:
                print("Nome não pode ser vazio!")
                continue
            
            # Inicializa estoque do novo produto
            while True:
                try:
                    qtd = int(input(f"Digite a quantidade inicial de {nome}: "))
                    if qtd >= 0:
                        produtos[codigo] = {'nome': nome, 'estoque': qtd}
                        print(f"Produto {nome} (código {codigo}) cadastrado com sucesso!")
                        return
                    else:
                        print("Quantidade não pode ser negativa!")
                except ValueError:
                    print("Digite um número válido!")
                    
        except ValueError:
            print("Código deve ser um número inteiro!")

# Função para processar entrada no estoque
def entrada_estoque():
    if not produtos:
        print("Nenhum produto cadastrado!")
        return
    
    print("\nPRODUTOS DISPONÍVEIS:")
    for codigo in sorted(produtos.keys()):
        print(f"{codigo} - {produtos[codigo]['nome']}")
    
    while True:
        try:
            codigo = int(input("\nDigite o código do produto: "))
            if codigo in produtos:
                qtd = int(input("Digite a quantidade a adicionar: "))
                if qtd > 0:
                    produtos[codigo]['estoque'] += qtd
                    print(f"{qtd} {produtos[codigo]['nome']}(s) adicionado(s) ao estoque.")
                    print(f"Novo estoque: {produtos[codigo]['estoque']}")
                    break
                else:
                    print("Quantidade deve ser maior que zero!")
            else:
                print("Código de produto inválido!")
        except ValueError:
            print("Digite um número válido!")

# Função para processar saída no estoque
def saida_estoque():
    if not produtos:
        print("Nenhum produto cadastrado!")
        return
    
    print("\nPRODUTOS DISPONÍVEIS:")
    for codigo in sorted(produtos.keys()):
        print(f"{codigo} - {produtos[codigo]['nome']} (Estoque: {produtos[codigo]['estoque']})")
    
    while True:
        try:
            codigo = int(input("\nDigite o código do produto: "))
            if codigo in produtos:
                qtd = int(input("Digite a quantidade a retirar: "))
                if qtd > 0:
                    if produtos[codigo]['estoque'] >= qtd:
                        produtos[codigo]['estoque'] -= qtd
                        print(f"{qtd} {produtos[codigo]['nome']}(s) retirado(s) do estoque.")
                        print(f"Novo estoque: {produtos[codigo]['estoque']}")
                        break
                    else:
                        print(f"Estoque insuficiente! Há apenas {produtos[codigo]['estoque']} unidades disponíveis.")
                else:
                    print("Quantidade deve ser maior que zero!")
            else:
                print("Código de produto inválido!")
        except ValueError:
            print("Digite um número válido!")

# Função para gerar relatório
def gerar_relatorio():
    if not produtos:
        print("Nenhum produto cadastrado!")
        return
    
    print("\nRELATÓRIO DE ESTOQUE")
    print("-" * 40)
    print("{:<10} {:<20} {:<10}".format("CÓDIGO", "PRODUTO", "QUANTIDADE"))
    print("-" * 40)
    for codigo in sorted(produtos.keys()):
        print("{:<10} {:<20} {:<10}".format(
            codigo, 
            produtos[codigo]['nome'], 
            produtos[codigo]['estoque']
        ))
    print("-" * 40)
    total = sum(produto['estoque'] for produto in produtos.values())
    print(f"TOTAL DE ITENS NO ESTOQUE: {total}")

# Programa principal
def main():
    print("CONTROLE DE ESTOQUE - ALMOXARIFADO")
    inicializar_estoque()
    
    while True:
        exibir_menu()
        opcao = input("\nEscolha a operação (E/S/R/C/X): ").upper()
        
        if opcao == 'E':
            entrada_estoque()
        elif opcao == 'S':
            saida_estoque()
        elif opcao == 'R':
            gerar_relatorio()
        elif opcao == 'C':
            cadastrar_produto()
        elif opcao == 'X':
            print("\nRelatório final:")
            gerar_relatorio()
            print("\nEncerrando o programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()