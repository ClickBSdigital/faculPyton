# Argumentos nomeados **kwargs:
# **kwargs faz um dicionário cujo conteúdo podemos acessar através do nome do argumento.
def local_estudo(**kwargs):
 print(kwargs)
 for key, value in kwargs.items():
  print ("%s == %s" %(key, value))
local_estudo(first ='Senac', second ='Hub', third='Academy')