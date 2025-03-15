# 03- Faça um programa que leia um valor em reais e
# calcule o valor equivalente em dólares. O usuário
# deve informar, além do valor em reais da compra,
# o valor da cotação do dólar.

# real = float(input("Digite a quantidade de reais = "))
# cotacao = float(input("Digite a cotação do dolar = "))
# dolar = float(real/cotacao)
# print("\nR$ = ", real, "equivale a U$ = ", dolar)

real = float(input("Digite a quantidade de reais = "))
cotacao = float(input("Digite a cotação do dolar = "))
dolar = float(real/cotacao)
print(f"\nR$ = {real:.2f} equivale a U$ = {dolar:.2f}")

