binario = input("Digite um número binário: ")
hexadecimal = f"{int(binario, 2):X}"  # Converte diretamente para hex em maiúsculas
print(f"Hexadecimal: {hexadecimal}")

print()

hexadecimal2 = input("Digite um número hexadecimal: ")
binario2 = f"{int(hexadecimal2, 16):b}"  # Converte diretamente para binário
print(f"Binário: {binario2}")