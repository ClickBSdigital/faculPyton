# 60 – Verifique se três lados formam um triângulo (soma de dois lados maior que o terceiro)
a = int(input("Digite o primeiro lado: "))
b = int(input("Digite o segundo lado: "))
c = int(input("Digite o terceiro lado: "))

if a + b > c and a + c > b and b + c > a:
    print("Os três lados formam um triângulo.")
else:
    print("Os três lados não formam um triângulo.")
