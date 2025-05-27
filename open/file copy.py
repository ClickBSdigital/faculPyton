f = open("open/super.png", "rb")
conteudo = f.read()
f.close()
print(f"Conteúdo binário lido, tamanho: {len(conteudo)} bytes")

