# Introdução as Listas em Python

"""
Listas são coleções **ordenadas**, **mutáveis** e **permitem elementos duplicados**.
Elas são úteis para armazenar sequências de itens, como números, strings ou até outras listas.
Listas são uma das estruturas de dados mais utilizadas em Python, permitindo fácil manipulação e acesso aos dados.
"""

# Criando uma lista
lista_1 = []

# Criando uma lista com funcao list()
lista_2 = list()

# Lista de strings
nomes = ["Ana", "Carlos", "João"]

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Lista mista
mista = [42, "texto", True, 3.14]

# Lista vazia
vazia = []

# Acessando elementos da lista
lista = ["a", "b", "c", "d"]

print(lista[0])   # 'a' (primeiro elemento)
print(lista[-1])  # 'd' (último elemento)

lista = ["vermelho", "verde", "azul"]
lista[1] = "amarelo"
print(lista)  # ['vermelho', 'amarelo', 'azul']

# Adicionando elementos
lista = [1, 2, 3]
lista.append(4)           # adiciona no final
lista.insert(1, "novo")   # insere na posição 1
print(lista)              # [1, 'novo', 2, 3, 4]

# Removendo elementos
lista = ["a", "b", "c", "d"]

lista.remove("b")     # remove por valor
item = lista.pop()    # remove o último
del lista[0]          # remove por índice


# Pegando o tamanho da lista
# len() retorna o número de elementos
itens = [10, 20, 30]
print(len(itens))  # 3


# Slicing (fatiamento)
# Acessando partes da lista
numeros = [0, 1, 2, 3, 4, 5]

print(numeros[1:4])    # [1, 2, 3]
print(numeros[:3])     # [0, 1, 2]
print(numeros[::2])    # [0, 2, 4]


# Iterando sobre listas
nomes = ["João", "Maria", "Ana"]

for nome in nomes:
    print(nome)

# Verificação de existência na lista
frutas = ["maçã", "banana", "laranja"]

print("banana" in frutas)     # True
print("uva" not in frutas)    # True

# Métodos Comuns
numeros = [3, 1, 4, 2]

numeros.sort()        # ordena em ordem crescente
print(numeros)        # [1, 2, 3, 4]

numeros.sort(reverse=True)  # ordem decrescente
print(numeros)        # [4, 3, 2, 1]

numeros.reverse()     # apenas inverte a ordem atual

numeros.clear()      # remove todos os elementos
print(numeros)        # []

# Copiando listas
# Usando o método copy()
lista_1 = [1, 2, 3]
lista_2 = lista_1.copy()

lista_2.append(4)
print(lista_1)  # [1, 2, 3]
print(lista_2)  # [1, 2, 3, 4]

# Listas aninhadas(listas dentro de listas)
matriz = [
    [1, 2],
    [3, 4]
]

# Acessando elementos de uma lista aninhada
print(matriz[0])    # Acessa a primeira lista: [1, 2]
print(matriz[1])    # Acessa a segunda lista: [3, 4]
print(matriz[0][1])  # Acessa o número 2

# List Comprehension(compreensão de listas)
# Uma maneira concisa de criar listas
# A sintaxe básica é: [expressão for item in iterável]
# Exemplo: Criando uma lista de quadrados
quadrados = [x**2 for x in range(5)]
print(quadrados)  # [0, 1, 4, 9, 16]

# Exemplo: Criando uma lista de pares
pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8]

# Exemplo: Criando uma lista de tuplas
tuplas = [(x, x**2) for x in range(5)]
print(tuplas)  # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)]

# Exemplo: Criando uma lista de sets
sets = [{x, x**2} for x in range(5)]
print(sets)  # [{0}, {1}, {2}, {3}, {4}]

# Exemplo: Criando uma lista de dicionários
dicionarios = [{"numero": x, "quadrado": x**2} for x in range(5)]

# [{'numero': 0, 'quadrado': 0}, {'numero': 1, 'quadrado': 1}, {'numero': 2, 'quadrado': 4}, {'numero': 3, 'quadrado': 9}, {'numero': 4, 'quadrado': 16}]
print(dicionarios)

# Métodos muito úteis
# map() - aplica uma função a todos os itens de um iterável
# filter() - filtra itens de um iterável com base em uma função
# lambda() - função anônima, útil para funções pequenas e rápidas

# Criando uma lista de números
numeros = [1, 2, 3, 4, 5]

# Criando uma função para dobrar os números


def dobrar(x):
    return x * 2


# Usando 'map' para dobrar os números
dobrados = list(map(dobrar, numeros))
print(dobrados)  # [2, 4, 6, 8, 10]

# Usando 'filter' para filtrar números pares


def par(x):
    return x % 2 == 0


# Usando 'filter' para filtrar números pares
pares = list(filter(par, numeros))
print(pares)  # [2, 4]

# Mesmo exemplo com lambda
dobrados = list(map(lambda x: x * 2, numeros))
print(dobrados)  # [2, 4, 6, 8, 10]

pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4]

# Com o uso do lambda, podemos criar funções anônimas de forma rápida e eficiente.
# Não é necessário definir uma função separada para operações simples.
# Isso torna o código mais limpo e fácil de entender.
# No entanto, para funções mais complexas, é melhor usar a definição de função tradicional.
# Isso melhora a legibilidade e a manutenção do código.
