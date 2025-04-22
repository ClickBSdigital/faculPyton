# 54 – Verifique se a média de três notas está entre 7 e 10
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = (n1 + n2 + n3) / 3

if 7 <= media <= 10:
    print("A média está entre 7 e 10.")
else:
    print("A média não está entre 7 e 10.")
