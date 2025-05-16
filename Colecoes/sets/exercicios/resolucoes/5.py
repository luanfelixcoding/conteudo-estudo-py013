"""
Você está ajudando na organização de um evento e recebeu duas listas de convidados de diferentes organizadores. 
Cada lista contém nomes (strings) de pessoas convidadas. 
Seu objetivo é identificar:

- Quem foi convidado por ambos os organizadores.

- A lista final de convidados única, sem repetições.

- Quem foi convidado apenas pelo primeiro organizador.

Exemplo de listas:
# Listas dos organizadores
convidados_joao = ["Ana", "Bruno", "Carlos", "Ana", "Daniela"]
convidados_maria = ["Carlos", "Eduardo", "Fernanda", "Bruno", "Fernanda"]

OUTPUT:
{'Carlos', 'Bruno'}
{'Ana', 'Bruno', 'Carlos', 'Daniela', 'Eduardo', 'Fernanda'}
{'Ana', 'Daniela'}
"""

# Listas dos organizadores
convidados_joao = ["Ana", "Bruno", "Carlos", "Ana", "Daniela"]
convidados_maria = ["Carlos", "Eduardo", "Fernanda", "Bruno", "Fernanda"]

# Convertendo as listas em conjuntos
convidados_joao_set = set(convidados_joao)
convidados_maria_set = set(convidados_maria)

# Encontrando os convidados que foram convidados por ambos os organizadores
convidados_comum = convidados_joao_set.intersection(convidados_maria_set)
print(convidados_comum)

# Encontrando a lista final de convidados única, sem repetições
convidados_final = convidados_joao_set.union(convidados_maria_set)
print(convidados_final)

# Encontrando os convidados que foram convidados apenas pelo primeiro organizador
convidados_unicos_joao = convidados_joao_set.difference(convidados_maria_set)
print(convidados_unicos_joao)
