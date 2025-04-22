# 90 - Verifique se o número é palíndromo
n = input("Digite um número: ")

if n == n[::-1]:
    print("O número é palíndromo.")
else:
    print("O número não é palíndromo.")


# 90 - Verifique se um número é divisível por 3 e 5
numero = int(input("Digite um número: "))
if numero % 3 == 0 and numero % 5 == 0:
    print("O número é divisível por 3 e 5.")
else:
    print("O número NÃO é divisível por 3 e 5.")
    
    
    # =====================================
    
#     Vamos analisar com calma o exercício #90 - Verifique se um número é divisível por 3 e 5:

# ✅ Objetivo:
# Verificar se um número é divisível tanto por 3 quanto por 5 ao mesmo tempo.

# 🔢 Exemplo de números divisíveis por 3 e 5:
# 15 → 15 ÷ 3 = 5 ✔️ e 15 ÷ 5 = 3 ✔️

# 30 → 30 ÷ 3 = 10 ✔️ e 30 ÷ 5 = 6 ✔️

# 45, 60, 75 também são exemplos válidos.

# 🧠 Explicação do código:

# numero = int(input("Digite um número: "))
# Aqui, o usuário digita um número que será convertido para inteiro e armazenado na variável numero.


# if numero % 3 == 0 and numero % 5 == 0:
# numero % 3 == 0: verifica se o número é divisível por 3.

# O operador % (módulo) retorna o resto da divisão.

# Se o resto for zero, o número é divisível.

# numero % 5 == 0: mesma lógica, mas para o número 5.

# and: significa que as duas condições precisam ser verdadeiras ao mesmo tempo.


#     print("O número é divisível por 3 e 5.")
# Se ambas as condições forem verdadeiras, imprime essa mensagem.


# else:
#     print("O número NÃO é divisível por 3 e 5.")
# Se uma ou as duas condições forem falsas, essa mensagem será exibida.

# ⚠️ Atenção:
# O número só será aceito se for divisível pelos dois números ao mesmo tempo!

# Exemplo:

# 9 → divisível por 3 ❌ mas não por 5

# 10 → divisível por 5 ❌ mas não por 3

# 30 → divisível por 3 ✔️ e por 5 ✔️ ✅

# # Se quiser, posso adaptar esse código para verificar somente um ou qualquer um dos dois (com or no lugar de and), ou até mostrar mensagens separadas para cada divisor. 

# # ==================================
# Abaixo estão três versões diferentes do exercício, conforme o que você pode querer:

# ✅ Versão 1: Verificar se é divisível por 3 OU por 5 (qualquer um dos dois)

# numero = int(input("Digite um número: "))

# if numero % 3 == 0 or numero % 5 == 0:
#     print("O número é divisível por 3 ou por 5.")
# else:
#     print("O número NÃO é divisível por 3 nem por 5.")
# ✅ Versão 2: Mostrar mensagens separadas para cada caso

# numero = int(input("Digite um número: "))

# if numero % 3 == 0:
#     print("O número é divisível por 3.")
# else:
#     print("O número NÃO é divisível por 3.")

# if numero % 5 == 0:
#     print("O número é divisível por 5.")
# else:
#     print("O número NÃO é divisível por 5.")
# ✅ Versão 3: Mostrar todas as possibilidades com clareza

# numero = int(input("Digite um número: "))

# if numero % 3 == 0 and numero % 5 == 0:
#     print("O número é divisível por 3 e por 5.")
# elif numero % 3 == 0:
#     print("O número é divisível apenas por 3.")
# elif numero % 5 == 0:
#     print("O número é divisível apenas por 5.")
# else:
#     print("O número NÃO é divisível por 3 nem por 5.")