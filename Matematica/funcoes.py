def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

def permutacao_sem_repeticao(n):
    return fatorial(n)

def permutacao_com_repeticao(n, repeticoes):
    denominador = 1
    for r in repeticoes:
        denominador *= fatorial(r)
    return fatorial(n) // denominador

def combinacao(n, r):
    return fatorial(n) // (fatorial(r) * fatorial(n - r))

# Função para receber a entrada do usuário
def obter_entrada():
    print("Escolha uma das opções abaixo:")
    print("1. Fatorial")
    print("2. Permutação sem repetição")
    print("3. Permutação com repetição")
    print("4. Combinação")
    
    escolha = int(input("Digite o número da opção escolhida: "))
    
    if escolha == 1:
        n = int(input("Digite o número para calcular o fatorial: "))
        print(f"O fatorial de {n} é: {fatorial(n)}")
        
    elif escolha == 2:
        n = int(input("Digite o número de elementos para a permutação sem repetição: "))
        print(f"O número de permutações sem repetição de {n} elementos é: {permutacao_sem_repeticao(n)}")
        
    elif escolha == 3:
        n = int(input("Digite o número total de elementos: "))
        repeticoes = list(map(int, input("Digite as repetições de elementos (separados por espaço): ").split()))
        print(f"O número de permutações com repetição é: {permutacao_com_repeticao(n, repeticoes)}")
        
    elif escolha == 4:
        n = int(input("Digite o número total de elementos: "))
        r = int(input("Digite o número de elementos a serem escolhidos: "))
        print(f"O número de combinações de {r} elementos de um conjunto de {n} é: {combinacao(n, r)}")
        
    else:
        print("Opção inválida. Tente novamente.")

# Chamar a função para obter a entrada
obter_entrada()


# =================================================
# Como Funciona:
# O programa pede ao usuário que escolha entre fatorial, permutação sem repetição, permutação com repetição ou combinação.

# Dependendo da escolha, ele pede os números necessários:

# Para fatorial: o número 
# 𝑛
# n.

# Para permutação sem repetição: o número 
# 𝑛
# n de elementos.

# Para permutação com repetição: o número total de elementos 
# 𝑛
# n e as repetições de cada elemento.

# Para combinação: o número total de elementos 
# 𝑛
# n e o número de elementos a escolher 
# 𝑟
# r.

# O programa calcula e exibe o resultado na tela.

# Exemplo de Execução:
# Ao rodar o código, ele pode pedir algo assim:


# Escolha uma das opções abaixo:
# 1. Fatorial
# 2. Permutação sem repetição
# 3. Permutação com repetição
# 4. Combinação
# Digite o número da opção escolhida: 4
# Digite o número total de elementos: 5
# Digite o número de elementos a serem escolhidos: 3
# O número de combinações de 3 elementos de um conjunto de 5 é: 10
# Com esse código, você pode facilmente comparar e tirar as provas dos exercícios, inserindo os valores diretamente. Basta rodar o código e seguir as instruções na tela.