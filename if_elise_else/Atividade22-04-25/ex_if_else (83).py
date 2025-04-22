# 83 - Verifique se um número é quadrado perfeito
import math

n = int(input("Digite um número: "))
raiz = math.isqrt(n)

if raiz * raiz == n:
    print("O número é um quadrado perfeito.")
else:
    print("O número não é um quadrado perfeito.")
# ===================

# 83 - Verifique se um número é quadrado perfeito
n = int(input("Digite um número: "))

eh_quadrado_perfeito = False

i = 1
while i * i <= n:
    if i * i == n:
        eh_quadrado_perfeito = True
        break
    i += 1

if eh_quadrado_perfeito:
    print("O número é um quadrado perfeito.")
else:
    print("O número não é um quadrado perfeito.")


# ============================

# 🔢 O que é um quadrado perfeito?
# Um número é chamado de quadrado perfeito quando existe um número inteiro que, multiplicado por ele mesmo, resulta nele.

# Por exemplo:

# 4 → √4 = 2 → 2 × 2 = 4 ✅

# 9 → √9 = 3 → 3 × 3 = 9 ✅

# 10 → √10 = 3,16... ❌ (não inteiro)

# 💡 Explicação do código:
# python
# Copiar
# Editar
# n = int(input("Digite um número: "))
# Aqui pedimos para o usuário digitar um número inteiro. Esse é o número que vamos testar.

# python
# Copiar
# Editar
# eh_quadrado_perfeito = False
# Criamos uma variável de controle. Vamos usar ela para saber no final se encontramos um quadrado perfeito ou não.

# python
# Copiar
# Editar
# i = 1
# while i * i <= n:
# Começamos um laço que vai testar todos os números inteiros a partir de 1. A condição i * i <= n serve para parar o teste assim que o quadrado de i for maior que n, já que não faz sentido continuar além disso.

# python
# Copiar
# Editar
#     if i * i == n:
#         eh_quadrado_perfeito = True
#         break
# Se o quadrado de i for exatamente igual a n, então n é um quadrado perfeito. Atualizamos a variável de controle e usamos break para sair do laço.

# python
# Copiar
# Editar
#     i += 1
# Se i * i não for igual a n, continuamos testando o próximo número (i + 1).

# python
# Copiar
# Editar
# if eh_quadrado_perfeito:
#     print("O número é um quadrado perfeito.")
# else:
#     print("O número não é um quadrado perfeito.")
# No final, usamos a variável de controle para imprimir a resposta.

# ✅ Exemplo com o número 36:
# i = 1 → 1×1 = 1

# i = 2 → 2×2 = 4

# i = 3 → 3×3 = 9

# i = 4 → 4×4 = 16

# i = 5 → 5×5 = 25

# i = 6 → 6×6 = 36 → ✅ Achou!

