"""
Peça uma palavra ao usuario e diga se ela é um 
palíndromo (lê igual de trás para frente)

EXEMPLOS: arara, oso, radar, reviver...

OUTPUT:
Caso Verdadeiro: arara é um palíndromo

Caso Falso: pneu não é um palíndromo
"""

palavra: str = input("Digite alguma palavra: ")

if palavra == palavra[::-1]:
    print(f"{palavra} é um palíndromo")
else:
    print(f"{palavra} não é um palíndromo")
