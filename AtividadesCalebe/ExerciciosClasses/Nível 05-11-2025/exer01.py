# 1. Crie uma classe que modele uma pessoa
# (a) Atributos: nome, idade e enderec¸o
# (b) Metodos: mostrar enderec¸o e alterar enderec¸o

from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    idade: int
    endereco: str


    def mostrar_endereco(self) -> str:
        return self.endereco


    def alterar_endereco(self, novo_endereco: str):
        self.endereco = novo_endereco


if __name__ == "__main__":
    p = Pessoa("João", 30, "Rua A, 123")
    print("Endereço atual:", p.mostrar_endereco())
    p.alterar_endereco("Rua B, 456")
    print("Endereço alterado:", p.mostrar_endereco())