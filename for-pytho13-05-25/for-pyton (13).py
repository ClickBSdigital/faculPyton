# 13. Sequência de Fibonacci até N termos

n = int(input("Digite quantos termos da sequência de Fibonacci deseja: "))

a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b