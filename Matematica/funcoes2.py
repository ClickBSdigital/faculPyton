def fatorial(n):
    """Função para calcular o fatorial de um número."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

def permutacao_sem_repeticao(n):
    """Função para calcular a permutação sem repetição: P(n) = n!"""
    return fatorial(n)

def arranjo(n, r):
    """Função para calcular o arranjo (ou permutação sem repetição de r elementos de n): P(n, r) = n! / (n - r)!"""
    return fatorial(n) // fatorial(n - r)

def permutacao_com_repeticao(n, repeticoes):
    """Função para calcular a permutação com repetição: P_rep(n; a1, a2, ..., an) = n! / (a1! * a2! * ... * an!)"""
    denominador = 1
    for r in repeticoes:
        denominador *= fatorial(r)
    return fatorial(n) // denominador

def combinacao(n, r):
    """Função para calcular a combinação: C(n, r) = n! / (r! * (n - r)!)"""
    return fatorial(n) // (fatorial(r) * fatorial(n - r))

# Função principal para interagir com o usuário
def obter_entrada():
    print("Escolha uma das opções abaixo:")
    print("1. Combinação (C(n, r))")
    print("2. Arranjo (P(n, r))")
    print("3. Permutação sem repetição (P(n))")
    print("4. Permutação com repetição (P_rep(n; a1, a2, ..., an))")
    
    escolha = int(input("Digite o número da opção escolhida: "))
    
    if escolha == 1:
        n = int(input("Digite o número total de elementos (n): "))
        r = int(input("Digite o número de elementos a serem escolhidos (r): "))
        print(f"O número de combinações de {r} elementos de um conjunto de {n} é: {combinacao(n, r)}")
        
    elif escolha == 2:
        n = int(input("Digite o número total de elementos (n): "))
        r = int(input("Digite o número de elementos a serem arranjados (r): "))
        print(f"O número de arranjos (permutação sem repetição) de {r} elementos de um conjunto de {n} é: {arranjo(n, r)}")
        
    elif escolha == 3:
        n = int(input("Digite o número total de elementos (n): "))
        print(f"O número de permutações sem repetição de {n} elementos é: {permutacao_sem_repeticao(n)}")
        
    elif escolha == 4:
        n = int(input("Digite o número total de elementos (n): "))
        repeticoes = list(map(int, input("Digite as repetições de elementos (separados por espaço): ").split()))
        print(f"O número de permutações com repetição é: {permutacao_com_repeticao(n, repeticoes)}")
        
    else:
        print("Opção inválida. Tente novamente.")

# Chamar a função principal
obter_entrada()



# =======================================:


# Explicação das Funções:
# Fatorial: A função fatorial(n) calcula o fatorial de um número 
# 𝑛
# n, que é 
# 𝑛
# !
# n!. O fatorial de um número é o produto de todos os números inteiros de 1 até 
# 𝑛
# n.

# Permutação sem repetição (P(n)): A função permutacao_sem_repeticao(n) calcula o número de maneiras de organizar 
# 𝑛
# n elementos distintos, sem repetição.

# Arranjo (P(n, r)): A função arranjo(n, r) calcula o número de arranjos (ou permutações sem repetição de 
# 𝑟
# r elementos de 
# 𝑛
# n). É dado por 
# 𝑃
# (
# 𝑛
# ,
# 𝑟
# )
# =
# 𝑛
# !
# (
# 𝑛
# −
# 𝑟
# )
# !
# P(n,r)= 
# (n−r)!
# n!
# ​
#  .

# Permutação com repetição (P_rep(n; a1, a2, ..., an)): A função permutacao_com_repeticao(n, repeticoes) calcula a permutação com repetição. O número de permutações é dado por 
# 𝑃
# rep
# (
# 𝑛
# ;
# 𝑎
# 1
# ,
# 𝑎
# 2
# ,
# .
# .
# .
# ,
# 𝑎
# 𝑛
# )
# =
# 𝑛
# !
# 𝑎
# 1
# !
# ⋅
# 𝑎
# 2
# !
# ⋅
# .
# .
# .
# P 
# rep
# ​
#  (n;a1,a2,...,an)= 
# a1!⋅a2!⋅...
# n!
# ​
#  , onde 
# 𝑎
# 1
# ,
# 𝑎
# 2
# ,
# …
# a1,a2,… são as repetições de elementos.

# Combinação (C(n, r)): A função combinacao(n, r) calcula o número de combinações, que é o número de maneiras de escolher 
# 𝑟
# r elementos de um conjunto de 
# 𝑛
# n elementos sem levar em consideração a ordem. A fórmula é 
# 𝐶
# (
# 𝑛
# ,
# 𝑟
# )
# =
# 𝑛
# !
# 𝑟
# !
# ⋅
# (
# 𝑛
# −
# 𝑟
# )
# !
# C(n,r)= 
# r!⋅(n−r)!
# n!
# ​
#  .

# Como Funciona:
# O programa mostra um menu com as opções de cálculo: Combinação, Arranjo, Permutação sem repetição e Permutação com repetição.

# O usuário escolhe uma das opções e o programa pede os valores necessários:

# Para Combinação: o número total de elementos 
# 𝑛
# n e o número de elementos a escolher 
# 𝑟
# r.

# Para Arranjo: o número total de elementos 
# 𝑛
# n e o número de elementos a serem arranjados 
# 𝑟
# r.

# Para Permutação sem repetição: o número total de elementos 
# 𝑛
# n.

# Para Permutação com repetição: o número total de elementos 
# 𝑛
# n e as repetições de elementos (se houver).

# O programa calcula e exibe o resultado na tela.

# Exemplo de Execução:
# Imagine que você escolhe a opção 2 (Arranjo) e insere os valores:


# Escolha uma das opções abaixo:
# 1. Combinação (C(n, r))
# 2. Arranjo (P(n, r))
# 3. Permutação sem repetição (P(n))
# 4. Permutação com repetição (P_rep(n; a1, a2, ..., an))
# Digite o número da opção escolhida: 2
# Digite o número total de elementos (n): 5
# Digite o número de elementos a serem arranjados (r): 3
# O número de arranjos (permutação sem repetição) de 3 elementos de um conjunto de 5 é: 60
# Você pode testar e usar esse código sempre que precisar de cálculos de combinação, arranjo, permutação, entre outros.