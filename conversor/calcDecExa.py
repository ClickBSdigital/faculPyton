decimal = int(input("Digite um número decimal: "))
print(f"Hexadecimal: {decimal:#X}")  # Com prefixo 0X
# Ou sem prefixo:
print(f"Hexadecimal: {decimal:X}")


print()

hexadecimal = input("Digite um número hexadecimal: ")
decimal = int(hexadecimal, 16)
print(f"Decimal: {decimal}")