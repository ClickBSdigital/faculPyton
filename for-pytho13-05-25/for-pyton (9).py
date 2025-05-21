# 9. Votação com 3 candidatos

votos = [0, 0, 0]
eleitores = int(input("Número de eleitores: "))

for i in range(eleitores):
    voto = int(input("Vote no candidato 1, 2 ou 3: "))
    if voto in [1, 2, 3]:
        votos[voto - 1] += 1
    else:
        print("Voto inválido!")

print(f"Votos Candidato 1: {votos[0]}")
print(f"Votos Candidato 2: {votos[1]}")
print(f"Votos Candidato 3: {votos[2]}")

campeao = votos.index(max(votos)) + 1
print(f"O Candidato vencedor é o {campeao}")