"""
Crie uma função que receba uma tupla de números inteiros e 
retorne uma nova tupla, onde todos os números pares vêm antes 
dos ímpares, mantendo a ordem original dentro de cada grupo.

Tupla de exemplo:
valores = (3, 2, 4, 7, 10, 1, 6)

OUTPUT:
(2, 4, 10, 6, 3, 7, 1)
"""


def separar_pares_impares(tupla: tuple) -> tuple:
    pares = tuple(num for num in tupla if num % 2 == 0)
    impares = tuple(num for num in tupla if num % 2 == 1)

    return tuple(pares) + tuple(impares)


# criando tupla
valores = (3, 2, 4, 7, 10, 1, 6)

# chamando a função
resultado = separar_pares_impares(valores)

# imprimindo o resultado
print(resultado)  # (2, 4, 10, 6, 3, 7, 1)
