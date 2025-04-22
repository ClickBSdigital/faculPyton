# 99: Verifique se um número é perfeito (a soma dos divisores é igual ao número)
numero = int(input("Digite um número: "))
soma_divisores = sum(i for i in range(1, numero) if numero % i == 0)

if soma_divisores == numero:
    print("O número é perfeito.")
else:
    print("O número não é perfeito.")


# ==================================

# 🔍 Explicação passo a passo:
# Entrada: O número é recebido com input() e convertido para inteiro com int().

# soma_divisores = sum(i for i in range(1, numero) if numero % i == 0): Essa linha calcula a soma dos divisores do número.

# A expressão range(1, numero) gera todos os números de 1 até o número anterior.

# numero % i == 0 verifica se o número é divisível por i (se o resto da divisão for 0).

# sum(...) soma todos os divisores encontrados.

# A condição soma_divisores == numero verifica se a soma dos divisores é igual ao número.

# Se for verdade, o número é perfeito.

# Caso contrário, o número não é perfeito.

# 🧠 Exemplo:

# Entrada: 6 → divisores: 1, 2, 3 → soma: 1 + 2 + 3 = 6 → perfeito → ✅

# Entrada: 10 → divisores: 1, 2, 5 → soma: 1 + 2 + 5 = 8 → não perfeito → ❌