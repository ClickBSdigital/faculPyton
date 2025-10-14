# FUNÇÕES COM MÚLTIPLOS ARGUMENTOS
# Argumentos nomeados **kwargs:
# **kwargs faz um dicionário cujo conteúdo podemos acessar através do nome do argumento.
def calculate_tax(value, **kwargs):
 total = 0
 print(kwargs)
 if 'iss' in kwargs:
  total += value * kwargs['iss']
 if 'pis' in kwargs:
  total += value * kwargs['pis']
 return total

calculate_tax(1000, iss=0.05, pis=0.033)
calculate_tax(1000, iss=0.05)
calculate_tax(1000, pis=0.033)  





