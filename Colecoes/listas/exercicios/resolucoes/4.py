"""
Você tem uma lista com os nomes de alunos em ordem de inscrição 
e quer fazer análises básicas.

Lista de alunos:
alunos = ['Ana', 'Bruno', 'Carla', 'Daniel', 'Eduardo', 'Fernanda', 'Gabriel', 'Helena']

Desafio: 
1. Pegue os 3 primeiros nomes.
2. Pegue os 3 últimos nomes.
3. Pegue os nomes dos alunos que estão nas posições pares da lista (0, 2, 4, ...).
4. Inverta a ordem da lista.

OUTPUT:
['Ana', 'Bruno', 'Carla']
['Fernanda', 'Gabriel', 'Helena']
['Ana', 'Carla', 'Eduardo', 'Gabriel']
['Helena', 'Gabriel', 'Fernanda', 'Eduardo', 'Daniel', 'Carla', 'Bruno', 'Ana']
"""

# Lista de alunos
alunos = ['Ana', 'Bruno', 'Carla', 'Daniel',
          'Eduardo', 'Fernanda', 'Gabriel', 'Helena']

# 1. Três primeiros nomes
primeiros_3 = alunos[:3]
print(primeiros_3)

# 2. Três últimos nomes
ultimos_3 = alunos[-3:]
print(ultimos_3)

# 3. Alunos nas posições pares (index 0, 2, 4, ...)
pares = alunos[::2]
print(pares)

# 4. Lista invertida
invertida = alunos[::-1]
print(invertida)
