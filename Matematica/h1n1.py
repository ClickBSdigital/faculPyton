# Vamos criar um código Python que calcula a probabilidade usando o Teorema de Bayes
# Dados:
P_H = 0.01  # Probabilidade de ter H1N1 (1%)
P_not_H = 0.99  # Probabilidade de não ter H1N1 (99%)
P_Pos_given_H = 0.90  # Probabilidade de teste positivo dado que tem H1N1
P_Pos_given_not_H = 0.10  # Probabilidade de teste positivo dado que não tem H1N1 (falso positivo)

# Calcular a probabilidade total de teste positivo
P_Pos = (P_Pos_given_H * P_H) + (P_Pos_given_not_H * P_not_H)

# Aplicar Teorema de Bayes para encontrar P(H|Pos)
P_H_given_Pos = (P_Pos_given_H * P_H) / P_Pos

P_H_given_Pos


# ============================
# 🤒 Problema (versão completa):
# Uma doença (H1N1) afeta 1% da população.

# Um teste para detectar a doença tem 90% de acurácia, ou seja:

# Se a pessoa tem H1N1, o teste acerta em 90% dos casos.

# Se a pessoa não tem H1N1, o teste erra em 10% dos casos (falso positivo).

# Suponha que você fez o teste e deu positivo.

# ❓ Qual a probabilidade real de você estar com H1N1, mesmo com o teste positivo?