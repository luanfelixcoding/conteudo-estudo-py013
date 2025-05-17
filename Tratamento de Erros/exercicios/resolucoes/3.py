"""
Crie uma função acessar_lista(lista, indice) que tenta acessar um item da lista. 
Se o índice não existir, mostre "Índice inválido".

Exemplo de lista:
lista = [10, 20, 30]

Exemplo de entrada:
print(acessar_lista(lista, 1)) 
print(acessar_lista(lista, 5)) 

OUTPUT:
20
Índice inválido.
None
"""


def acessar_lista(lista, indice):
    try:
        # Tenta acessar o índice informado na lista
        return lista[indice]
    except IndexError:
        # Se o índice não existir, exibe mensagem de erro
        print("Índice inválido.")


lista = [10, 20, 30]  # Criando lista
print(acessar_lista(lista, 1))  # Acesso válido
print(acessar_lista(lista, 5))  # Índice inválido
