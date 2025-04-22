# 97 - Verifique se um número possui ao menos dois dígitos iguais consecutivos
n = input("Digite um número: ")

tem_repetido = any(n[i] == n[i+1] for i in range(len(n) - 1))

if tem_repetido:
    print("O número possui dígitos iguais consecutivos.")
else:
    print("Não há dígitos iguais consecutivos.")
# =======================

# 🧩 Objetivo:
# Verificar se um número digitado possui ao menos dois dígitos iguais e consecutivos.

# Exemplos:
# 1223 → ✅ (os dígitos 2 e 2 aparecem um após o outro)

# 1234 → ❌ (todos os dígitos são diferentes)

# 7788 → ✅ (tem dois pares consecutivos: 7 e 8 repetidos)

# 9090 → ❌ (apesar de 9 aparecer duas vezes, não é consecutivo)

# 🔍 Explicação do código:

# n = input("Digite um número: ")
# Aqui, a entrada é recebida como texto (string).

# Isso facilita o acesso a cada dígito individualmente com n[i].


# tem_repetido = any(n[i] == n[i+1] for i in range(len(n) - 1))
# Essa linha é a mais poderosa e pode parecer confusa. Vamos destrinchar:

# for i in range(len(n) - 1):

# Percorre cada posição da string até a penúltima posição, para poder comparar com o próximo caractere.

# n[i] == n[i+1]:

# Compara o dígito atual com o próximo dígito.

# any(...):

# Retorna True se qualquer uma das comparações for verdadeira (ou seja, encontrou dois dígitos iguais consecutivos).

# ✅ Se pelo menos uma vez n[i] == n[i+1], então tem_repetido será True.


# if tem_repetido:
#     print("O número possui dígitos iguais consecutivos.")
# else:
#     print("Não há dígitos iguais consecutivos.")
# Aqui, o resultado da verificação é exibido de acordo com o valor da variável tem_repetido.

# ✅ Exemplo com n = "5668":
# 5 == 6 → ❌

# 6 == 6 → ✅ (encontrado!)

# tem_repetido vira True