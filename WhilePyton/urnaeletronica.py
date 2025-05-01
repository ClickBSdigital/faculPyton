# Inicializando os contadores
votos_candidatos = [0, 0, 0, 0]  # Candidatos 1, 2, 3, 4
votos_nulos = 0
votos_branco = 0

print("Eleição Presidencial")
print("Códigos válidos: 1,2,3,4 (candidatos), 5=voto nulo, 6=voto em branco")
print("Pressione ENTER sem digitar ou insira código inválido para voto nulo")
print("Digite 0 para encerrar")

while True:
    voto = input("Digite o código do voto: ")
    
    # Se pressionar ENTER sem digitar
    if voto == "":
        votos_nulos += 1
        print("Voto em branco (ENTER) contabilizado como NULO")
        continue
    
    try:
        voto = int(voto)
        
        if voto == 0:
            break  # Encerra a votação
        
        if 1 <= voto <= 4:
            votos_candidatos[voto - 1] += 1
        elif voto == 5:
            votos_nulos += 1
        elif voto == 6:
            votos_branco += 1
        else:
            print("Número inválido! Contabilizado como NULO")
            votos_nulos += 1
    
    except ValueError:
        print("Entrada não numérica! Contabilizado como NULO")
        votos_nulos += 1


# Exibe os resultados
print("\n--- RESULTADOS DA ELEIÇÃO ---")
for i in range(4):
    print(f"Candidato {i + 1}: {votos_candidatos[i]} votos")
print(f"Votos nulos: {votos_nulos}")
print(f"Votos em branco: {votos_branco}")
print("-----------------------------")

# [Código anterior permanece igual...]

# Exibe os resultados
print("\n--- RESULTADOS DA ELEIÇÃO ---")
for i in range(4):
    print(f"Candidato {i + 1}: {votos_candidatos[i]} votos")
print(f"Votos nulos: {votos_nulos}")
print(f"Votos em branco: {votos_branco}")

# Determina o vencedor
max_votos = max(votos_candidatos)
vencedores = [i + 1 for i, votos in enumerate(votos_candidatos) if votos == max_votos]

if len(vencedores) == 1:
    print(f"\n🏆 VENCEDOR: Candidato {vencedores[0]} com {max_votos} votos!")
elif max_votos == 0:
    print("\nℹ️ Nenhum candidato recebeu votos.")
else:
    print(f"\n⚠️ EMPATE entre os candidatos {', '.join(map(str, vencedores))} com {max_votos} votos cada!")

print("-----------------------------")