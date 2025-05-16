"""
Dada uma tupla com vários números inteiros, 
escreva um código que retorne uma nova tupla 
contendo apenas os elementos que aparecem uma única vez.

Tupla de exemplo
numeros = (4, 5, 7, 4, 5, 8, 9, 8, 10)

OUTPUT:
(7, 9, 10)
"""
numeros = (4, 5, 7, 4, 5, 8, 9, 8, 10)

unicos = tuple(num for num in numeros if numeros.count(num) == 1)
"""
# Outra forma de fazer
for num in numeros:
    if numeros.count(num) == 1:
        unicos += (num,)
"""
print(unicos)
