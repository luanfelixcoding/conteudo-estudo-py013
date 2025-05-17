"""
Crie uma função chamada converter_temperatura que receba dois parâmetros:
- valor: a temperatura a ser convertida
- escala_destino: "C" para Celsius ou "F" para Fahrenheit

A função deve converter automaticamente a temperatura e retornar o resultado.

Exemplo de entrada:
100
0

OUTPUT:
37.78
32.0
"""

# Criando a função


def converter_temperatura(valor: float, escala_destino):
    # Verifica se o destino é Celsius
    if escala_destino.upper() == "C":
        # Fahrenheit -> Celsius
        return round((valor - 32) * 5 / 9, 2)

    # Verifica se o destino é Fahrenheit
    elif escala_destino.upper() == "F":
        # Celsius -> Fahrenheit
        return round((valor * 9 / 5) + 32, 2)

    # Escala inválida informada
    else:
        return "Escala inválida. Use 'C' ou 'F'."


# Printando e chamando a função
print(converter_temperatura(100, "C"))  # 37.78
print(converter_temperatura(0, "F"))    # 32.0
