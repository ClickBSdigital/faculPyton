
pessoa = {}

pessoa['nome'] = "Eliandro"

def cria_dicionario(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
        
## chamade de função com argumentos nomeados!!!
cria_dicionario(nome="Eliandro", idade=35, sexo='M', altura=1.55, city='Campão')