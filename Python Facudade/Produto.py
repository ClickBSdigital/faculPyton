class Produto:
    def __init__(self, nome, marca, modelo,preco):
        self.nome = nome
        self.marca = marca
        self.modelo = modelo
        self.preco = preco
        self.__inicia_prod()

    def mostrar_dados(self): ### Método Get
        return f"Nome: {self.nome} - Marca: {self.marca} - Modelo: {self.modelo} - Preço: {self.preco}" 
    
    def __inicia_prod(self): ### Método Privado
        print(f"Produto: {self.nome}, da marca: {self.marca}, modelo: {self.modelo}. Cadastrado com sucesso!!")

if __name__ == "__main__":
    prod1 = Produto("Smartphone", "Samsung", "Galaxy S21", 3500)
    nome_prod = prod1.get_nome()
    print(f"O nome do produto é: {nome_prod}")