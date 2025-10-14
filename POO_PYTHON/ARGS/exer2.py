
pessoa = {}

pessoa['nome'] = input('Nome: ')
pessoa['sexo'] = input('Sexo: [M/F] ').upper()[0]
pessoa['idade'] = int(input('Idade: '))

print(f'O nome é {pessoa["nome"]}')
print(f'O sexo é {pessoa["sexo"]}')
print(f'A idade é {pessoa["idade"]}')
print(f'A pessoa tem {len(pessoa)} chaves')

def cria_dicionario(**kwargs):
    dicionario = {}
    for key, value in kwargs.items():
        dicionario[key] = value
    return dicionario
