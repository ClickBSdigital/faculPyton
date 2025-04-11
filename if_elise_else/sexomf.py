# faça um programa que verifica se uma letra
# digitanda é "F" , "M" ou " O". Conforme
# a letra esvreve : F - Feminino, M - Masculino
# O - Outros ou sexo inválido.
# Solicita a letra do sexo
letra = input("Digite uma letra (F, M ou O): ").upper()

# Verifica e imprime o sexo correspondente
if letra == "F":
    print("Feminino")
elif letra == "M":
    print("Masculino")
elif letra == "O":
    print("Outros")
else:
    print("Sexo inválido!! ")
