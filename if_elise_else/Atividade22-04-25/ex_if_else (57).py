# 57 – Verifique se a temperatura está fora da faixa de 15 a 35 graus
temp = float(input("Digite a temperatura em graus: "))

if temp < 15 or temp > 35:
    print("A temperatura está fora da faixa de 15 a 35 graus.")
else:
    print("A temperatura está dentro da faixa de 15 a 35 graus.")
