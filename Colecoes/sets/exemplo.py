# Introdução aos Sets (Conjuntos) em Python

"""
Sets são coleções **não ordenadas**, **imutáveis** (mas podem ser alteradas),
e **não permitem elementos duplicados**.

Eles são úteis para:
- Remover duplicatas de listas
- Verificar existência de itens rapidamente
- Operações matemáticas como união, interseção e diferença

"""

# Criando um set
meu_set = {1, 2, 3, 3, 4}
print(meu_set)  # Saída: {1, 2, 3, 4} – elimina duplicados

# Ou usando a função set()
outro_set = set([3, 4, 5])
print(outro_set)

# Métodos comuns:
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.union(b))        # União: {1, 2, 3, 4, 5, 6}
print(a.intersection(b))  # Interseção: {3, 4}
print(a.difference(b))   # Diferença: {1, 2}
print(b.difference(a))   # Diferença: {5, 6}
print(a.symmetric_difference(b))  # Diferença simétrica: {1, 2, 5, 6}

# Adicionar e remover
a.add(7)
a.remove(2)      # Se não existir, dá erro
a.discard(10)    # Se não existir, não dá erro

# Verificar existência
print(3 in a)    # True
print(10 in a)   # False

# Iterar sobre um set
for item in a:
    print(item)  # Saída: 1, 3, 4, 5, 6, 7 (em ordem não definida)

# Copiar um set
copia = a.copy()  # Cria uma cópia do set
print(copia)  # Saída: {1, 3, 4, 7}

# Limpar o set
a.clear()  # Remove todos os elementos
print(a)  # Saída: set()


# Comparar sets
print(a == b)  # False
print(a != b)  # True
print(a < b)   # False
print(a <= b)  # False
print(a > b)   # False
print(a >= b)  # False
