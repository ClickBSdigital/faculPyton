# 1. Abrir e ler o conteúdo inicial do arquivo
f = open("open/file.txt", "r", encoding="utf-8")
print("Conteúdo original:")
print(f.read())
f.close()

# 2. Adicionar um nome (append)
z = open("open/file.txt", "a", encoding="utf-8")
x = input("Digite seu nome para adicionar: ")
z.write(f"{x}\n")
z.close()

# 3. Ler novamente para mostrar o novo conteúdo
z = open("open/file.txt", "r", encoding="utf-8")
print("Conteúdo após adicionar o nome:")
print(z.read())
z.close()

# 4. Limpar o arquivo usando 'w' (escrita - apaga tudo)
h = open("open/file.txt", "w", encoding="utf-8")
h.write("")  # Escreve nada = limpa tudo
h.close()

# 5. Adicionar novo nome após limpar
y = open("open/file.txt", "a", encoding="utf-8")
p = input("Digite seu nome após limpar o arquivo: ")
y.write(f"{p}\n")
y.close()

# 6. Ler e mostrar o conteúdo final
y = open("open/file.txt", "r", encoding="utf-8")
print("Conteúdo final do arquivo:")
print(y.read())
y.close()
