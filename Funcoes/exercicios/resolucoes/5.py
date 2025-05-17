"""
Crie uma função chamada calcular_frete que receba dois parâmetros:
- peso (em kg)
- expressa (booleano que indica se é entrega expressa)

A regra do frete é:

- Até 1 kg: R$ 10
- De 1.01 kg até 5 kg: R$ 20
- Acima de 5 kg: R$ 30
- Se for expressa, o valor é acrescido de 50%

A função deve retornar o valor final do frete.

OUTPUT:
10
30.0
30
20
30.0
"""


def calcular_frete(peso, expressa):
    # Define o valor base do frete conforme o peso
    if peso <= 1:
        valor = 10
    elif peso <= 5:
        valor = 20
    else:
        valor = 30

    # Se a entrega for expressa, aplica um acréscimo de 50%
    # Multiplicar por 1.5 significa: valor + 50% do valor
    if expressa:
        valor *= 1.5  # Exemplo: 20 * 1.5 = 30 (ou seja, 20 + 10)

    # Retorna o valor final arredondado para 2 casas decimais
    return round(valor, 2)


# Chamando a funcao
print(calcular_frete(0.8, False))  # 10
print(calcular_frete(3, True))     # 30.0
print(calcular_frete(6, False))    # 30
print(calcular_frete(2.5, False))  # 20
print(calcular_frete(2.5, True))   # 30.0
