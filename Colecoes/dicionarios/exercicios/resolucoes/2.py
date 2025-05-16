"""
Dado um dicionário onde as chaves são nomes de alunos 
e os valores são listas com 3 notas, 
crie um novo dicionário apenas com os alunos que têm média >= 7.

Dicionario de Exemplo:
alunos = {"Ana": [9, 8, 10],
        "Bruno": [6, 7, 5],
        "Carlos": [7, 7, 7]}

OUTPUT:
{'Ana': 9.0, 'Carlos': 7.0}
"""

# Criando a funcao


def alunos_aprovados(notas_alunos):
    aprovados = dict()
    for aluno, notas in notas_alunos.items():
        media = sum(notas) / len(notas)
        if media >= 7:
            aprovados[aluno] = media
    return aprovados


# Criando dicionário
notas = {
    "Ana": [9, 8, 10],
    "Bruno": [6, 7, 5],
    "Carlos": [7, 7, 7]
}
resultado = alunos_aprovados(notas)  # Chamando a função
print(resultado)
