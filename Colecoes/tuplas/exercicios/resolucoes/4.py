"""
Crie uma função que recebe uma tupla, 
um valor a ser substituído e o novo valor. 
A função deve retornar uma nova tupla com todas as ocorrências
do valor antigo substituídas.

# Exemplo:
tupla = (1, 3, 3, 5, 3, 6)
antigo = 3
novo = 9

# Saída esperada: (1, 9, 9, 5, 9, 6)
"""

# Outra forma de fazer:


"""def substituir(tupla: tuple, antigo: int, novo: int) -> tuple:
    # Converte a tupla em uma lista para facilitar a substituição
    tupla = list(tupla)
    # Percorre a lista e substitui os valores
    for i, num in enumerate(tupla):
        if num == antigo:
            tupla[i] = novo
    # Retorna a lista convertida de volta para tupla
    return tuple(tupla)"""


def substituir(tupla: tuple, antigo: int, novo: int) -> tuple:
    # Usa uma expressão geradora para criar uma nova tupla
    # onde o valor antigo é substituído pelo novo
    # e os outros valores permanecem inalterados
    return tuple(novo if num == antigo else num for num in tupla)


tupla = (1, 3, 3, 5, 3, 6)
antigo = 3
novo = 9

print(substituir(tupla, antigo, novo))
