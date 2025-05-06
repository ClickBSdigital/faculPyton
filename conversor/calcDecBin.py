# ## DECIMAL PARA BINÁRIO
# ## 
# decimal = []
# valor = 29 ## é impar 

# novo_val = valor % 2 ## resto da divisão

# print(novo_val) ## valor do resto de 29 / 2

# valor = valor/2

# print(int(valor))

# decimal.insert(0,novo_val)

# print(decimal)



# DECIMAL PARA BINÁRIO

# valor = float(input("Digite um valor em decimal pata converter em Binário: "))
# valor_binario = []

# while valor > 0:
#     novovalor = valor % 2
#     novovalor = int(novovalor)
#     print("Resto : ",novovalor)
#     valor = valor / 2
#     print("Dividendo: ",valor)
#     valor = int(valor)
#     valor_binario.insert(0,novovalor)
    
# print(valor_binario)
# print(valor)


######################

valor = int(input("Digite um valor inteiro para converter em Binário: "))
valor_binario = []
contador_loop = 0  # Variável para contar as iterações

while valor > 0:
    contador_loop += 1  # Incrementa o contador a cada iteração
    novovalor = valor % 2
    valor_binario.insert(0, novovalor)
    valor = valor // 2
    print(f"Iteração {contador_loop}: Resto = {novovalor}, Valor atual = {valor}")

print("Número binário resultante:", valor_binario)
print("Total de Loop:", contador_loop)

 # Convertendo lista para string binária
binario_str = ''.join([str(bit) for bit in valor_binario])
print(f"{valor} em binário é: {binario_str}")

###############################################