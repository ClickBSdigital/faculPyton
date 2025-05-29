# with open("open/cadastro.txt","a") as f:
#  f.write("novo cadastro\n")
 
# with open("open/cadastro.txt","r") as f:
#  linha = f.readline()
#  print(linha[2])

# with open("open/cadastro.txt","r") as f:
#     for linhas in f:
#         if "eliandro" in linhas.lower():
#            print(linhas)

with open("open/cadastro.txt", "r") as f:
    linhas = f.readlines()  # Lê todas as linhas como uma lista
    del linhas[2]           # Remove a terceira linha (índice 2)

with open("open/cadastro.txt", "w") as f:
    f.writelines(linhas)    # Reescreve o arquivo sem a linha removida

     