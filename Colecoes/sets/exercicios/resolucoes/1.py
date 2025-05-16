"""
Dada a lista abaixo, remova os elementos duplicados usando sets:
numeros = [1, 2, 2, 3, 4, 4, 4, 5]

OUTPUT:
{1, 2, 3, 4, 5}
"""

numeros = [1, 2, 2, 3, 4, 4, 4, 5]

# Converte a lista em um set para remover duplicatas
numeros_unicos = set(numeros)
print(numeros_unicos)
