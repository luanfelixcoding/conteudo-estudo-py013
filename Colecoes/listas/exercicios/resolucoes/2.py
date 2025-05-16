"""
Uma empresa tem uma lista com os valores de faturamento de seus vendedores. 
O imposto cobrado é de 15%. 
Você precisa calcular quanto será pago em impostos por cada um.

# Desafio: use map e lambda para calcular o valor do imposto (15%) de cada faturamento.
OBS: Arredonde o valor do imposto para duas casas decimais.

Lista de faturamento:
faturamentos = [12000, 8000, 15000, 5000]

OUTPUT:
[180003.45, 1200.0, 2250.0, 750.0]
"""

faturamentos = [1200023, 8000, 15000, 5000]

# Calculando o imposto de cada faturamento com map e lambda
impostos = list(map(lambda f: round(f * 0.15, 2), faturamentos))
print(impostos)  # [180003.45, 1200.0, 2250.0, 750.0]
