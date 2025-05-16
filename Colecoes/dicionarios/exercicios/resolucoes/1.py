"""
Crie uma função que receba uma frase e 
retorne um dicionário com a contagem de cada palavra.

Frase Exemplo:
frase = "o rato roeu a roupa do rei de roma"

OUTPUT:
{'o': 1, 'rato': 1, 'roeu': 1, 'a': 1, 'roupa': 1, 'do': 1, 'rei': 1, 'de': 1, 'roma': 1}
"""

# Criando funcao para contar as palavras


def contar_palavras(frase: str) -> dict:
    palavras = frase.split()  # Separando a frase em palavras
    contagem = dict()  # Criando dicionário
    for palavra in palavras:
        contagem[palavra] = contagem.get(palavra, 0)+1
    return contagem


frase = "o rato roeu a roupa do rei de roma"  # Criando a frase do enunciado
resultado = contar_palavras(frase)  # Chamando a funcao
print(resultado)
