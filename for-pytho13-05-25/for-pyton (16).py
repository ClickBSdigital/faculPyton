# 16. Temperaturas: registrar várias e mostrar maior, menor, média, mês e ano

dados = []

while True:
    temp = float(input("Digite a temperatura: "))
    mes = input("Mês: ")
    ano = input("Ano: ")
    dados.append((temp, mes, ano))
    
    cont = input("Deseja continuar? (s/n): ").lower()
    if cont != 's':
        break

# Processamento
maior = max(dados, key=lambda x: x[0])
menor = min(dados, key=lambda x: x[0])
media = sum(d[0] for d in dados) / len(dados)

print(f"\nMaior temperatura: {maior[0]}°C em {maior[1]}/{maior[2]}")
print(f"Menor temperatura: {menor[0]}°C em {menor[1]}/{menor[2]}")
print(f"Média das temperaturas: {media:.2f}°C")