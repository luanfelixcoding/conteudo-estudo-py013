"""
Você está criando um sistema simples para gerenciar uma lista de compras. 
A ideia é construir a lista com itens digitados pelo usuário, 
organizá-la em ordem alfabética, exibir os itens e, 
no final, limpar a lista para uma nova compra.

OBS: Obrigatório mostrar os números dos itens na lista.

Lista de compras(caso o usuario digite o seguinte):

OUTPUT: 
Lista de compras:
1 - maçã
2 - banana
3 - arroz
4 - feijão
5 - pão

Lista de compras (ordenada):
- arroz
- banana
- feijão
- maçã
- pão

Lista de compras após limpar: []
"""

# Lista vazia
lista_compras = []

# Adicionando itens com append() usando um laço for
for i in range(5):
    item = input(f"{i+1} - ")
    lista_compras.append(item)

# Ordenando em ordem alfabética
lista_compras.sort()

# Mostrando os itens
print("\nLista de compras (ordenada):")
for item in lista_compras:
    print(f"- {item}")

# Limpando a lista
lista_compras.clear()
print(f"\nLista de compras após limpar: {lista_compras}")
