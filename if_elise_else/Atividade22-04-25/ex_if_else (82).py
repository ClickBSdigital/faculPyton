# 82 - Verifique se dois números são primos entre si (MDC == 1)
from math import gcd

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

if gcd(a, b) == 1:
    print("Os números são primos entre si.")
else:
    print("Os números não são primos entre si.")

# ==================

# 82 - Verifique se dois números são primos entre si (MDC == 1)

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

# Algoritmo de Euclides para encontrar o MDC
# x = a
# y = b
# while y != 0:
#     resto = x % y
#     x = y
#     y = resto

# if x == 1:
#     print("Os números são primos entre si.")
# else:
#     print("Os números não são primos entre si.")
    
#     Explicação rápida:
# O while roda até o segundo número (y) virar zero.

# O valor final de x será o MDC entre a e b.

# Se o MDC for 1, eles são primos entre si.
