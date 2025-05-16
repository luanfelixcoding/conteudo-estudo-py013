"""
Crie uma função que receba uma string e 
retorne um dicionário com a frequência de cada caractere 
(ignorando espaços)

Exemplo de string:
string = "banana"

OUTPUT:
{'b': 1, 'a': 3, 'n': 2}
"""

# Criando a funcao para contar a frequência das letras


def frequencia_caracteres(string: str) -> dict:
    frequencia = {}
    for caractere in string.replace(" ", ""):  # Remove espaços
        frequencia[caractere] = frequencia.get(caractere, 0) + 1
    return frequencia


string = "banana"
resultado = frequencia_caracteres(string)
print(resultado)
