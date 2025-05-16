"""
TUPLAS SÃO IMUTÁVEIS
Não é possível adicionar, remover ou alterar elementos de uma tupla.
"""

# criando uma tupla
tupla = (1, 2, 3, 4, 5)

# acessando os elementos da tupla
print(tupla[0])  # 1
print(tupla[1])  # 2
print(tupla[2])  # 3
print(tupla[3])  # 4
print(tupla[4])  # 5

# acessando os elementos da tupla com slice
print(tupla[0:2])  # (1, 2)
print(tupla[1:3])  # (2, 3)
print(tupla[2:4])  # (3, 4)
print(tupla[3:5])  # (4, 5)
print(tupla[0:5])  # (1, 2, 3, 4, 5)

# acessando os elementos da tupla com slice negativo
print(tupla[-1])  # 5
print(tupla[-2])  # 4
print(tupla[-3])  # 3
print(tupla[-4])  # 2
print(tupla[-5])  # 1

# acessando os elementos da tupla com slice negativo
print(tupla[-5:-3])  # (1, 2)
print(tupla[-4:-2])  # (2, 3)
print(tupla[-3:-1])  # (3, 4)
print(tupla[-2:])  # (2, 3, 4, 5)

# adicionando elementos na tupla
tupla += (6, 7, 8, 9, 10)
print(tupla)  # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# removendo elementos da tupla
# tupla.remove(1)  # TypeError: 'tuple' object has no attribute 'remove'
# tupla.pop(0)  # TypeError: 'tuple' object has no attribute 'pop'
# tupla.clear()  # TypeError: 'tuple' object has no attribute 'clear'

# métodos paliativos para adicionar e remover elementos
tupla = list(tupla)  # convertendo a tupla para lista
tupla.append(11)  # adicionando elemento na lista
tupla.remove(1)  # removendo elemento da lista

tupla = tuple(tupla)  # convertendo a lista de volta para tupla
print(tupla)  # (2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
