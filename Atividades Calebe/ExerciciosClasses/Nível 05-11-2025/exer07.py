# 7. Crie uma classe que modele um carro
# (a) Atributos: marca, ano e prec¸o
# (b) Metodos: mostrar prec¸o e de exibic¸ ´ ao dos dados ˜
# Leia os dados de 5 carros e um valor p, Mostre as informac¸oes de todos os carros com ˜
# prec¸o menor que p.

from dataclasses import dataclass
from typing import List


@dataclass
class Carro:
    marca: str
    ano: int
    preco: float


    def mostrar_preco(self) -> float:
        return self.preco


    def exibir_dados(self) -> str:
        return f"Marca: {self.marca} | Ano: {self.ano} | Preço: R$ {self.preco:.2f}"




def filtrar_carros_por_preco(carros: List[Carro], p: float) -> List[Carro]:
    return [c for c in carros if c.preco < p]


if __name__ == "__main__":
    carros = [
        Carro("Ford", 2010, 25000.0),
        Carro("Chevrolet", 2018, 45000.0),
        Carro("Fiat", 2015, 20000.0),
        Carro("Honda", 2020, 80000.0),
        Carro("Volks", 2012, 18000.0),
    ]
    p = 30000.0
    print(f"Carros com preço menor que R$ {p:.2f}:")
    for c in filtrar_carros_por_preco(carros, p):
        print(c.exibir_dados())