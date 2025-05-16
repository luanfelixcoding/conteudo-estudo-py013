"""
Crie uma função que receba dois dicionários e os una. 
Se uma mesma chave existir nos dois, 
mantenha a do segundo dicionário.

Exemplo de Dicionários:
dict_1 = {"a": 1, "b": 2}
dict_2 = {"b": 3, "c": 4}

OUTPUT:
{'a': 1, 'b': 3, 'c': 4}
"""

# Criando funcao para juntar dicionários


def fusao_dicionarios(dict1: dict, dict2: dict) -> dict:
    resultado = dict1.copy()  # Faz uma cópia do primeiro dicionário
    resultado.update(dict2)   # Atualiza com os valores do segundo
    return resultado


dict1 = {"a": 1, "b": 2}  # Criando dicionário 1
dict2 = {"b": 3, "c": 4}  # Criando dicionário 2
resultado = fusao_dicionarios(dict1, dict2)  # Chamando a função
print(resultado)
