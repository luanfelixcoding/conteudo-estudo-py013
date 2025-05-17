"""
Crie uma função chamada buscar_contato que receba uma 
agenda (dicionário com nomes como chaves e telefones como valores) e um nome. 
A função deve retornar o telefone do contato, ou "Contato não encontrado" se o nome não existir.

Exemplo de Agenda:
agenda = {"João": "9999-1111", "Maria": "8888-2222"}

OUTPUT:
9999-1111
Contato não encontrado
"""

# Criando a funcao


def buscar_contato(agenda, nome):
    # Usa o método get() para buscar o nome com valor padrão
    return agenda.get(nome, "Contato não encontrado")


# Criando a agenda
agenda = {
    "João": "9999-1111",
    "Maria": "8888-2222"
}

# Chamando a funcao
print(buscar_contato(agenda, "João"))  # 9999-1111
print(buscar_contato(agenda, "Ana"))   # Contato não encontrado
