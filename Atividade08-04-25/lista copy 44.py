# 44. Multiplicar todos os valores entre si
from functools import reduce
import operator
lista44 = [2, 3, 4]
produto = reduce(operator.mul, lista44)
print(produto)

