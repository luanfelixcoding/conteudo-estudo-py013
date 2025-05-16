"""
Encontre os elementos que estão apenas na primeira lista, 
mas não na segunda:
lista_1 = [1, 2, 3, 4, 5]
lista_2 = [4, 5, 6, 7]

OUTPUT: 
{1, 2, 3}
"""

lista_1 = [1, 2, 3, 4, 5]
lista_2 = [4, 5, 6, 7]

# Convertendo as listas em conjuntos
conjunto_1 = set(lista_1)
conjunto_2 = set(lista_2)

# Encontrando os elementos que estão apenas na primeira lista
resultado = conjunto_1.difference(conjunto_2)

"""
# Outra maneira de fazer
resultado = conjunto_1 - conjunto_2
print(resultado)  # {1, 2, 3}
"""
