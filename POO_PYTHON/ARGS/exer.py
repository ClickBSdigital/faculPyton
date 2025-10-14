
# DICIONÁRIO - é uma coleção de itens não ordenada, mutável e indexada. 
# Em Python, os dicionários são escritos com chaves {} e possuem chaves e valores.
brinquedo = {
    'marca': 'Lego',    
    'modelo': 'Star Wars',
    'preco': 299.99
}

valor = brinquedo['preco']

print(f"O preço do brinquedo é R$ {valor:.2f}")
print(brinquedo['preco'])


#  quando eu criar uma função que não sei 
#  a quantidade de parametros que ira resceber usar
#  *args
def my_func(param1, *args):
    print(param1)
    for item in args:
        print(item)

    print(args)
    print(len(args) )
    
my_func(10, 20, 30, 40, 50, 60)