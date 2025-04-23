

import math

def combinacao(n, r):
    return math.comb(n, r)

def arranjo(n, r):
    return math.perm(n, r)

def permutacao_simples(n):
    return math.factorial(n)

def permutacao_com_repeticao(total, repeticoes):
    denominador = 1
    for r in repeticoes:
        denominador *= math.factorial(r)
    return math.factorial(total) // denominador

def exemplo_mulheres_homens():
    total = 0
    # Caso 1: 2 mulheres e 4 homens
    total += combinacao(4, 2) * combinacao(7, 4)
    # Caso 2: 3 mulheres e 3 homens
    total += combinacao(4, 3) * combinacao(7, 3)
    # Caso 3: 4 mulheres e 2 homens
    total += combinacao(4, 4) * combinacao(7, 2)
    return total

# Menu simples
while True:
    print("\nEscolha uma opção:")
    print("1 - Combinação")
    print("2 - Arranjo")
    print("3 - Permutação simples")
    print("4 - Permutação com repetição")
    print("5 - Exemplo: Grupo com pelo menos 2 mulheres")
    print("0 - Sair")
    opcao = input("Opção: ")

    if opcao == '0':
        break
    elif opcao == '1':
        n = int(input("Digite o total (n): "))
        r = int(input("Digite quantos escolher (r): "))
        print(f"Combinação C({n}, {r}) = {combinacao(n, r)}")
    elif opcao == '2':
        n = int(input("Digite o total (n): "))
        r = int(input("Digite quantos escolher (r): "))
        print(f"Arranjo A({n}, {r}) = {arranjo(n, r)}")
    elif opcao == '3':
        n = int(input("Digite o número de elementos (n): "))
        print(f"Permutação P({n}) = {permutacao_simples(n)}")
    elif opcao == '4':
        total = int(input("Digite o total de letras (ou elementos): "))
        rep = input("Digite as repetições separadas por vírgula (ex: 2,3,1): ")
        repeticoes = list(map(int, rep.split(",")))
        print(f"Permutação com repetição = {permutacao_com_repeticao(total, repeticoes)}")
    elif opcao == '5':
        print(f"Total de grupos possíveis com pelo menos 2 mulheres: {exemplo_mulheres_homens()}")
    else:
        print("Opção inválida!")


# ✅ O que esse script faz:
# Calcula combinação, arranjo e permutações (simples e com repetição);

# Resolve a questão da EFOMM (grupo de 6 pessoas com pelo menos 2 mulheres);

# Pede os valores para você digitar — ideal para estudar!