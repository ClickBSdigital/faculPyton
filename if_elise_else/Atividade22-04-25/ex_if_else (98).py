# 98: Verifique se um número é palíndromo (lê-se igual de trás para frente)
numero = input("Digite um número: ")

if numero == numero[::-1]:
    print("O número é um palíndromo.")
else:
    print("O número não é um palíndromo.")


# ==================================

# 🔍 Explicação passo a passo:
# Entrada: O número é recebido como string com input().

# numero[::-1]: Inverte a string. O fatiamento [::-1] percorre a string de trás para frente.

# A condição numero == numero[::-1] verifica se a string é igual à sua versão invertida.

# Se a condição for verdadeira, significa que o número é um palíndromo.

# Caso contrário, o número não é palíndromo.

# 🧠 Exemplo:

# Entrada: 12321 → 12321 == 12321 (palíndromo) → ✅

# Entrada: 12345 → 12345 != 54321 (não palíndromo) → ❌

# ====================================

# numero = input("Digite um número: ")

# # Definir variáveis para as extremidades
# inicio = 0
# fim = len(numero) - 1

# # Verificar se o número é palíndromo
# is_palindromo = True
# while inicio < fim:
#     if numero[inicio] != numero[fim]:
#         is_palindromo = False
#         break
#     inicio += 1
#     fim -= 1

# if is_palindromo:
#     print("O número é um palíndromo.")
# else:
#     print("O número não é um palíndromo.")
# 🔍 Explicação passo a passo:
# Entrada: O número é recebido como string com input().

# A variável inicio começa no índice 0 e a variável fim começa no último índice da string (len(numero) - 1).

# O laço while percorre as extremidades da string até o meio:

# Se os caracteres nas posições inicio e fim não forem iguais, is_palindromo é definido como False e o laço é interrompido.

# Se forem iguais, os índices são ajustados (inicio aumenta e fim diminui) para continuar a comparação na próxima iteração.

# Após a verificação completa, se is_palindromo for True, o número é palíndromo. Caso contrário, não é.

# 🧠 Exemplos:
# Entrada: 12321 → 1 == 1, 2 == 2, 3 == 3 → palíndromo → ✅

# Entrada: 12345 → 1 != 5 → não palíndromo → ❌

# Essa abordagem faz a comparação manualmente, sem depender do fatiamento, e pode ser útil para entender melhor como a comparação entre as extremidades funciona.