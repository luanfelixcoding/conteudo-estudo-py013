# Introdução aos Dicionários (dict) em Python

"""
Dicionários são coleções **não ordenadas**, **mutáveis** e **indexadas por chaves**.

Eles armazenam pares **chave: valor** e são úteis para:
- Representar entidades com atributos (ex: pessoa com nome e idade)
- Buscar dados rapidamente por chave
- Organizar informações de forma estruturada
"""

# Criando um dicionário vazio
pessoa = {}

# Criando um dicionário vazio com dict()
pessoa = dict()

# Preenchendo o dicionário
pessoa = {
    "nome": "Alice",
    "idade": 28,
    "cidade": "Curitiba"
}
print(pessoa)  # {'nome': 'Alice', 'idade': 28, 'cidade': 'Curitiba'}

# Acessando valores
print(pessoa["nome"])         # Saída: Alice
print(pessoa.get("idade"))    # Saída: 28

# Adicionar ou alterar
pessoa["profissão"] = "Engenheira"  # Adiciona nova chave
pessoa["idade"] = 29               # Atualiza valor existente
# {'nome': 'Alice', 'idade': 29, 'cidade': 'Curitiba', 'profissão': 'Engenheira'}
print(pessoa)

# Remover elementos
pessoa.pop("cidade")          # Remove chave específica
print(pessoa)  # {'nome': 'Alice', 'idade': 29, 'profissão': 'Engenheira'}

# Métodos comuns
print(pessoa.keys())          # Retorna todas as chaves
# dict_keys(['nome', 'idade', 'profissão'])

print(pessoa.values())        # Retorna todos os valores
# dict_values(['Alice', 29, 'Engenheira'])

print(pessoa.items())         # Retorna pares (chave, valor)
# dict_items([('nome', 'Alice'), ('idade', 29), ('profissão', 'Engenheira')])

# Verificar se uma chave existe
print("nome" in pessoa)       # True
print("altura" in pessoa)     # False

# Iterar sobre o dicionário
for chave in pessoa:
    print(f"{chave} -> {pessoa[chave]}")

# Ou de forma mais legível e mais usado:
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

# Copiar dicionário
copia = pessoa.copy()
print(copia)  # {'nome': 'Alice', 'idade': 29, 'profissão': 'Engenheira'}

# Limpar dicionário
pessoa.clear()
print(pessoa)  # Saída: {}
