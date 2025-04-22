# 55 – Verifique se a média de três notas é inferior a 4
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media < 4:
    print("A média é inferior a 4.")
else:
    print("A média não é inferior a 4.")
