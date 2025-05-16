"""
Escreva uma função que inverta as chaves e valores de um dicionário.
Assuma que os valores são únicos e podem ser usados como chaves.

Exemplo de Dicionário:
dicionario = {'a': 1, 'b': 2, 'c': 3}

OUTPUT:
{1: 'a', 2: 'b', 3: 'c'}
"""

# Criando a funcao para inverter o dicionario


def inverter_dicionario(dicionario):
    # Invertendo as chaves e valores usando List Comprehension
    invertido = {v: k for k, v in dicionario.items()}
    return invertido


dicionario = {'a': 1, 'b': 2, 'c': 3}  # Criando o dicionário do enunciado
resultado = inverter_dicionario(dicionario)  # Chamando a função
print(resultado)
