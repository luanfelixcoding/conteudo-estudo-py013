"""
Crie uma função chamada calcular_juros_compostos que receba:

- capital inicial
- taxa de juros anual (em %)
- tempo em anos

A função deve retornar o valor final após os juros.

Exemplo de entrada:
1000
5
2

OUTPUT:
1102.5
"""


def calcular_juros_compostos(capital, taxa_juros_anual, anos):
    # Converte a taxa percentual para decimal (ex: 5% vira 0.05)
    taxa_decimal = taxa_juros_anual / 100

    # Aplica a fórmula dos juros compostos: M = C * (1 + i)^t
    montante = capital * (1 + taxa_decimal) ** anos

    # Retorna o valor final arredondado para 2 casas decimais
    return round(montante, 2)


# Chamando a função
print(calcular_juros_compostos(1000, 5, 2))  # 1102.5
