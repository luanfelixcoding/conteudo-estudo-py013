"""
Crie uma função chamada formatar_produtos que receba uma lista de dicionários com produtos contendo nome e preco. 
A função deve retornar uma string formatada com nome e preço em reais.

Exemplo de produtos: 
produtos = [
    {"nome": "Arroz", "preco": 5.49},
    {"nome": "Feijão", "preco": 7.90}
]
OUTPUT:
Arroz - R$ 5,49
Feijão - R$ 7,90
"""


def formatar_produtos(lista_produtos):
    linhas = []  # Lista para armazenar as linhas formatadas

    # Percorre cada dicionário da lista
    for produto in lista_produtos:
        nome = produto["nome"]
        preco = produto["preco"]

        # Formata o preço com duas casas decimais e vírgula no lugar do ponto
        linha_formatada = f"{nome} - R$ {preco:.2f}".replace(".", ",")

        # Adiciona à lista de linhas
        linhas.append(linha_formatada)

    # Junta todas as linhas em uma única string separada por quebra de linha
    return "\n".join(linhas)


produtos = [
    {"nome": "Arroz", "preco": 5.49},
    {"nome": "Feijão", "preco": 7.90}
]

print(formatar_produtos(produtos))
